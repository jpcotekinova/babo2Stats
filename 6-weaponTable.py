import time
import operator
from collections import OrderedDict

#killFile
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filenameList = sys.argv[1].split("!")
filenameList2 = filenameList[1].split(".")
print filenameList2

currentDate = filenameList2[0]

with open('killFile!'+currentDate+'.txt') as f:
    content = f.read().splitlines()

orderedContent = sorted(content, key=str.lower);

weaponList = []
for item in orderedContent:
    rawItem = item.split(";")
    #print rawItem
    
    if rawItem[2] in weaponList:
        continue
    weaponList.append(rawItem[2])

#print weaponList

weaponListFile = open('SQL-weaponList.txt', 'w')

for weapon in weaponList:
    weaponListFile.write("INSERT INTO weapon (name) VALUES ('" +weapon+"');\n")

weaponListFile.close()
f.close()
