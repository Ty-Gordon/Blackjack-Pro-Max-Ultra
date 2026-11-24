import homerSimpson2
import loginSystem
import time
import upgradeSystem
import random

player1 = homerSimpson2.player()
dealer = homerSimpson2.player()
options = ["hit", "stand", "h", "s", "", "u", "d"]
options2 = ["hit", "stand", "h", "s", ""]
end = 0
magaggie = upgradeSystem.upgrade()

def numberManipulationThingy(a):
    remoh = len(a) - 1
    barneyGumble = remoh%3
    temp = []

    if barneyGumble > 0:
        for x in range(barneyGumble):
            temp.append(a[x])
        temp.append(",")

    michreal = []

    for x in range(len(a)):
        michreal.append(a[x])

    for x in range(barneyGumble):
        michreal.remove(michreal[0])

    placeholder = len(michreal)//3
    
    z = 0
    for x in range(placeholder):
        for y in range(3):
            temp.append(michreal[z])
            z += 1
        temp.append(",")   
    

    real = "".join(temp[:-1])


    return real

def numberManipulationThingy2(a):
    remoh = len(a)
    barneyGumble = remoh%3
    temp = []

    if barneyGumble > 0:
        for x in range(barneyGumble):
            temp.append(a[x])
        temp.append(",")

    michreal = []

    for x in range(len(a)):
        michreal.append(a[x])

    for x in range(barneyGumble):
        michreal.remove(michreal[0])

    placeholder = len(michreal)//3
    
    z = 0
    for x in range(placeholder):
        for y in range(3):
            temp.append(michreal[z])
            z += 1
        temp.append(",")   
    

    real = "".join(temp[:-1])


    return real
        

def bartSymptom(a, b, c, d, e):
    if  len(a.upgrades) > 0:
                    
        trewq = input("are you sure? y/n")
                    
        if trewq == "y":
            print("\nYOUR UPGRADES")
            for x in range(len(a.upgrades)):
                print(f"({x+1}) {a.upgrades[x]['text']}")
            print("\n")
                
            ieurt = 0
            
            while ieurt == 0:
    
                choosed = input("enter your choice (press 'c' to cancel)")
                
                try:
                    choosed = int(choosed)
                    if choosed <= len(a.upgrades):
                        homerSimpson2.upgradeStuff(a, choosed, b, c, d, e)
                        ieurt = 1
                    else:
                        print("invalid input")
                        
                except:
                    if  choosed == "c":
                        ieurt = 1
                    else:
                        print("invalid input")
                
                    
                    
        b.evaluate()
        print(f"your score: {player1.score}")


def signIn():
    qter = loginSystem.begin()
    success = qter[0]
    position = qter[1]
    bank = int(loginSystem.users[position][2][: -1])
    
    return bank, success, position


def withdraw(a, b, c):
    
        if a > 0:
        
            print(f"you have £{numberManipulationThingy2(str(b))} in the bank")
            loopCondition = 0
            
            while loopCondition == 0:
                amount = input("how much would you like to withdraw?")
                
                try:
                    amount = int(amount)
                    if amount <= 0 or amount > b:
                        print("invalid input")
                    else:
                        loopCondition = 1
                    
                except:
                    print("invalid input")
            
            c.moneys = amount
            total = amount
            b -= amount
        else:
            total = 0
        
        return b, total


def firstBet(a, b):
    a.aces = 0
    b.aces = 0
    
    print("\n")          
    pot = 0
    a.hand = []
    b.hand = []
    
    print(f"you have {numberManipulationThingy2(str(a.moneys))} moneys left")
    pot = a.bet(pot)
    print("\n")
    
    return pot

def reveal(a, b):
    a.deal(cards)
    b.deal(cards)

    print(f"your cards: {a.hand[0]}, {a.hand[1]}\ndealer cards: {b.hand[0]}, ?")
    a.evaluate()
    print(f"your score: {a.score}")
    
def marchSimpson():
    loopCondition = 0
    
    while loopCondition == 0:
        
        choice = input("\nhit(h) or stand(s), double down(d) or use upgrade(u)")
        if choice.lower() not in options:
            print("invalid input")
        else:
            loopCondition = 1
    
    return choice

def playerHit(a):
    a.hit(cards)
    a.show()
    loopCondition = 0
    a.evaluate()
    

def gameLoop(a, b, c, d, e):
    loopCondition = 0
    choice = "h"
    
    while choice in options and loopCondition == 0:
        
        choice = marchSimpson()
        
        if choice.lower() == "d":
            if b <= a.moneys:
                a.moneys -= b
                b = b * 2
                print(f"new stakes: £{numberManipulationThingy2(str(b))}\n")
                playerHit(a)
            else:
                print("insufficient funds")
                    
                    
        if choice.lower() == "s" or choice.lower() == "stand" or choice == "":
            loopCondition = 1
        else:
            loopCondition = 0
                    
        if choice.lower() == "h" or choice.lower() == "hit":
            playerHit(a)
        
        if choice == "u":
            if len(c.upgrades) > 0:
                bartSymptom(c, a, d, cards, e)
            else:
                print("no upgrades left")
        
        if a.score > 21:
            choice = "ausdgbfauisd"
            loopCondition = 1
            print("BUST")
        
    a.evaluate()
    d.evaluate()
    
    return b

