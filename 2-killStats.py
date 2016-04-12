import time
import operator
from collections import OrderedDict
import sys

#KillFile
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

filenameList = sys.argv[1].split("!")
filenameList2 = filenameList[1].split(".")
print filenameList2

currentDate = filenameList2[0]


with open('killFile!'+currentDate+'.txt') as f:
    content = f.read().splitlines()

orderedContent = sorted(content, key=str.lower);

playerList = []
playerKilledList = []

stats = {}
statsRatioRaw = {}
statsRatio = {}
statsKilled = {}
statsDied = {}

brief = "BRIEF\n"

timeStr = currentDate
statsKillFileName = "statsKillFile-" + timeStr + ".txt"
statsDiedFileName = "statsDieFile-" + timeStr + ".txt"

statsRatioFileName = "statsRatioFile-" + timeStr + ".txt"

statsKilledFile = open(statsKillFileName, 'w')
statsDiedFile = open(statsDiedFileName, 'w')
statsRatioFile = open(statsRatioFileName, 'w')

for item in orderedContent:
    words = item.split(";")
    playerName = words[1]
    playerKilledName = words[3]

    if playerName != playerKilledName:
        if playerName in playerList :
            stats[playerName]  = stats[playerName] + 1
        else:
            playerList.append(playerName)
            stats[playerName] = 1
            
    if playerKilledName in playerKilledList :
        statsRatioRaw[playerKilledName]  = statsRatioRaw[playerKilledName] + 1
    else:
        playerKilledList.append(playerKilledName)
        statsRatioRaw[playerKilledName] = 1        

statsRatioFile.write("\n=====\n")
statsRatioFile.write("Ratio")
statsRatioFile.write("\n=====\n")
for player in stats:
    statsRatio[player] = float(stats[player])/float(statsRatioRaw[player])

od = OrderedDict(sorted(statsRatio.items(), key=lambda t: t[1], reverse= True))

number = 1
for player in od:
    statsRatioFile.write(str(number).zfill(2) + ":" + player + ":" + str(stats[player])  + ":"+ str(statsRatioRaw[player])  + ":" + str(statsRatio[player])+ "\n")
    number = number +1

statsRatioFile.write("\n")
statsRatioFile.close()

for item in orderedContent:
    words = item.split(";")
    playerName = words[1]
    weaponUsed = words[2]
    playerKilled = words[3]

    if playerName in statsKilled :
        if playerKilled in statsKilled[playerName] :
            statsKilled[playerName][playerKilled]  = statsKilled[playerName][playerKilled] + 1
        else:
            statsKilled[playerName][playerKilled] = 1
    else:
        statsKilled[playerName] = {}
        statsKilled[playerName][playerKilled] = 1

    if playerKilled in statsDied :
        if playerName in statsDied[playerKilled] :
            statsDied[playerKilled][playerName]  = statsDied[playerKilled][playerName] + 1
        else:
            statsDied[playerKilled][playerName] = 1
    else:
        statsDied[playerKilled] = {}
        statsDied[playerKilled][playerName] = 1
    

for player in playerList:
    print (player)
    print (" ")
    print (stats[player])
    print( "\n")

print ("==========","\n")
print ("KILL STATS ","\n")
print ("==========","\n")

brief += "KILL STATS\n"
for player in statsKilled:
    print (player)
    statsKilledFile.write(player+"\n")
    mostKill = 0
    mostKillName= ""
    for playerKilled in statsKilled[player]:
        if mostKill< statsKilled[player][playerKilled]:
            mostKill= statsKilled[player][playerKilled]
            mostKillName = playerKilled
        print ("---", playerKilled, " ", statsKilled[player][playerKilled])    
        statsKilledFile.write("---"+playerKilled+" "+str(statsKilled[player][playerKilled])+"\n")
    print (player, " OWNED ", mostKillName+"\n")
    statsKilledFile.write(player + " OWNED: "+ mostKillName+"\n")
    brief += player + " OWNED: "+ mostKillName+"\n"
    statsKilledFile.write("\n")

print ("==========","\n")
print ("DIE STATS ","\n")
print ("==========","\n")
brief += "\nDIE STATS\n"
for player in statsDied:
    print (player)
    statsDiedFile.write(player+"\n")
    mostDie = 0
    mostDieName= ""
    for playerDied in statsDied[player]:
        if mostDie< statsDied[player][playerDied]:
            mostDie= statsDied[player][playerDied]
            mostDieName = playerDied
        print ("---", playerDied, " ", statsDied[player][playerDied])    
        statsDiedFile.write("---"+playerDied+" "+str(statsDied[player][playerDied])+"\n")
    print (player, " NEMESIS is: ", mostDieName+"\n")
    statsDiedFile.write(player + " NEMESIS is: "+ mostDieName+"\n")
    brief += player + " NEMESIS is: "+ mostDieName+"\n"
    statsDiedFile.write("\n")    

statsKilledFile.write("\n"+brief+"\n")
f.close()
statsKilledFile.close()
statsDiedFile.close()
