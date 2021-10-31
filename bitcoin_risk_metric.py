import quandl
import matplotlib.pyplot as plt
import math

##def movingAverage(days, price_list):
##    price_list.reverse()
##    maList = []
##    x = 0
##
##    for i in price_list:
##        sumList = price_list[x:x + days]
##        posIntSumList=[]
##        for j in sumList:
##            if j != 0.0:
##                posIntSumList.append(j)
##        if len(posIntSumList) > 0:
##            maList.append(((sum(posIntSumList)) / len(posIntSumList)))
##        else:
##            maList.append(None)
##        x = x + 1
##
##    maList.reverse()
##    price_list.reverse()
##    return maList

def movingAverage(days, price_list):
    maList = []
    x = 0
    y = 1

    for i in price_list:
        ## until length of price data > days, sum all price data
        if x < days:
            maList.append(sum(price_list[0:x+1])/(x+1))
        ## when length of price data > days, create proper moving average
        else:
            maList.append(sum(price_list[y:x+1])/(days))
            y = y + 1
        x = x + 1
        
    return maList

        
##        sumList = price_list[x:x + days]
##        posIntSumList=[]
##        for j in sumList:
##            if j != 0.0:
##                posIntSumList.append(j)
##        if len(posIntSumList) > 0:
##            maList.append(((sum(posIntSumList)) / len(posIntSumList)))
##        else:
##            maList.append(None)
##        x = x + 1
##
##    maList.reverse()
##    price_list.reverse()
    return maList

##def calculateRisk(baseline, price):
##    risk = []
##    x = 0
##
##    for i in baseline:
##        if i != None and i != 0 and x > 350:
##            risk.append((price[x]/i))
##        else:
##            risk.append(None)
##        x = x + 1
##    return risk

def calculateRisk(baseline, price):
    risk = []
    x = 0

    # Calculate risk by dividing price by moving average
    for i in baseline:
        risk.append((price[x]/i))
        x = x + 1

    return risk

def multiply(data,multiplier):
    mList = []
    for i in data:
        if i != None:
            mList.append(i*multiplier)
        else:
            mList.append(None)
    return mList

def deminishReturns(risk_list):
    adjRiskList = []
    x = 1
    for i in risk_list:
        if i != None:
            adjRiskList.append(i*(max(risk_list[351:])/((17391*(x)**-0.997))))
        else:
            adjRiskList.append(None)
        x = x + 1
        
    return adjRiskList

def deminishReturns2(risk_list):
    adjRiskList = []
    x = 1
    for i in risk_list:
        #if i != None:
        
        #adjRiskList.append(i*(55.924/(-6.402*(math.log(x))+55.924)))
        adjRiskList.append(i*(19.059/(19.059*math.e**(-4*(10**-4*(x))))))
        #else:
            #adjRiskList.append(None)
        x = x + 1
        
    return adjRiskList

def normalise(data):
    nomData = []
    nomData2 = []

    for i in data:
        if i != 0:
            nomData.append(i)
    for i in nomData:
        nomData2.append(((i-min(nomData))/(max(nomData)-min(nomData))))

    nomData2.reverse()
    for i in range(len(data)-len(nomData)):
        nomData2.append(None)
    nomData2.reverse()
        
    return nomData2

def normaliseAndStretch(data,minX,maxY):
    nomData = []
    nomData2 = []

    for i in data:
        if i != 0:
            nomData.append(i)
    for i in nomData:
        nomData2.append(((i-min(nomData))/(max(nomData)-min(nomData))))

    nomData2.reverse()
    for i in range(len(data)-len(nomData)):
        nomData2.append(None)
    nomData2.reverse()

    nomData3 = []
    for i in nomData2:
        nomData3.append((i*(maxY-minX))+minX)
        
    return nomData3

def stretch(data,minX):
    data2 = []
    
    for i in data:
        data2.append((i*(max(data)-minX))+minX)

    return data2

def getPrice():
    # Fetch data
    price_raw = quandl.get("BCHAIN/MKPRU", authtoken="dRsdc8njMS4QHeKqoJy-").values.tolist()
    price = []

    ## Only use price data above 0
    for i in price_raw:
        if i[0] > 0.0:
            price.append(i[0])

    return price

def BenChart1():
    price = getPrice()
    baseline = movingAverage(350, price)
    risk = calculateRisk(baseline, price)

    fig, ax = plt.subplots(figsize = (10, 5))
    ax2 = ax.twinx()
    ax3 = ax.twinx()
    ax.set_yscale("log")
    ax.set_ylim(0.01,100000)
    ax.set_xlim(0,len(price))
    ax3.set_ylim(0,1)
    ax2.axes.yaxis.set_visible(False)
    ax3.set_yticks([x * 0.1 for x in range(0, 11)])
    ax2.set_yscale("log")
    ax.set_ylabel('BTC Price ($)')
    ax3.set_ylabel('Risk')
    ax.set_title('Ben Chart 1')
    plt.grid()

    ax.plot(range(len(price)), price, color = 'b')
    ax2.plot(range(len(risk)), risk, color = 'orange')
    
    plt.show()

