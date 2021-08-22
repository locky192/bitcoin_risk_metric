import quandl
import matplotlib.pyplot as plt

## Magic Number
## y = 17391x^(-0.997)

def movingAverage(days, price_list):
    price_list.reverse()
    maList = []
    x = 0

    for i in price_list:
        sumList = price_list[x:x + days]
        posIntSumList=[]
        for j in sumList:
            if j != 0.0:
                posIntSumList.append(j)
        if len(posIntSumList) > 0:
            maList.append(((sum(posIntSumList)) / len(posIntSumList)))
        else:
            maList.append(None)
        x = x + 1

    maList.reverse()
    price_list.reverse()
    return maList

def EMA(length, data):
    x = 0
    emalist = []
    for i in data:
        if i != 0.0:
            emalist.append((i*(2/(1+length)))+(emalist[x-1]*(1-(2/(1+length)))))
        else:
            if data[x+1] != 0:
                emalist.append(data[x+1])
            else:
                emalist.append(None)
        x = x + 1
    return emalist

def deminishReturns(risk_list):
    adjRiskList = []
    x = 1
    for i in risk_list:
        adjRiskList.append(i*(max(risk_list)/((17391*(x)**-0.997))))
        x = x + 1
        
    return adjRiskList

def calculateRisk(baseline):
    risk = []
    x = 0

    for i in baseline:
        if i != None and i != 0 and x > 930:
            risk.append(price[x]/i)
        else:
            risk.append(0)
        x = x + 1
    return risk

def normalise(data):
    nomData = []
    for i in data:
        nomData.append((i-min(data))/(max(data)-min(data)))
    return nomData

## Retrieve Price Data
price_raw = quandl.get("BCHAIN/MKPRU", authtoken="dRsdc8njMS4QHeKqoJy-").values.tolist()
price = []
for i in price_raw:
    price.append(i[0])

baseline = movingAverage(350, price)

risk = calculateRisk(baseline)

#adjustedRisk = deminishReturns(risk)

nomRisk = normalise(risk)

x = range(len(price))

fig, ax = plt.subplots(figsize = (10, 5))
ax2 = ax.twinx()
ax3 = ax.twinx()
ax.plot(x, price, color = 'g')
ax.set_yscale("log")
ax2.plot(x, nomRisk, color = 'b')
ax.set_ylim(0.01,100000)
ax3.set_ylim(0,1)
ax2.axes.yaxis.set_visible(False)
ax3.set_yticks([x * 0.1 for x in range(0, 11)])
#ax2.set_ylim(0.027,1)
ax2.set_yscale("log")
#ax.plot(baseline)
plt.show()
