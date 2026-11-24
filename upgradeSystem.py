import random

class upgrade:
    
    def __init__(self):
        self.text = ""
        self.value = 0
        self.change = 0
        self.skibdi = []
        self.upgrades = []
        
    def rollUpgrades(self, a, b, c, d, e, f):
        self.skibdi = []
        options = [a, a, a, b, b, b, b, b, c, c, c, c, c, c, c, d, d, e, e, e, f, f, f, f, f, f, f, f]
        for x in range(3):
            temp = random.randint(0, len(options)-1)
            self.skibdi.append(options[temp])
            options.remove(options[temp])
        
        
    def chooseUpgrade(self):
        loopCondition = 0
        
        while loopCondition == 0:
            
            choice = input("enter your choice 1, 2, or 3")
            
            try:
                if int(choice) >= 1 and int(choice) <= 3:
                    self.upgrades.append(self.skibdi[int(choice)-1])
                    loopCondition = 1
                else:
                    print("invalid input")
            except:
                print("invalid input")
        
        

#OPTIONS:
freeAce = {
    "text": "get a free ace",
    "value": "0"
    }

plusTen = {
    "text": "add 10 to your score",
    "value": "1"
    }

dealerZero = {
    "text": "reset the dealer score to 0",
    "value": "2"
    }

freeMoney = {
    "text": "get a random amount of money between 0 and 10000",
    "value": "3"
    }

redeal = {
    "text": "redeal a new pair of cards",
    "value": "4"
    }

peek = {
    "text": "Look at both the dealer's cards",
    "value": "5"
    }


def ledZeppelin(a):
    print("\nCHOOSE AN UPGRADE")
    a.rollUpgrades(freeAce, plusTen, dealerZero, freeMoney, redeal, peek)
    for x in range(len(a.skibdi)):
        print(f"({x+1}) {a.skibdi[x]['text']}")

    print("\n")
    a.chooseUpgrade()
    print("\nyour upgrades:")
    for x in range(len(a.upgrades)):
        print(a.upgrades[x]["text"])






    
    
