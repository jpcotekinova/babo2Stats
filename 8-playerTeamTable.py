import time
import operator
from collections import OrderedDict

import sys
#playerfile
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filenameList = sys.argv[1].split("!")
filenameList2 = filenameList[1].split(".")
print filenameList2

currentDate = filenameList2[0]

with open('playerFile!'+currentDate+'.txt') as f:
    content = f.read().splitlines()

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

    #print rawItem1[1]+"-"+rawItem2[1]

    if rawItem2[1] == '0' :
        playerTeamListFile.write("INSERT INTO playerteam (playerid,color) SELECT id,'red' from player WHERE name='"+rawItem1[1]+"';\n")
    else :
        playerTeamListFile.write("INSERT INTO playerteam (playerid,color) SELECT id,'blue' from player WHERE name='"+rawItem1[1]+"';\n")

playerTeamListFile.close()
f.close()
