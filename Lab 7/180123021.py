import pandas as pd
import numpy as np

def readData():
    data = pd.read_csv('SBIN.NS.csv',usecols=['Date','Adj Close'])
    prices = []
    dates = []
    for ind in data.index:
        dates.append(data['Date'][ind])
        prices.append(data['Adj Close'][ind])
    return dates,prices

def computeMuSigma(s):
    u = []
    for i in range(1,len(s)):
        u.append(np.log(s[i]/s[i-1]))

    E = np.mean(u)
    n = len(u)

    var = 0
    for i in range(n):
        var += (u[i]-E)*(u[i]-E)
    var /= (n-1)

    sigma = np.sqrt(var)
    mu = var/2 + E

    return mu,sigma

def generateNormal(T):
    Z = 0
    for i in range(T):
        Z += np.random.normal(0,1)
    return Z

def estimateStockPrice(mu,sigma,S0,T):
    estimateVals = []
    for i in range(1000):
        W = generateNormal(T)
        ST = S0*(np.exp(T * (mu - (sigma**2)/2) + sigma*W))
        estimateVals.append(ST)

    estimateVal = np.mean(estimateVals)
    return estimateVal

def calculateStockPrice(mu,sigma,S0,T,date,actual_price):
    estimated_price = estimateStockPrice(mu,sigma,S0,T)
    error = np.absolute((estimated_price-actual_price)/actual_price)*100

    print("Estimated Price on %s = %.2f"%(date,estimated_price))
    print("Actual Price on %s = %.2f"%(date,actual_price))
    print("Error in Estimation = %.2f"%(error),"%")
    print("")

def main():
    dates,prices = readData()
    mu,sigma = computeMuSigma(prices)
    print("mu = %f,sigma = %f\n"%(mu,sigma))

    S0 = prices[len(prices)-1]
    print("S0 (Price on September 30) = %.2f\n"%(S0))

    T = 4
    actual_price_7oct = 190.70
    calculateStockPrice(mu,sigma,S0,T,"October 7",actual_price_7oct)

    T = 9
    actual_price_14oct = 200.05
    calculateStockPrice(mu,sigma,S0,T,"October 14",actual_price_14oct)

    T = 14
    actual_price_21oct = 203.75
    calculateStockPrice(mu,sigma,S0,T,"October 21",actual_price_21oct)

if __name__ == "__main__":
    main()