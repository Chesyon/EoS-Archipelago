# EoS-Archipelago
There's not much here right now, but here's hoping that'll change. For now I'm just going to use this readme to store my notes, that people can use as they wish. Please feel welcome to edit this.

## Notes from Archipelago Thread
### ROM Randomization Process
[This spreadsheet](https://docs.google.com/spreadsheets/d/16LUXgBpVGb1Z2gvpKYMjoJ6D5y6RngrfjW1kd4hjtpc/edit?usp=sharing) has more information on the code relevant to this.
1. Unmodified EU ROM (provided by user)
2. Apply base XDelta patch (Chesyon is making it)
3. Dungeon and Pokemon randomization (built off of the Skytemple Randomizer)
4. All the AP code (i apologize that there isn't much here, this is the part that i understand the least.)
5. Generate Wondermail codes (There are existing wondermail generators. The important things are making sure the job client species matches the npc species, and making sure there's a set reward)
6. Generate ASM files (based off of Adex's ASM, plugging in the different Wondermail codes)
7. Import ASM files as special processes (code from SkyTemple)

### Randomization
The [SkyTemple Randomizer](https://github.com/SkyTemple/skytemple-randomizer) will randomize all Pokemon species, and dungeon settings, allowing for a different experience on each playthrough.

### Wondermail
[dengler9/wmsgenerator](https://github.com/dengler9/wmsgenerator) is the core of step 5 of the randomization process. It needs to be ported from JavaScript to Python to be implemented in my WIP randomization script.

### Gameplay
Linear gameplay would NOT work well for this. As such, we've decided to completely change the gameplay flow. There is a 6x6 array of dungeons, called the "labyrinth." At the end of each dungeon is a rest area, including a save point, and potentially an NPC that will assign a mission (see Checks.) The rooms that have NPCs will be randomized. Rest points will connect to all adjacent dungeons in the labyrinth, but unlocking those dungeons is an AP Item. You can travel back to the hub area from any rest point, and you can travel from the hub area to any unlocked dungeon. Dungeons that are farther down in the labyrinth are more difficult (more floors, higher level enemies.) The bottom row of dungeons in the labyrinth will each contain a boss, guarding a "Time Gear." Collecting all six Time Gears will unlock the final dungeon, with a final boss. Defeating the final boss is the objective.

### Items
Dungeon unlocks (36), storage upgrades (8), bag size upgrades (4), other useful consumables such as Golden Seeds and Ginsengs.

### Checks
First time dungeon clears, and mission completions. A proof of concept for using checks can be found [here](https://discord.com/channels/731205301247803413/1175911373822242946/1195200836121403413). In the proof of concept, the AP Item just kills the player, but it is ASM code, so it could theoretically do anything (preferably something that BizHawk can detect!)
