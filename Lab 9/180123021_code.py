import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def calculateNextPrice(currPrice,mu,sigma,deltaT):
    Z = np.random.normal(0,1)
    drift = (mu - (sigma**2)/2)*deltaT 
    diffusion = sigma*Z*np.sqrt(deltaT)
    nextPrice = currPrice*np.exp(drift + diffusion)
    return nextPrice

def calculatePayoff(S0,mu,sigma,K,N,T):
    # length of a time interval (N equally spaced intervals with total time T)
    deltaT = T/N

    prices = []
    currPrice = S0
    for i in range(N):
        nextPrice = calculateNextPrice(currPrice,mu,sigma,deltaT)
        prices.append(nextPrice)
        currPrice = nextPrice

    payoff = max(0,K - sum(prices)/(N+1))
    return payoff

def asianPut(S0,mu,sigma,K,N,M,T):

    payOffs = []
    for i in range(M):
        payoff = calculatePayoff(S0,mu,sigma,K,N,T)
        payOffs.append(payoff)
    
    #mean
    mu_hat = np.mean(payOffs)
    # standard devaiation
    sigma_hat = np.sqrt(np.var(payOffs))
    
    length = 1.96*sigma_hat/np.sqrt(M)

    print("PART - 1\n")
    print("Mean (mu_hat) = %s " %mu_hat)
    print("Standard Deviation (sigma_hat) = %s " %sigma_hat)
    print("Variance (sigma_hat*sigma_hat) = %s " % (sigma_hat**2))
    print("95%% Confidence Interval = [%s, %s] \n\n" % (mu_hat - length, mu_hat + length))
    return payOffs

def controlVariance(S0,mu,sigma,K,N,M,T,Payoff):
    X = []
    for i in range(M):
        ST = calculateNextPrice(S0,mu,sigma,T)
        payoff = max(0,K-ST)
        X.append(payoff)

    meanX = np.mean(X)
    varX = np.var(X)

    b = 0
    D = 0
    meanPayoff = np.mean(Payoff)
    for i in range(M):
        b += (X[i] - meanX)*(Payoff[i]-meanPayoff)
        D += (X[i] - meanX)*(X[i] - meanX)
    b /= D

    Y = []
    for i in range(M):
        Y.append(Payoff[i] - b*(X[i]-meanX))

    #mean
    mu_hat = np.mean(Y)
    # standard devaiation
    sigma_hat = np.sqrt(np.var(Y))
    
    length = 1.96*sigma_hat/np.sqrt(M)

    print("\nPART - 2\n")
    print("b = %f"%b)

    print("Mean (mu_hat) = %s " %mu_hat)
    print("Standard Deviation (sigma_hat) = %s " %sigma_hat)
    print("Variance (sigma_hat*sigma_hat) = %s " % (sigma_hat**2))
    print("95%% Confidence Interval = [%s, %s] \n\n" % (mu_hat - length, mu_hat + length))

def main():
    dates,prices = readData()
    mu,sigma = computeMuSigma(prices)
    print("mu = %f, sigma = %f\n"%(mu,sigma))

    S0 = prices[len(prices)-1]
    print("S0 (Price on September 30) = %.2f\n"%(S0))    
    
    K = 1.1*S0
    N = 300
    M = 1000
    T = 30

    payOffs = asianPut(S0,mu,sigma,K,N,M,T)
    controlVariance(S0,mu,sigma,K,N,M,T,payOffs)

if __name__ == "__main__":
    main()
