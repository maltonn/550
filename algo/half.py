# 半分全列挙
import csv
from bisect import bisect_left


def HalfFullEnumeration(contents_half):
    L=[]
    for i in range(2**len(contents_half)):
        tmp=tuple((menu,price) for j,(menu,price) in enumerate(contents_half) if (i>>j)&1)
        menus=tuple(menu for menu,price in tmp)
        total_price=sum(price for menu,price in tmp)
        L.append((menus,total_price))

    L.sort(key=lambda x:x[1])

    menus_lst=[]
    price_lst=[]
    for menus,price in L:
        menus_lst.append(menus)
        price_lst.append(price)

    return menus_lst,price_lst


def main():
    contents=[]
    with open ('食堂メニュー.csv','r',encoding='utf-8_sig') as f:
        for menu,price in csv.reader(f):
            contents.append([menu,int(price)])

    if len(contents)>=50:
        print('contents is too large')
        exit()

    contents_half_1=contents[:len(contents)//2]
    contents_half_2=contents[len(contents)//2:]


    menus_lst_1,price_lst_1=HalfFullEnumeration(contents_half_1)
    menus_lst_2,price_lst_2=HalfFullEnumeration(contents_half_2)

    results=[]
    for menu,price in zip(menus_lst_1,price_lst_1):
        idx=bisect_left(price_lst_2,550-price)

        while True:
            if idx!=len(price_lst_2) and price_lst_2[idx]==550-price:
                results.append(menu+menus_lst_2[idx])
                idx+=1
            else:
                break

    for i in range(10):
        print(results[i])
    print('...\n')
    print(len(results),'種類\n')
    results2=[]
    for menu,price in zip(menus_lst_1,price_lst_1):
        idx=bisect_left(price_lst_2,550-price-5)

        flag=False
        while True:
            if idx!=len(price_lst_2) and abs(price_lst_2[idx]-(550-price))<=5:
                results2.append(menu+menus_lst_2[idx])
                idx+=1
            else:
                if flag:# bisect_leftの性質 
                    break
                else:
                    flag=True
                    idx+=1

    for i in range(10):
        print(results2[i])

    print('...\n')
    print(len(results2),'種類')

    output=[list(res) for res in results]
    output2=[list(res) for res in results2]


    with open ('../client/js/contents.js','w',encoding='utf-8_sig') as f:
        f.write('menus='+str(contents)+'\ncolab='+str(output)+'\ncolab2='+str(output2))

if __name__ == '__main__':
    main()