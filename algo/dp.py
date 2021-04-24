#under constructing...
#dp
import csv

def Near(x,y):#550に近いほうを返す
    return x if abs(x-550)<abs(y-550) else y
 
menus=[]
prices=[]
with open ('食堂メニュー.csv','r',encoding='utf-8_sig') as f:
    for menu,price in csv.reader(f):
        menus.append(menu)
        prices.append(int(price))

