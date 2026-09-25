# Generic Manual FAQ

## What is a Manual game?

A Manual game is a custom game that you've set an item list and location list for so that any game can be included in a multiworld game. You'll manually mark locations checked, and you'll manually restrict what items you use based on the items you've been sent.

## How do I install the mod for a Manual game?

You don't. There is no mod. The tasks of marking locations as checked and limiting your items used based on items received is all performed by you (the player) while using the Manual client and its accompanying tracker.

# Hades 2 Manual FAQ

## What does randomization do to Hades 2?

Hades 2 Manual will start you with random Weapons (or Aspects), Keepsakes, and a Gate to either Erebus or Ephyra. The rest of the Items like Weapons, Aspects, Arcana Cards, Grasp, Keepsakes, Familiars, Vows, etc. are all randomly assigned to locations. These locations include clearing a room of enemies, defeating Guardians, defeating Wardens, talking to NPCs, etc.

As you complete the objective at each location, you can mark it as checked in the Manual Tracker. The corresponding item will then be sent to Archipelago. As you receive items from Archipelago, you can choose from the newly available Weapons, Aspects, Arcana Cards, etc. before each attempt.

## What is the goal of the Hades 2 Manual?

The goal is to acquire a certain amount of Grasp (30 by default) and then claim victory by defeating either Chronos or Typhon.

## What do all these terms mean?

The following terms describe items you can collect in Archipelago.

- Gates - Used by the logic in Archipelago to determine what locations are available to be reached. The Archipelago will start with either a Gate to Erebus (Underworld) or Gate to Ephyra (Surface) and gates to other regions will be found throughout the Archipelago. Since the manual can't impose how strict it is to follow the gates, it is up to the player how to follow these rules.
  - "Strict" gates might prevent you from continuing into a region until you've unlocked the gate. For example, even if you've defeated Hecate you can't continue into Oceanus until after you get the Gate to Oceanus, which might be located somewhere else in the Archipelago Multiworld.
  - "Flexible" gates on the other hand will still prevent the Archipelago from including checks in-logic that are behind a locked gate, but the player can decide to continue into that locked region to get out-of-logic checks.
- Grasp - Required to enable Arcana Cards. After collecting the required amount (30 by default), defeat Chronos or Typhon to claim victory and finish this world in Archipelago.
- Weapons - The 6 aspects of night wielded by Melinoe.
- Aspects - Each weapon has 3 aspects and 1 hidden aspect. All the Aspects of Melinoe will just use the Weapon name in the Archipelago (e.g. Witch's Staff).
- Keepsakes - The items given by each Olympian and some NPCs that give Melinoe a special effect for that region.
- Arcana Cards - The passive abilities you can equip to Melinoe at the start of a run. You can only enable Arcana Cards that you have received in the Archipelago up to the amount of Grasp you have received.
- Vows - The challenges you can apply before each run in the Oath of the Unseen. Vows must be collected in Archipelago before enabling them. Optional checks are available for clearing locations or bosses at certain Fear levels (0, 1, 2, 4, 8, 16, 32), which accumulate as you enable different Vows.
- Familiars - Frinos, Raki, Toula, etc. both the normal forms and all their other forms are available to collect in the Archipelago.

The following terms describe locations you can check off in Archipelago.

- Location Clears - An arbitrary check every time you defeat all enemies within a location. Since it can be difficult to track using the in-game location count, it is often easiest to wait until after a Guardian is defeated and then send all checks for the region leading up to the Guardian. If using options for additional Fear based location checks, then consider them to be X or higher fear (i.e. if you have 16 Fear enabled and clear a location, then you can send the 4 Fear, 8 Fear, and 16 Fear checks).
- Guardians - The bosses located at the end of each in-game region (e.g. Hecate).
- Wardens - The mini-bosses located in the middle of each in-game region (e.g. Root Stalker, Uh-Oh).
- Olympians - The Gods that have core boons (e.g. Attack, Special) that can be given to Melinoe. Some Olympians are arbitrarily considered in-logic for the Surface, while others are in-logic for the Underworld.
- NPCs - The other people Melinoe can see during a run who typically provide some benefit (e.g. Arachne). Seeing an NPC in The Crossroads does not count; you must encounter them during a run.

## What Hades 2 save file should I use?

The Hades 2 Manual can be played with either a completed save file with all possible items already unlocked and max level, or with the custom `ProfileX_*.sav` save files included in this repo. If using one of the custom save files provided, then there are additional options in the yaml to add progressive items for the Arcana Cards, Weapons, and Aspects. See the `progressive_*_enabled` options in the yaml for more details.

- [ProfileX_Level_One.sav](../ProfileX_Level_One.sav) has all Weapons and Aspects unlocked at level one. Most Arcana Cards are also at level one, but Awakening cards remain locked so they cannot activate before you receive them in Archipelago. Use this save file when any of the `progressive_*_enabled` options are `true`.
- [ProfileX_Max_Levels.sav](../ProfileX_Max_Levels.sav) has all Weapons and Aspects unlocked at level five. Most Arcana Cards are at level three, but Awakening cards remain locked so they cannot activate before you receive them in Archipelago. Use this save file when all of the `progressive_*_enabled` options are `false`.
- When using your own save file or a completed save file (one can also be found at: https://www.speedrun.com/hades2/resources), then it's recommended to play with `progressive_*_enabled` options set to `false` and `awakening_enabled` set to `false`.

Hades 2 save files can typically be found at "C:\Users\{Your Name}\Saved Games\Hades II" on Windows computers. Make sure to take a backup of any existing save files before replacing them. Rename the custom save (`ProfileX_*.sav`) to match whichever save slot you want to overwrite (e.g. `Profile4.sav`) and then replace the file. For more instructions see: https://www.speedrun.com/hades2/resources.

## How do Awakening Arcana Cards work?

If using a completed save file, Awakening Arcana Cards are activated when certain conditions are met and cannot be disabled otherwise, so they can be tricky to keep track of when playing.

With a completed save file, one option is to exclude Awakening Arcana Cards in the yaml by setting `awakening_enabled` to `false`. This way Awakening Arcana Cards will not be assigned to locations and the Awakening Arcana Cards can be used at any time. This does lead to Judgement becoming incredibly powerful in the early game giving access to Arcana Cards that might otherwise be locked. This can also be done for shorter sessions.

The other option is to include Awakening Arcana Cards in the yaml by setting `awakening_enabled` to `true`. This will randomize the locations of the Arcana Cards, so you will have to take extra care when setting up your Arcana Cards to not enable Awakening Cards you don't have unlocked. However, it can be nearly impossible to avoid activating Awakening Arcana Cards like The Queen until you have a lot of Arcana Cards, so you might have to be lenient on which Arcana Cards you are fine with Awakening early.

If using the custom save file, the Awakening cards have not yet been unlocked. This prevents you from accidentally activating their effects before receiving the corresponding items in Archipelago. Once you receive an item, you can pay to unlock and use that Awakening Arcana Card as usual. Due to its position on the board, Judgement is the only card that also requires finding either Divinity or The Queen before you can purchase it.

## What customization options are there?

The yaml has options for customizing some of the following things. See the documentation within the yaml for more details.

- Underworld only or Surface only options
- Additional Guardian locations
- Additional Fear based locations and Guardians
- Removing Warden or NPC locations
- Adding progressive Arcana Cards, Weapons, and Aspects
- Configuring the amount of Grasp required to claim victory
