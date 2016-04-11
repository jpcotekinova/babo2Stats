import time
import operator
from collections import OrderedDict

#killFile
with open("killFile.txt") as killFile:
    content = killFile.read().splitlines()

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
    weaponListFile.write("INSERT INTO Weapon (name) VALUES ('" +weapon+"');\n")

weaponListFile.close()
killFile.close()
