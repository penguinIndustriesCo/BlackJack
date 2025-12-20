from random import randint

card = None
cardsPulled = []

def drawcard():
    card = randint(1,54)
    if card in cardsPulled:
        drawcard()  
    else:
        print (card) 
        cardsPulled.append(card)
        cardsPulled.sort()
    
drawcard()
drawcard()
print(cardsPulled)

print("how many players?")
players = input()

playernum = 0
player = 0
playerdata = []

for playernum in range (int(players)):
    playerdata.append({"playernum": playernum, "stand?": False, "bust?": False, "cards": [], "total": 0})
    
print (playerdata)

for playernum in range (int(players)):
    print('hit? player' + str(playernum + 1) + " (y/n)") 
    hit = input()
    if hit != "y":
        playerdata[playernum]["stand?"] = True

print (playerdata)
