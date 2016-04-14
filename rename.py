# !/usr/bin/python

import os, sys
import re

# listing directories
#print "The dir is: %s"%os.listdir(os.getcwd())

fileList = os.listdir(os.getcwd())



#print fileList
for thisFile in fileList:
    filenamelist = re.split('!|-|\.',thisFile)
    if filenamelist[0] == "console":
        pre, ext = os.path.splitext(thisFile)
        os.rename(thisFile, pre + ".log")
        if int(filenamelist[1]) < 1000:
            year =  filenamelist[3]
            month = filenamelist[2]
            day =   filenamelist[1]

            os.rename(thisFile,"console!"+year+"-"+month+"-"+day+".log")
            
for thisFile in fileList:
    filenamelist = re.split('!|-|\.',thisFile)
    if filenamelist[0] == "statsDieFile":
        pre, ext = os.path.splitext(thisFile)
        os.rename(thisFile, pre + ".txt")        
        if int(filenamelist[1]) < 1000:
            year =  filenamelist[3]
            month = filenamelist[2]
            day =   filenamelist[1]

            os.rename(thisFile,"statsDieFile!"+year+"-"+month+"-"+day+".txt")

for thisFile in fileList:
    filenamelist = re.split('!|-|\.',thisFile)
    if filenamelist[0] == "statsKillFile":        
        pre, ext = os.path.splitext(thisFile)
        os.rename(thisFile, pre + ".txt")        
        if int(filenamelist[1]) < 1000:
            year =  filenamelist[3]
            month = filenamelist[2]
            day =   filenamelist[1]

            os.rename(thisFile,"statsKillFile!"+year+"-"+month+"-"+day+".txt")

for thisFile in fileList:
    filenamelist = re.split('!|-|\.',thisFile)
    if filenamelist[0] == "statsRatioFile":        
        pre, ext = os.path.splitext(thisFile)
        os.rename(thisFile, pre + ".txt")        
        if int(filenamelist[1]) < 1000:
            year =  filenamelist[3]
            month = filenamelist[2]
            day =   filenamelist[1]

            os.rename(thisFile,"statsRatioFile!"+year+"-"+month+"-"+day+".txt")
# renaming directory ''tutorialsdir"
#os.rename("tutorialsdir","tutorialsdirectory")

#print "Successfully renamed."

# listing directories after renaming "tutorialsdir"
#print "the dir is: %s" %os.listdir(os.getcwd())\
