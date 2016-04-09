import time
import operator
from collections import OrderedDict

#playerfile
with open("playerFile.txt") as playerfile:
    content = playerfile.read().splitlines()

orderedContent = sorted(content, key=str.lower);

playerList = []
playerTeamListFile = open('SQL-playerTeamList.txt', 'w')
for item in orderedContent:
    rawItem = item.split(";")
    #print rawItem
    rawItem1 = rawItem[0].split(":")
    rawItem2 = rawItem[6].split(":")
    
    if rawItem1[1] in playerList:
        continue
    playerList.append(rawItem1[1])

    print rawItem1[1]+"-"+rawItem2[1]

    if rawItem2[1] == '0' :
        playerTeamListFile.write("INSERT INTO playerteam (playerid,color) SELECT id,'red' from player WHERE name='"+rawItem1[1]+"';\n")
    else :
        playerTeamListFile.write("INSERT INTO playerteam (playerid,color) SELECT id,'blue' from player WHERE name='"+rawItem1[1]+"';\n")

playerTeamListFile.close()
playerfile.close()
