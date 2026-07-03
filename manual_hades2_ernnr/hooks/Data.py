from copy import deepcopy

fear_levels = [0, 1, 2, 4, 8, 16, 32]

# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table
# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:
    # Duplicate "Location Clears" locations for each region
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
                    new_location["category"] += f"{fear_level} Fear - Location Clears"
                    location_table.append(new_location)

            # Remove base location
            location_table.remove(location)

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
    for fear_level in fear_levels:
        category_table[f"{fear_level} Fear - Location Clears"] = {
            "hidden": True,
            "yaml_option": [f"locations_{fear_level}_fear_enabled"]
        }
    return category_table

# called after the categories.json file has been loaded
def after_load_option_file(option_table: dict) -> dict:
    # option_table["core"] is the dictionary of modification of existing options
    # option_table["user"] is the dictionary of custom options
    for fear_level in fear_levels:
        option_table["user"][f"locations_{fear_level}_fear_enabled"] = {
            "type": "Toggle",
            "display_name": f"Clear Locations with {fear_level} Fear",
            "description": [f"Adds locations for clearing each location with {fear_level} Fear."],
            "default": False,
            "group": "Location Clear Options"
        }
    return option_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table
