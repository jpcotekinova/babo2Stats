import time
import operator
from collections import OrderedDict

finalFile = open('SQL-All.txt', 'w')

#playerfile
with open("SQL-game.txt") as gamefile:
    content = (gamefile.read().splitlines())
	
for item in content:
	finalFile.write(item+"\n")
	
with open("SQL-playerList.txt") as playerfile:
    content = (playerfile.read().splitlines())
	
for item in content:
	finalFile.write(item+"\n")
	
with open("SQL-playerTeamList.txt") as playerteamfile:
    content = (playerteamfile.read().splitlines())
	
for item in content:
	finalFile.write(item+"\n")
	
with open("SQL-shotList.txt") as shotfile:
    content = (shotfile.read().splitlines())
	
for item in content:
	finalFile.write(item+"\n")
	
with open("SQL-weaponList.txt") as weaponfile:
    content = (weaponfile.read().splitlines())
	
for item in content:
	finalFile.write(item+"\n")

finalFile.close()
gamefile.close()
playerfile.close()
playerteamfile.close()
shotfile.close()
weaponfile.close()
