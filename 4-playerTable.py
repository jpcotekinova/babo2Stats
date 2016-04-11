import time
import operator
from collections import OrderedDict

#playerfile
with open("playerFile.txt") as playerfile:
    content = playerfile.read().splitlines()

orderedContent = sorted(content, key=str.lower);

playerList = []
for item in orderedContent:
    rawItem = item.split(";")
    #print rawItem
    rawItem = rawItem[0].split(":")
    
    if rawItem[1] in playerList:
        continue
    playerList.append(rawItem[1])

#print playerList

playerListFile = open('SQL-playerList.txt', 'w')

for player in playerList:
    playerListFile.write("INSERT INTO Player (name) VALUES ('" +player+"');\n")

playerListFile.close()
playerfile.close()
