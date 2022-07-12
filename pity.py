import random


#Is Fgo or Genshin More expensive?


def fgoPulls(ssrgoal):
    count=0
    moneyWasted=0
    price=1.7
    ssrhit=0
    while(ssrhit<ssrgoal):
        while True:
            pull = random.randint(1, 100)
            moneyWasted+=price
            if(pull==1 or count==330):
                ssrhit+=1
                count=0
                break
            else:
                count+=1
    return moneyWasted

def genshinPulls(ssrgoal):
    count=0
    moneyWasted=0
    price=2
    ssrhit=0
    while(ssrhit<ssrgoal):
        pityrate=False
        while True:
            if(count>=75):
                pityrate==True  
            pull = random.randint(1, 1000)
            moneyWasted+=price
            if(pull<=6 or count==90):
                ssrhit+=1
                count=0
                break
            elif(pityrate==True and pull<=16):
                ssrhit+=1
                count=0
                break
            else:
                count+=1
    return moneyWasted

def getAvgFgo(ssrgoal):
    counter=0
    total=0
    while(counter<100):
        total+=fgoPulls(ssrgoal)
        counter+=1
    return(total/100)

def getAvgGenshin(ssrgoal):
    counter=0
    total=0
    while(counter<100):
        total+=genshinPulls(ssrgoal)
        counter+=1
    return(total/100)

print("Average Fgo: $"+str(getAvgFgo(1)))
print("Average Genshin: $"+str(getAvgGenshin(1)))
      
