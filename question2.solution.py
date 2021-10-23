# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    tup=0,
    totalcost1=0
    totalcost2=0
    for i in orderList:
        tup=i
        if tup[0] =="apples" :
            totalcost1+=tup[1]*fruitShops[0][1]['apples']
            totalcost2+=tup[1]*fruitShops[1][1]['apples']
        elif tup[0] == "oranges" :
            totalcost1+=tup[1]*fruitShops[0][1]['oranges']
            totalcost2+=tup[1]*fruitShops[1][1]['oranges']
    if totalcost1 <totalcost2 :
         print("For orders ", orderList, ", the best shop is : Shop1")
    else:
        print("For orders ", orderList, ", the best shop is  : Shop2")
    return None
orders = [('apples', 1.0), ('oranges', 3.0)]
dir1 = {'apples': 2.0, 'oranges': 1.0}
shop1 = ('shop1', dir1)
dir2 = {'apples': 1.0, 'oranges': 5.0}
shop2 = ('shop2', dir2)
shops = [shop1, shop2]
shopSmart(orders,shops)
orders = [('oranges', 3.0)]
shopSmart(orders,shops)





