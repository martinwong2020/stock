import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import pandas_ta
import copy
with open("Input.txt") as UserInput:
  lines=UserInput.readlines()
StockName=lines[0]
StockName=StockName.strip()
# print(type(StockName))
# StockName=input("Enter Stock Name: ")
ticker = yf.Ticker(StockName)
tickerHistory=ticker.history(period="1y")
tickerHigh=tickerHistory["High"]
tickerLow=tickerHistory["Low"]
tickerClose=tickerHistory["Close"]
# tickerDate=tickerHistory["Date"]
x=tickerHistory.index.tolist()
y=tickerClose 
plt.plot(x,y)

# print("newline")
# date=pd.date_range(tickerHistory['1y'])
# x=date
# print(x)
# y=np.array(tickerClose)

# print(tickerClose.info())
#to view the history of the stock

# print(ticker.history(period="1y"))
# print(tickerHistory["Low"])
# print(tickerHistory["High"]
# print(tickerHistory["Close"])
# averagex=sum(tickerClose)/len(tickerClose)
# print(averagex)
trainData=[]
def BestLine(tickerClose,x):
  xsum=0
  averagey=sum(tickerClose)/len(tickerClose)
  # print("I",type(len(x)))
  xlen=len(x)
  xbar=[]
  for i in range(0,xlen):
    xsum=xsum+i
    xbar.append(i)
  averagex=xsum/xlen
  ybar=copy.deepcopy(tickerClose)
  xybar=[]
  xxbar=[]

  for i in range(0,len(tickerClose)):
    ybar[i]=ybar[i]-averagey
    xbar[i]=xbar[i]-averagex
    xybar.append(ybar[i]*xbar[i])
    xxbar.append(xbar[i]*xbar[i])
  # print(ybar)
  # print(averagey)
  slope=sum(xybar)/sum(xxbar)
  yint=averagey-slope*averagex
  Bestx=np.array(range(0,len(x)))
  Besty=slope*Bestx+yint
  plt.plot(x,Besty)
  return slope

Slope=BestLine(tickerClose,x)

def output(slope):
  print("Disclaimer: We are not professional. We are not accountable for your actions based off this program. You are using this at your own risk. We are not financial advisors!!!!! \nThere may be external factors that our algorithm does not account for such as the covid-19 pandemic.")
  if(slope<=0):
    print("\nWe would say since the algorithm we developed shows that the line is decreasing/nonincreasing we don't think this would be an appealing stock to look into.")
  else:
    print("\nThis stock may look appealing for you to do more research on and check on.")
    # print("\nThis is some brief background about the stock:")
    # print( ticker.info["longBusinessSummary"])
    print("\nThe following are the major stake holders in the stock with the # of insituitions holding the shares.")
    print( ticker.major_holders)
    
output(Slope)
plt.legend(["DataSets","Algorithm"],loc="upper right")
plt.show()
with open('Exported.csv', 'w') as OutData:
    OutData.write(str(ticker.history()))
