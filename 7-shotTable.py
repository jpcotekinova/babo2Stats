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
    print rawItem
    timestamp = rawItem[0]
    killerName = rawItem[1]
    weaponName = rawItem[2]
    killedName =  rawItem[3]

    killerRequest = "(SELECT id from player WHERE name='"+killerName+"')";
    killedRequest = "(SELECT id from player WHERE name='"+killedName+"')";
    weaponRequest = "(SELECT id from weapon WHERE name='"+weaponName+"')";

    gameRequest = "(SELECT id from game WHERE date='"+time.strftime("%Y-%m-%d")+"')";

    
    shotListFile.write("INSERT INTO shot ('killerid','killedid','weaponid','timestamp','gameid') VALUES (" +killerRequest+","+killedRequest+","+weaponRequest+","+timestamp+","+gameRequest+");\n")

shotListFile.close()
killFile.close()
