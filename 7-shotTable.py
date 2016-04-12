import time
import operator
from collections import OrderedDict

import sys
#killfile
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filenameList = sys.argv[1].split("!")
filenameList2 = filenameList[1].split(".")
print filenameList2

currentDate = filenameList2[0]

with open('killFile!'+currentDate+'.txt') as f:
    content = f.read().splitlines()

orderedContent = sorted(content, key=str.lower);

shotList = []
shotListFile = open('SQL-shotList.txt', 'w')
for item in orderedContent:
    rawItem = item.split(";")
    #print rawItem
    timestamp = rawItem[0]
    killerName = rawItem[1]
    weaponName = rawItem[2]
    killedName =  rawItem[3]
    
	#INSERT INTO `shot` (`id`, `killername`, `killedname`, `weaponname`, `timestamp`, `gametime`) VALUES (NULL, 'dd', 'eee', 'eee', '1', '2016-04-06');
    shotListFile.write("INSERT INTO `shot` (`id`, `killername`, `killedname`, `weaponname`, `timestamp`, `gametime`) VALUES (NULL,'" +killerName+"','"+killedName+"','"+weaponName+"','"+timestamp+"','"+currentDate+"');\n")

shotListFile.close()
f.close()
