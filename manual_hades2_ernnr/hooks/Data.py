from copy import deepcopy

fear_levels = [0, 1, 2, 4, 8, 16, 32]
progressive_items = {
    "Arcana Cards": 3,
    "Weapons and Aspects": 5
}

# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table

# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    item_table = duplicate_progressive_items(item_table)
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:
    location_table = duplicate_location_clears(location_table)
    location_table = duplicate_guardian_clears(location_table)
    return location_table

# called after the events.json file has been loaded, before any processing has occurred
# If you need access to the events after processing, you should use the hooks in World.py
def after_load_event_file(event_table: list) -> list:
    return event_table

# called after the regions.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    for category, _ in progressive_items.items():
        category_table[f"Progressive {category}"] = {
            "hidden": True,
            "yaml_option": [f"progressive_{category.lower().replace(' ', '_')}_enabled"]
        }

    for fear_level in fear_levels[1:]:  # Skip 0 Fear since it doesn't need an option
        category_table[f"{fear_level} Fear - Location Clears"] = {
            "hidden": True,
            "yaml_option": [f"locations_{fear_level}_fear_enabled"]
        }
        category_table[f"{fear_level} Fear - Guardians"] = {
            "hidden": True,
            "yaml_option": [f"guardians_{fear_level}_fear_enabled"]
        }
    return category_table

# called after the categories.json file has been loaded
def after_load_option_file(option_table: dict) -> dict:
    # option_table["core"] is the dictionary of modification of existing options
    # option_table["user"] is the dictionary of custom options
    for category, _ in progressive_items.items():
        option_table["user"][f"progressive_{category.lower().replace(' ', '_')}_enabled"] = {
            "type": "Toggle",
            "display_name": f"Progressive {category}",
            "description": [
                f"Adds progressive items for {category}.",
                "Should only be enabled if using a custom save file that has all Weapons, Aspects, and Arcana Cards at level 0 or 1, and the resources necessary to upgrade them.",
                "Should not be enabled if using a completed save file."
                ],
            "default": False,
            "group": "Progressive Item Options"
        }

    for fear_level in fear_levels[1:]:  # Skip 0 Fear since it doesn't need an option
        option_table["user"][f"locations_{fear_level}_fear_enabled"] = {
            "type": "Toggle",
            "display_name": f"Clear Locations with {fear_level} Fear",
            "description": [f"Adds locations for clearing each location with {fear_level} Fear."],
            "default": False,
            "group": "Location Clear Options"
        }
        option_table["user"][f"guardians_{fear_level}_fear_enabled"] = {
            "type": "Toggle",
            "display_name": f"Defeat Guardians with {fear_level} Fear",
            "description": [f"Adds locations for defeating each Guardian with {fear_level} Fear."],
            "default": False,
            "group": "Guardian Options"
        }
    return option_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table


# Duplicates items in the "progressive_items" list, creating extra items with an extra category.
def duplicate_progressive_items(item_table: list) -> list:
    for category, count in progressive_items.items():
        matching_items = []
        for item in item_table:
            categories = item.get("category")
            if isinstance(categories, list) and category in categories:
                matching_items.append(item)

        if matching_items:
            for item in matching_items:
                name = item.get("name")

                new_item = deepcopy(item)
                new_item["name"] = f"Progressive - {name}"
                new_item["category"].remove(category)
                new_item["category"] += [f"Progressive {category}"]
                new_item["count"] = count
                item_table.append(new_item)
    return item_table

# Duplicates locations with the "Location Clears" category for each level of fear, creating new locations with modified names and requirements.
def duplicate_location_clears(location_table: list) -> list:
    matching_locations = []
    for location in location_table:
        categories = location.get("category")
        if isinstance(categories, list) and "Location Clears" in categories:
            matching_locations.append(location)

    if matching_locations:
        for location in matching_locations:
            # Filter and join only the digit characters to get the count
            cleaned_text = "".join(char for char in location.get("name", "") if char.isdigit())
            if not cleaned_text:
                continue

            count = int(cleaned_text)

            # Get the region to construct the name
            region = location.get("region")

            # For each level of fear, create a new location with the same region and categories, but with a modified name and requirement
            for fear_level in fear_levels:
                # Add copies of the base location, so each incrementing location has the same region and categories
                for index in range(1, count + 1):
                    new_location = deepcopy(location)
                    new_location["name"] = f"{fear_level} Fear - {region} Location #{index}"
                    new_location["requires"] = f"{{ItemValue(Fear:{fear_level})}}"
                    if fear_level > 0:
                        new_location["category"] += [f"{fear_level} Fear - Location Clears"]
                    location_table.append(new_location)

            # Remove base location
            location_table.remove(location)

    return location_table

# Duplicates locations with the "Guardians" category for each level of fear, creating new locations with modified names and requirements.
def duplicate_guardian_clears(location_table: list) -> list:
    matching_locations = []
    for location in location_table:
        categories = location.get("category")
        if isinstance(categories, list) and "Guardians" in categories:
            matching_locations.append(location)

    if matching_locations:
        for location in matching_locations:

            # Get the original name to construct the new name
            name = location.get("name")

            # For each level of fear, create a new location with the same region and categories, but with a modified name and requirement
            for fear_level in fear_levels:
                new_location = deepcopy(location)
                new_location["name"] = f"{fear_level} Fear - {name}"
                new_location["requires"] = f"{{ItemValue(Fear:{fear_level})}}"
                if fear_level > 0:
                    new_location["category"] += [f"{fear_level} Fear - Guardians"]
                    new_location.pop("place_item", None)  # Remove place_item for fear levels greater than 0, since Gates are only required for fear 0
                location_table.append(new_location)

            # Remove base location
            location_table.remove(location)

    return location_table