def dealerLogic(a, b):
    
    asdx = False
    if b.score == 17:
        lorc = random.randint(1, 15)
        if lorc == 15:
            asdx = True
    elif b.score == 16:
        lorc = random.randint(1, 10)
        if lorc == 10:
            adsx = True
    elif b.score == 15:
        lorc = random.randint(1, 5)
        if lorc == 5:
            asdx = True
    elif b.score == 14:
        lorc = random.randint(1, 3)
        if lorc >= 2:
            asdx = True
    elif b.score <= 13:
        asdx = True
        
    while (b.score < a.score or asdx == True) and b.score < 21 and a.score <= 21:
        b.hit(cards)
        a.evaluate()
        b.evaluate()
    
    print("\n")
    print("PLAYER:")
    a.show()
    print("\n")
    print("DEALER:")
    b.show()
    print("\n")

def finalise(a, b, c, d):
    final = 0
    winCondition = homerSimpson2.end(a, b)

    if winCondition[0] > 0:
        print("you win")
        print(f"+ £{numberManipulationThingy2(str(c))}")
        a.moneys += 2 * c
    elif winCondition[1] > 0:
        print("you lose")
        print(f"- £{numberManipulationThingy2(str(c))}")
    elif winCondition[2] > 0:
        print("draw")
        a.moneys += c
    
    d += 1
    
    if a.moneys > 0:
        end = input("cash out? y/n")
    else:
        end = "y"
    
    if end == "y":
        final = a.moneys
        a.moneys = 0
    
    return final, d

def leaderboard():
    mintel = []
    for x in range(len(loginSystem.users)):
        mintel.append(loginSystem.users[x])
        
    for x in range(len(mintel)+1):
        for x in range(len(mintel)-1):
            if int(mintel[x][2][:-1]) < int(mintel[x+1][2][:-1]):
                r = mintel[x]
                mintel[x] = mintel[x+1]
                mintel[x+1] = r
    print("____________________________")
    print("\n\nTOP 5 RICHEST PLAYERS:\n")
    time.sleep(0.5)
    for x in range(5):
        print(f"({x+1}): {mintel[x][0]} - £{numberManipulationThingy(mintel[x][2])}")
        time.sleep(0.25)
    print("____________________________\n\n")
    
    time.sleep(1)
        
            
    
def balls(a, b, c, d):
    print("\n")
    if a > b:
        print("taking 25% cut...\n")
        a = b + int((a - b) * 3/4)
        time.sleep(1)
        
    if a >= b:
        print(f"you won £{numberManipulationThingy2(str(a - b))}")
    else:
        print(f"you lost £{numberManipulationThingy2(str(0 - (a - b)))}")
    c += a
    print(f"£{numberManipulationThingy2(str(c))} in the bank")
    loginSystem.users[d][2] = str(c) + "\n"

    if c > 0:
        loginSystem.write()
    else:
        print("you ran out of money!")
        print("deleting user")
        loginSystem.users.remove(loginSystem.users[d])
        loginSystem.write()

    iughsd = input("")

while player1.moneys > 0:
    the = signIn()
    bank = the[0]
    success = the[1]
    position = the[2]

    if success > 0:    
        print(f"\n\nWELCOME TO THE GAME {loginSystem.users[position][0].upper()}")
        print("upgrades will be given every 3 hands")
        print("user will be deleted if bankrupt\n\n")
        
        leaderboard()
        
        the = withdraw(success, bank, player1)
        bank = the[0]
        total = the[1]
    else:
        player1.moneys = -1
    
    while player1.moneys > 0 and end != "y" and success > 0:
            
        cards = ["♣A", "♦A", "♥A", "♠A", "♣2", "♦2", "♥2", "♠2", "♣3", "♦3", "♥3", "♠3", "♣4", "♦4", "♥4", "♠4", "♣5", "♦5", "♥5", "♠5", "♣6", "♦6", "♥6" ,"♠6", "♣7", "♦7", "♥7", "♠7", "♣8", "♦8", "♥8", "♠8", "♣9", "♦9", "♥9", "♠9", "♣10", "♦10", "♥10", "♠10", "♣J", "♦J", "♥J", "♠J", "♣Q", "♦Q", "♥Q", "♠Q", "♣K", "♦K", "♥K", "♠K"]

        
        upgradeSystem.ledZeppelin(magaggie)
        
        turns = 0
        
        while turns < 3 and player1.moneys > 0 and end != "y":
            
            pot = firstBet(player1, dealer)
            reveal(player1, dealer)
            pot = gameLoop(player1, pot, magaggie, dealer, total)
            dealerLogic(player1, dealer)
            the = finalise(player1, dealer, pot, turns)
            final = the[0]
            turns = the[1]
            
if success > 0:
    balls(final, total, bank, position)
