import random

rooms = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] # all rest areas, as IDs
ValidDungeons = [1,2,3,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,22,23,24,25,26,27,29,30,31,32,33,34,36,37,38,39,40,41] # the IDs of all dungeons in the labyrinth, excluding Final Dungeon and boss rooms
ApItemIDs = [11,12,98,113,114,138,166,175,176,177,181,184,185,198,205,219] # the item IDs for AP checks (specifically those of mission rewards)

def GetSpecies(room):
    actorName = "QUESTGIVE" + str(room)
    actorSpecies = 0 # placeholder
    #actorSpecies = # skytemple stuff to get the actor species (as int) of actorName
    return actorSpecies

def GenWonderMail(ClientSpecies, RewardItemId):
    GeneratedCode = "placeholder"
    # reuse code from dengler9/wmsgenerator (github) here.
    # ClientSpecies will be the client species, the reward type will be an item, the reward item will be RewardItemId, and the dungeon will be a random dungeon in ValidDungeons.
    # Everything else can be random.
    return GeneratedCode; #string

def ImportSpecialProcessEffect(SPId, AsmToImport):
    # Not functional yet. I still don't know how effects_code works, and I'd need to add ArmipsImporter and any files it uses.
    #with open_utf8(AsmToImport, "r") as file:
        #effects_code[SPID] = ArmipsImporter().assemble(file.read())
    print("placeholder import")

roomsWithNpcs = []
while len(roomsWithNpcs) != 16:
    roomsWithNpcs.append(rooms.pop(random.randrange(len(rooms)-1)))

f1 = open("check_for_num_template.asm", "r")
CheckForNumCode = f1.read()
f1.close()
f2 = open("check_for_num.asm", "w")

i = 0
for roomNum in roomsWithNpcs:
    CheckForNumCode = CheckForNumCode.replace(str(i+37), str(roomNum))
    WmCode = GenWonderMail(GetSpecies(roomNum), ApItemIDs[i])
    f = open("mission_template.asm", "r")
    AsmCode = f.read()
    f.close()
    NewAsmCode = AsmCode.replace("TEMPLATE", WmCode)
    NewFileName = "mission" + str(roomNum) + ".asm"
    f = open(NewFileName, "w")
    f.write(NewAsmCode)
    f.close()
    ImportSpecialProcessEffect(roomNum+60, NewFileName)
    i += 1
f2.write(CheckForNumCode)
f2.close()
