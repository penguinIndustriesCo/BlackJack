from random import randint

card = None
cardsPulled = []

def drawcard():
    card = randint(1,54)
    if card in cardsPulled:
        return drawcard()  
    else:
        print(card) 
        cardsPulled.append(card)
        cardsPulled.sort()
        return card

print("how many players?")
players = input()

playernum = 0
player = 0
playerdata = []

for playernum in range (int(players)):
    playerdata.append({"playernum": playernum, "stand?": False, "bust?": False, "cards": [], "total": 0})
    
print (playerdata)

for playernum in range (int(players)):
    print("Player " + str(playernum + 1) + ": Get First 2 cards? (y/n)") 
    hit = input()
    if hit == "y":
        for x in range(2):
            card = drawcard()
            playerdata[playernum]["cards"].append(card)
            if 1 <= card <= 4:
                playerdata[playernum]["total"] += 2
            elif 5 <= card <= 8:
                playerdata[playernum]["total"] += 3
            elif 9 <= card <= 12:
                playerdata[playernum]["total"] += 4
            elif 13 <= card <= 16:
                playerdata[playernum]["total"] += 5
            elif 17 <= card <= 20:
                playerdata[playernum]["total"] += 6
            elif 21 <= card <= 24:
                playerdata[playernum]["total"] += 7
            elif 25 <= card <= 28:
                playerdata[playernum]["total"] += 8
            elif 29 <= card <= 32:
                playerdata[playernum]["total"] += 9
            elif 33 <= card <= 36:
                playerdata[playernum]["total"] += 10
            elif 37 <= card <= 40:
                playerdata[playernum]["total"] += 10
            elif 41 <= card <= 44:
                playerdata[playernum]["total"] += 10
            elif 45 <= card <= 48:
                playerdata[playernum]["total"] += 10
            elif 49 <= card <= 52:
                playerdata[playernum]["total"] += 11
        
print(playerdata)

for playernum in range (int(players)):

    if playerdata[playernum]["stand?"] == False:
        print("Player " + str(playernum + 1) + ": Hit? (y/n)") 
        hit = input()
        if hit != "y" or playerdata[playernum]["bust?"] == True:
            playerdata[playernum]["stand?"] = True
        else:
            card = drawcard()
            playerdata[playernum]["cards"].append(card)
            if 1 <= card <= 4:
                playerdata[playernum]["total"] += 2
            elif 5 <= card <= 8:
                playerdata[playernum]["total"] += 3
            elif 9 <= card <= 12:
                playerdata[playernum]["total"] += 4
            elif 13 <= card <= 16:
                playerdata[playernum]["total"] += 5
            elif 17 <= card <= 20:
                playerdata[playernum]["total"] += 6
            elif 21 <= card <= 24:
                playerdata[playernum]["total"] += 7
            elif 25 <= card <= 28:
                playerdata[playernum]["total"] += 8
            elif 29 <= card <= 32:
                playerdata[playernum]["total"] += 9
            elif 33 <= card <= 36:
                playerdata[playernum]["total"] += 10
            elif 37 <= card <= 40:
                playerdata[playernum]["total"] += 10
            elif 41 <= card <= 44:
                playerdata[playernum]["total"] += 10
            elif 45 <= card <= 48:
                playerdata[playernum]["total"] += 10
            elif 49 <= card <= 52:
                playerdata[playernum]["total"] += 11

            if playerdata[playernum]["total"] > 21:
              playerdata[playernum]["bust?"] = True  
    print(playerdata[playernum]["total"])  

