import matplotlib.pyplot as plt
import numpy as np
import time

def N(x,mu,var):
    return (1/(np.sqrt(2*var*np.pi)))*(np.exp((-0.5)*(x-mu)*(x-mu)/var))

# Used to generate a bivariate normal distribution
# Z ~ N(0,I2), where I2 is the 2x2 identity matrix
def generateTerm():
    u1 = np.random.rand()
    u2 = np.random.rand()
    R = -2*np.log(u1)
    V = 2*np.pi*u2
    Z1 = (np.sqrt(R))*(np.cos(V))
    Z2 = (np.sqrt(R))*(np.sin(V))
    return Z1,Z2

# generates N(0,1) distibution
def generateDistribution(numTerms):
    X = []
    for i in range(numTerms//2):
        x,y = generateTerm()
        X.append(x)
        X.append(y)
    return X

# converts N(0,1) to N(mu,var)
def convertDistribution(X,mu,var):
    Y = []
    for x in X:
        y = np.sqrt(var)*x + mu
        Y.append(y)
    return Y

def findBucket(x,low,high,num_buckets):
    bucket_size = (high-low)/num_buckets
    return int(np.floor((x-low)/bucket_size))

def plotFunctionAndDistribution(X,mu,var,numTerms):
    # Plotting the actual distribution 
    x = np.linspace(mu-4*np.sqrt(var),mu+4*np.sqrt(var),5000,endpoint=True)
    plt.plot(x,N(x,mu,var),color = 'r',label = 'Actual Distribution')

    # nearly all values would fall in this range   
    low = mu-4*np.sqrt(var)
    high = mu+4*np.sqrt(var)     

    num_buckets = 100
    bucket_size = (high-low)/num_buckets

    buckets = []
    curr = low
    for i in range(num_buckets):
        buckets.append(curr)
        curr += bucket_size
    
    freq = [0]*num_buckets
    for x in X:
        if x >= low and x < high:
            freq[findBucket(x,low,high,num_buckets)] += 1
    
    area = bucket_size*len(X)
    
    for i in range(len(freq)):
        freq[i] /= area

    plt.plot(buckets,freq,label = 'Box Muller')
    plt.xlabel('x')
    plt.ylabel('N(%s,%s)'%(mu,var))
    plt.legend(loc = 'upper right')
    plt.title('Number of Iterations = %s'%(numTerms))
    plt.show()
    plt.clf()
    

def plotDistribution(X,mu,var,numTerms):
    # nearly all values would fall in this range   
    low = mu-4*np.sqrt(var)
    high = mu+4*np.sqrt(var)     

    num_buckets = 100
    bucket_size = (high-low)/num_buckets

    buckets = []
    curr = low
    for i in range(num_buckets):
        buckets.append(curr)
        curr += bucket_size
    
    freq = [0]*num_buckets
    for x in X:
        if x >= low and x < high:
            freq[findBucket(x,low,high,num_buckets)] += 1

    plt.plot(buckets,freq,label = 'Box Muller')
    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.legend(loc = 'upper right')
    plt.title('Number of Iterations = %s'%(numTerms))
    plt.show()
    plt.clf()

def boxMuller(numTerms):
    mu = 0
    var = 1
    start = time.time()
    X = generateDistribution(numTerms)
    end = time.time()
    
    print("Number of iterations = %s"%(numTerms))
    print("Time elapsed =",np.round(end-start,5), "seconds")
    mean = np.mean(X)
    variance = np.var(X)
    print("Mean = " + str(mean) + "\nVariance = " + str(var))
    plotDistribution(X,mu,var,numTerms)

    mu = 0
    var = 5
    Y = convertDistribution(X,mu,var)
    plotFunctionAndDistribution(Y,mu,var,numTerms)

    mu = 5
    var = 5
    Y = convertDistribution(X,mu,var)
    plotFunctionAndDistribution(Y,mu,var,numTerms)

def main():
    boxMuller(100)
    boxMuller(10000)

if __name__ == "__main__":
    main()