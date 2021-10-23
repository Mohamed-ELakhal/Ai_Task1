# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    totalCost = 0.0
    tup=0,
    for i in orderList:
        tup=i
        if tup[0] =="apples" : 
            totalCost+=tup[1]*2.00
        elif tup[0] == "oranges" :
            totalCost+=tup[1]*1.50
        elif tup[0] == "pears" :
            totalCost+=tup[1]*1.75
        elif tup[0] == "limes" :
            totalCost+=tup[1]*0.75
        elif tup[0] == "strawberries" :
            totalCost+=tup[1]*1.00
        else :
            print ("fruit :",tup[0], " doesn’t appear in fruitPrices")
            return None 
    return totalCost
fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}
orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
#Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
orderList = [('oranges', 4.0), ('strawberries', 3.0), ('limes', 4.0)]
print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
#Cost of [('oranges', 4.0), ('strawberries', 3.0), ('limes', 4.0)] is 12.0

