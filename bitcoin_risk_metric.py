import quandl
import matplotlib.pyplot as plt

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

##def deminishReturns(risk_list):
##    adjRiskList = []
##    x = 1
##    for i in risk_list:
##        #adjRiskList.append(i*(max(risk_list)/((17391*(x)**-0.997))))
##        if i != None:
##            adjRiskList.append(i*1.5)
##        else:
##            adjRiskList.append(None)
##        x = x + 1
##        
##    return adjRiskList

def calculateRisk(baseline):
    risk = []
    x = 0

    for i in baseline:
        if i != None and i != 0 and x > 930:
            risk.append((price[x]/i))
        else:
            risk.append(None)
        x = x + 1
    return risk

##def normalise(data):
##    nomData = []
##    nomData2 = []
##
##    for i in data:
##        if i != 0:
##            nomData.append(i)
##    for i in nomData:
##        #nomData2.append(((i-min(nomData))/(max(nomData)-min(nomData)))+0.1)
##        nomData2.append(((i-min(nomData))/(max(nomData)-min(nomData)))+0.03)
##
##    nomData2.reverse()
##    for i in range(len(data)-len(nomData)):
##        nomData2.append(None)
##    nomData2.reverse()
##        
##    return nomData2

## Retrieve Price Data
price_raw = quandl.get("BCHAIN/MKPRU", authtoken="dRsdc8njMS4QHeKqoJy-").values.tolist()
price = []

for i in price_raw:
    price.append(i[0])

baseline = movingAverage(350, price)

risk = calculateRisk(baseline)

x = range(len(price))

fig, ax = plt.subplots(figsize = (10, 5))
ax2 = ax.twinx()
ax3 = ax.twinx()
ax.plot(x, price, color = 'g')
ax.set_yscale("log")
#ax2.plot(range(len(risk)), risk, color = 'b')
ax2.plot(range(0,1426), risk[0:1426], color = 'y')
ax2.plot(range(1427,2746), risk[1427:2746], color = 'b')
ax2.plot(range(2747,4148), risk[2747:4148], color = 'r')
ax.set_ylim(0.01,100000)
ax3.set_ylim(0,1)
ax2.axes.yaxis.set_visible(False)
ax3.set_yticks([x * 0.1 for x in range(0, 11)])
ax2.set_yscale("log")
plt.grid()
plt.show()
