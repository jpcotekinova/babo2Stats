#!/usr/bin/python

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

with open(sys.argv[1]) as f:
    content = f.read().splitlines()

filenameList = sys.argv[1].split("!")
filenameList2 = filenameList[1].split(".")
print filenameList2

currentDate = filenameList2[0]

playerFile = open('playerFile!'+currentDate+'.txt', 'w')
killFile = open('killFile!'+currentDate+'.txt', 'w')

playerKilledDict = {}
playerWeaponDict = {}
index = 0
for item in content:
    index = index + 1
    if item.find("Player")==0:
        item = item.replace("Player ", "Player:")
        item = item.replace(" ID:", "ID:")        
        item = item.replace(" WeaponID", ";WeaponID")
        item = item.replace(" WeaponSide:", ";WeaponSide:")        
        item = item.replace(" SecondaryID:", ";SecondaryID:")        
        item = item.replace(" Position:", ";Position:")
        item = item.replace(" teamID:", ";teamID:")
        
        
        item = item.replace(" spawned", "")
        item = item.replace(" ", "")
        item = item.replace("'", "")
        playerFile.write(item)
        playerFile.write("\n")
    else:
        if item.find("{") == -1:
            if item.find("}") == -1:
                if item.find("R ") != 0:
                    if item.find("----->") != -1:
                        item = item.replace("\"", ".")
                        item = item.replace(" -----", ";")
                        item = item.replace("-----> ", ";")
                        item = item.replace(" ", "")
                        item = item.replace("'", "")
                        killFile.write(str(index))
                        killFile.write(";")
                        killFile.write(item)
                        killFile.write("\n")
            
playerFile.close()
killFile.close()
f.close()
