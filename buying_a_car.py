'''
description:
https://www.codewars.com/kata/554a44516729e4d80b000012
'''

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    capital=0 #money from savings per month
    month=1
    PriceOld=startPriceOld
    PriceNew=startPriceNew
    if startPriceOld<startPriceNew:
        while capital+PriceOld<=PriceNew:
            month+=1
            PriceOld*=(1-percentLossByMonth/100)
            PriceNew*=(1-percentLossByMonth/100)
            capital+=savingperMonth
            if month%2==0:
               percentLossByMonth+=0.5
        print(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth,capital+PriceOld-PriceNew)
        return [month-1,round(capital+PriceOld-PriceNew)]
    elif startPriceOld>=startPriceNew:
        return [0,capital+PriceOld-PriceNew]
