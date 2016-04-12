import time
import operator
from collections import OrderedDict
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filenameList = sys.argv[1].split("!")
filenameList2 = filenameList[1].split(".")
print filenameList2

currentDate = filenameList2[0]

gameFile = open('SQL-game.txt', 'w')

gameFile.write("INSERT INTO game (date) VALUE ('"+currentDate+"');\n")

gameFile.close()
