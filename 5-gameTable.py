import time
import operator
from collections import OrderedDict


timeStr = time.strftime("%d-%m-%Y-%H:%M:%S")

gameFile = open('SQL-game.txt', 'w')

gameFile.write("INSERT INTO game (date) VALUE ("+timeStr+")\n")

gameFile.close()
