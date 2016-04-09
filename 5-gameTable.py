import time
import operator
from collections import OrderedDict

#'2016-04-08 05:19:28'
timeStr = time.strftime("%Y-%m-%d")

gameFile = open('SQL-game.txt', 'w')

gameFile.write("INSERT INTO game (date) VALUE ('"+timeStr+"')\n")

gameFile.close()
