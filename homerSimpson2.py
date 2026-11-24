import random
import time
import upgradeSystem

class player:
    
    def __init__(self):
        self.royal = ["J", "Q", "K"]
        self.hand = []
        self.score = 0
        self.aces = 0
        self.moneys = 1000
        self.bust = 0
        
    def deal(self, a):
        for nedFlanders in range(2):
            the = random.randint(0, len(a)-1)
            self.hand.append(a[the])
            if a[the][1] == "A":
                self.aces += 1
            a.remove(a[the])
        
    
    def hit(self, a):
        the = random.randint(0, len(a)-1)
        self.hand.append(a[the])
        a.remove(a[the])
            
            
    def bet(self, a):
        loopCondition = 0
        
        while loopCondition == 0:
            amount = input("enter your bet")
            
            try:
                amount = int(amount)
                
                if amount > self.moneys:
                    print("insufficient funds")
                elif amount <= 0:
                    print("must input a value above 0")
                else:
                    loopCondition = 1
            except:
                
                print("invalid input")

        a += amount
        self.moneys -= amount
        return a
    
    def evaluate(self):
        self.aces = 0
        self.score = 0
        for x in range (len(self.hand)):
            if self.hand[x][1] == "A":
                self.score += 11
                self.aces += 1
            elif self.hand[x][1] in self.royal:
                self.score += 10
            elif self.hand[x][1] == "1":
                self.score += 10
            else:
                self.score += int(self.hand[x][1])
        
        while self.score > 21 and self.aces > 0:
            self.score -= 10
            self.aces -= 1
    
    def show(self):
        for x in range(len(self.hand)):
            print(self.hand[x])
            time.sleep(0.25)
        self.evaluate()
        print(f"score: {self.score}")
        

def end(a,b):
    win = 0
    loss = 0
    draw = 0
    
    if a.score > 21:
        loss += 1
    elif b.score > 21:
        win += 1
    elif a.score == b.score:
        draw = 1
    elif a.score > b.score:
        win += 1
    elif b.score > a.score:
        loss += 1
    
    
    return win, loss, draw


def upgradeStuff(a, b, c, d, e, f):
    if int(a.upgrades[b-1]["value"]) == 0:
        c.hand.append("♣A")
    elif int(a.upgrades[b-1]["value"]) == 1:
        c.hand.append("♣10")
    elif int(a.upgrades[b-1]["value"]) == 2:
        for x in range(len(d.hand)-1):
            d.hand.remove(d.hand[x])
    elif int(a.upgrades[b-1]["value"]) == 3:
        azxs = random.randint(0, 100)
        
        if azxs <= 25:
            cash = random.randint(0, 10)
        elif azxs <= 75:
            cash = random.randint(10, 100)
        elif azxs <= 90:
            cash = random.randint(100, 1000)
        elif azxs <= 98:
            cash = random.randint(1000, 5000)
        else:
            cash = random.randint(5000, 10000)
        
        c.moneys += cash
        print(f"you won £{cash}")
    elif int(a.upgrades[b-1]["value"]) == 4:
        c.hand = []
        c.deal(e)
        c.show()
    elif int(a.upgrades[b-1]["value"]) == 5:
        d.show()

    
    a.upgrades.remove(a.upgrades[b-1])

        
