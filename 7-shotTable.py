import time
import operator
from collections import OrderedDict

#killFile
with open("killFile.txt") as killFile:
    content = killFile.read().splitlines()

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
    shotListFile.write("INSERT INTO `shot` (`id`, `killername`, `killedname`, `weaponname`, `timestamp`, `gametime`) VALUES (NULL,'" +killerName+"','"+killedName+"','"+weaponName+"','"+timestamp+"','"+time.strftime("%Y-%m-%d")+"');\n")

shotListFile.close()
killFile.close()
