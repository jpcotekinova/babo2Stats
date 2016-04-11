import time
import operator
from collections import OrderedDict

finalFile = open('SQL-All.txt', 'w')

#playerfile
with open("SQL-game.txt") as gamefile:
    finalFile.write(gamefile.read().splitlines())
	
with open("SQL-playerList.txt") as playerfile:
    finalFile.write(playerfile.read().splitlines())
	
with open("SQL-playerTeamList.txt") as playerteamfile:
    finalFile.write(playerteamfile.read().splitlines())
	
with open("SQL-shotList.txt") as shotfile:
    finalFile.write(shotfile.read().splitlines())
	
with open("SQL-weaponList.txt") as weaponfile:
    finalFile.write(weaponfile.read().splitlines())

finalFile.close()
gamefile.close()
playerfile.close()
playerteamfile.close()
shotfile.close()
weaponfile.close()
