# Hades 2 Manual Archipelago

This repository contains a Manual Archipelago implementation for Hades 2. It is built around a data-driven set of items, locations, regions, and rules that let players randomize progression while still playing the game manually through the Archipelago client and tracker.

## Documentation

For the primary setup and usage guidance, refer to:

- [manual_hades2_ernnr/docs/setup_en.md](manual_hades2_ernnr/docs/setup_en.md) for installation, generation, and joining a multiworld.
- [manual_hades2_ernnr/docs/en_Manual_Hades2_ernnr.md](manual_hades2_ernnr/docs/en_Manual_Hades2_ernnr.md) for the game-specific FAQ, progression overview, and explanation of the manual's rules.

## How the Manual Works

The Hades 2 Manual starts each player with a randomized starting setup: one random weapon or aspect, one random keepsake, and an initial path gate to either Erebus or Ephyra. The rest of the progression is distributed across checks that are completed in-game, such as defeating guardians, meeting NPCs, clearing combat encounters, or reaching other progression milestones.

The main objective is to collect the configured amount of Grasp and then claim victory by defeating either Chronos or Typhon.

## Overview of the Data Folder

The content in the data folder defines the structure of the manual without relying on the Python implementation files.

### Items

The item definitions in [manual_hades2_ernnr/data/items.json](manual_hades2_ernnr/data/items.json) describe the randomized item pool that can be received from Archipelago. These include progression items such as Gates, Weapons, Vows, and Grasp, as well as useful items such as Arcana Cards, Aspects, Keepsakes and Familiars.

### Locations

The location definitions in [manual_hades2_ernnr/data/locations.json](manual_hades2_ernnr/data/locations.json) describe the checks that can be completed in-game. These include guardian encounters, warden encounters, NPC interactions, and the final victory condition. Each location may also include conditions that control when it becomes available or how its reward is placed.

### Regions

The region definitions in [manual_hades2_ernnr/data/regions.json](manual_hades2_ernnr/data/regions.json) define the progression map for the manual. The world is split into the Underworld and Surface paths, with regions such as Erebus, Oceanus, Mourning Fields, Tartarus, Ephyra, Rift of Thessaly, Mount Olympus, and The Summit. Progression flows through these regions and is gated by the appropriate gate items.

### Logic and Options

The logic behind the manual comes from the combination of the region graph, location requirements, and player options:

- [manual_hades2_ernnr/data/regions.json](manual_hades2_ernnr/data/regions.json) defines how regions connect and what gate items are required to enter them.
- [manual_hades2_ernnr/data/locations.json](manual_hades2_ernnr/data/locations.json) defines the requirements for each location and when certain items may be placed there.
- [manual_hades2_ernnr/data/options.json](manual_hades2_ernnr/data/options.json) allows the generator and player to customize the experience, including Underworld and Surface availability, extra guardian checks, wardens and NPC checks, awakening card support, hidden aspects, and the Grasp requirement for victory.
- [manual_hades2_ernnr/data/game.json](manual_hades2_ernnr/data/game.json) provides the base game metadata and the starting inventory setup.
