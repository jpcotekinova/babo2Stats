import time
import operator


from collections import OrderedDict
#playerfile
import sys

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
    playerListFile.write("INSERT INTO player (name) VALUES ('" +player+"');\n")

playerListFile.close()
f.close()
