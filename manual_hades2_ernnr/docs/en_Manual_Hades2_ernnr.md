# Generic Manual FAQ

## What is a Manual game?

A Manual game is a custom game that you've set an item list and location list for so that any game can be included in a multiworld game. You'll manually mark locations checked, and you'll manually restrict what items you use based on the items you've been sent.

## How do I install the mod for a Manual game?

You don't. There is no mod. The tasks of marking locations as checked and limiting your items used based on items received is all performed by you (the player) while using the Manual client and its accompanying tracker.

# Hades 2 Manual FAQ

## What does randomization do to Hades 2?

Hades 2 Manual will start you with 1 random Weapon (or Aspect), 1 random Keepsake, and a Gate to either Erebus or Ephyra. The rest of the Items like Weapons, Aspects, Arcana Cards, Grasp, Keepsakes, Familiars, Vows, etc. are all randomly assigned to locations. These locations include clearing a room of enemies, defeating Guardians, defeating Wardens, talking to NPCs, etc.

As you complete the objective of each location, you can check it off of the Manual Tracker and the corresponding item will be sent to the Archipelago. As your items are sent from the Archipelago, you will be able to chose from the newly available Weapons, Aspects, Arcana Cards, etc. before each attempt.

## What is the goal of the Hades 2 Manual?

The goal is to acquire a configurable amount of Grasp and then Claim Victory against either Chronos or Typhon.

## What Hades 2 save file should I use?

The Hades 2 Manual can be played with either a completed save file with all possible items already unlocked and max level, or with the custom `ProfileX.sav` save file that has all items unlocked but at level 1. If necessary, a completed save file and instructions can be found at: https://www.speedrun.com/hades2/resources.

If using the custom save file provided, then there are additional options in the yaml to add progressive items for the Arcana Cards, Weapons, and Aspects. See the `progressive_*_enabled` options in the yaml for more details.

Hades 2 save files can typically be found at "C:\Users\{Your Name}\Saved Games\Hades II" on windows computers. Make sure to take a backup of any existing save files before replacing them. Rename the custom save (`ProfileX.sav`) to match whichever save slot you want to overwrite (e.g. `Profile4.sav`) and then replace the file.

## How do Awakening Arcana Cards work?

If using a completed save file, Awakening Arcana Cards are activated when certain conditions are met and cannot be disabled otherwise, so they can be tricky to keep track of when playing.

With a completed save file, one option is to exclude Awakening Arcana Cards in the yaml by setting `awakening_enabled` to `false`. This way Awakening Arcana Cards will not be assigned to locations and the Awakening Arcana Cards can be used at any time. This does lead to Judgement becoming incredibly powerful in the early game giving access to Arcana Cards that might otherwise be locked. This can also be done for shorter sessions.

The other option is to include Awakening Arcana Cards in the yaml by setting `awakening_enabled` to `true`. This will randomize the locations of the Arcana Cards, so you will have to take extra care when setting up your Arcana Cards to not enable Awakening Cards you don't have unlocked. However, it can be nearly impossible to avoid activating Awakening Arcana Cards like The Queen until you have a lot of Arcana Cards, so you might have to be lenient on which Arcana Cards you are fine with Awakening early.

If using the custom save file, then the awakening cards have not yet been unlocked. This will prevent you from accidentally activating their effect until the item has been received in the Archipelago. Once you have received the item in the Archipelago, then you can pay to unlock and use the Awakening Arcana Cards like normal. Due to it's position on the board, Judgement is the only card that will also require finding either Divinity or The Queen before being able to purchase it.

## How do the Gates work?

There are Gates that lock access for every region in Hades 2. You will always randomly start with 1 Initial Gate for either Erebus or Ephyra and the other Initial Gate will be in a random location. Each 0 Fear Guardian will have a Gate to the next region. For example, Hecate has the Gate to Oceanus.

## What customization options are there?

The yaml has options for customizing some of the following things. See the documentation within the yaml for more details.

- Underworld only or Surface only options
- Additional Guardian locations
- Additional Fear based locations and Guardians
- Removing Warden or NPC locations
- Adding progressive Arcana Carads, Weapons, and Aspects
- Configuring the amount of Grasp for to Claim Victory
