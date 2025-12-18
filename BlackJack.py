from random import randint

card = None
cardsPulled = []

def drawcard():
    card = randint(1,54)
    if card in cardsPulled:
        print("Same card, re-pulling")
        drawcard()  
    else:
        print (card) 
        cardsPulled.append(card)
    
drawcard()
drawcard()
print(cardsPulled)