def BenChart2():
    price = getPrice()
    baseline = movingAverage(350, price)
    risk = calculateRisk(baseline, price)

    risk1 = risk[860:2140]
    risk2 = multiply(risk[2140:3541], 1.75)
    #risk0 = sub(risk[0:1426], 0)

    fig, ax = plt.subplots(figsize = (10, 5))
    ax2 = ax.twinx()
    ax3 = ax.twinx()
    ax.set_yscale("log")
    ax.set_ylim(0.01,100000)
    ax.set_xlim(0,len(price))
    ax3.set_ylim(0,1)
    ax2.axes.yaxis.set_visible(False)
    ax3.set_yticks([x * 0.1 for x in range(0, 11)])
    ax2.set_yscale("log")
    ax.set_ylabel('BTC Price ($)')
    ax3.set_ylabel('Risk')
    ax.set_title('Ben Chart 2')
    plt.grid()

    ax.plot(range(len(price)), price, color = 'b')
    ax2.plot(range(860,2140), risk1, color = 'orange')
    ax2.plot(range(2140,3541), risk2, color = 'orange')
    
    plt.show()

def BenChart3():
    price = getPrice()
    baseline = movingAverage(350, price)
    risk = calculateRisk(baseline, price)

    risk1 = normalise(risk[860:2140])
    risk2 = multiply(risk[2140:3541], 1.75)
    #risk0 = sub(risk[0:1426], 0)
    adjRisk = deminishReturns(risk)

    fig, ax = plt.subplots(figsize = (10, 5))
    ax2 = ax.twinx()
    ax3 = ax.twinx()
    ax.set_yscale("log")
    ax.set_ylim(0.01,100000)
    ax.set_xlim(0,len(price))
    ax2.set_ylim(0.001,1)
    ax3.set_ylim(0,1)
    ax2.axes.yaxis.set_visible(False)
    ax3.set_yticks([x * 0.1 for x in range(0, 11)])
    ax2.set_yscale("log")
    ax.set_ylabel('BTC Price ($)')
    ax3.set_ylabel('Risk')
    ax.set_title('Ben Chart 3')
    plt.grid()

    ax.plot(range(len(price)), price, color = 'b')
    ax2.plot(range(860,2140), risk1, color = 'orange')
    #ax2.plot(range(2140,3541), risk2, color = 'orange')
    ax.plot(baseline)
    
    plt.show()

def LockyChart():
    price = getPrice()
    baseline = movingAverage(350, price)
    risk = calculateRisk2(baseline, price)
    risk2 = deminishReturns2(risk)

    #hv1 = normalise2(risk[0:850],0.386,22.55)
    #hv2 = normalise2(risk[851:2160],0.358,18.17)
    #hv3 = normalise2(risk[2161:3600],0.418,16.36)
    e1 = normalise2(risk[1610:2678],0.15,1)

##    x = 0
##    while x < 851:
##        hv2.insert(0,None)
##        x = x + 1
##
##    x = 0
##    while x < 2161:
##        hv3.insert(0,None)
##        x = x + 1
    x = 0
    while x < 1610:
        e1.insert(0,None)
        x = x + 1

    
    

    fig, ax = plt.subplots(figsize = (10, 5))
    ax2 = ax.twinx()
    ax3 = ax.twinx()
    ax.set_yscale("log")
    ax.set_ylim(0.01,100000)
    ax2.set_ylim(e1[1610],e1[-1])
    ax.set_xlim(0,len(price))
    ax3.set_ylim(0,1)
    ax2.axes.yaxis.set_visible(False)
    ax3.set_yticks([x * 0.1 for x in range(0, 11)])
    ax2.set_yscale("log")
    ax.set_ylabel('BTC Price ($)')
    ax3.set_ylabel('Risk')
    ax.set_title('Ben Chart 1')
    plt.grid()

    ax.plot(price, color = 'b')
    ax.plot(baseline)
    #ax.plot(baseline2)
    #ax2.plot(risk)
    #ax2.plot(risk2)
    ax2.plot(e1)
    #ax2.plot(hv1)
    #ax2.plot(hv2)
    #ax2.plot(hv3)
    #ax2.plot(range(len(risk)), risk, color = 'orange')
    
    plt.show()

def LockyChart2():
    price = getPrice()
    baseline = movingAverage(350, price) 
    risk = calculateRisk(baseline, price)

    cycle1 = normaliseAndStretch(risk[0:459],0.2,1)
    cycle2 = normaliseAndStretch(risk[460:1609],0.2,1)
    cycle3 = normaliseAndStretch(risk[1610:3041],0.2,1)
    cycle4 = normaliseAndStretch(risk[3042:-1],0.2,1)
    
    normalisedRisk = []
    for i in cycle1:
        normalisedRisk.append(i)
    for i in cycle2:
        normalisedRisk.append(i)
    for i in cycle3:
        normalisedRisk.append(i)
    for i in cycle4:
        normalisedRisk.append(i)
 
    fig, ax = plt.subplots(figsize = (10, 5))
    ax2 = ax.twinx()
    ax3 = ax.twinx()
    ax.set_yscale("log")
    ax.set_ylim(0.01,100000)
    ax.set_xlim(0,len(price))
    ax3.set_ylim(0,1)
    ax2.axes.yaxis.set_visible(False)
    ax3.set_yticks([x * 0.1 for x in range(0, 11)])
    ax2.set_yscale("log")
    ax.set_ylabel('BTC Price ($)')
    ax3.set_ylabel('Risk')
    plt.grid()

    ax.plot(price, color = 'b')
    ax2.plot(normalisedRisk, color = 'orange')
    
    plt.show()

#BenChart1()
#BenChart2()
#BenChart3()
LockyChart2()
    
