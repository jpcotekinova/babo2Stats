with open("console.log") as f:
    content = f.read().splitlines()

playerFile = open('playerFile.txt', 'w')
killFile = open('killFile.txt', 'w')

playerKilledDict = {}
playerWeaponDict = {}
for item in content:
    if item.find("Player")==0:
        item = item.replace("Player ", "Player:")
        item = item.replace(" ID:", "ID:")        
        item = item.replace(" WeaponID", ";WeaponID")
        item = item.replace(" WeaponSide:", ";WeaponSide:")        
        item = item.replace(" SecondaryID:", ";SecondaryID:")        
        item = item.replace(" Position:", ";Position:")
        item = item.replace(" teamID:", ";teamID:")
        
        
        item = item.replace(" spawned", "")
        item = item.replace(" ", "")
        item = item.replace("'", "")
        playerFile.write(item)
        playerFile.write("\n")
    else:
        if item.find("{") == -1:
            if item.find("}") == -1:
                if item.find("R ") != 0:
                    if item.find("----->") != -1:
                        item = item.replace("\"", ".")
                        item = item.replace("'", ".")
                        item = item.replace(" -----", ";")
                        item = item.replace("-----> ", ";")
                        
                        killFile.write(item)
                        killFile.write("\n")
            
playerFile.close()
killFile.close()
f.close()
