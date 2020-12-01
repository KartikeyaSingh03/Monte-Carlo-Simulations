import matplotlib.pyplot as plt
import numpy as np
import time

def N(x,mu,var):
    return (1/(np.sqrt(2*var*np.pi)))*(np.exp((-0.5)*(x-mu)*(x-mu)/var))

def Y(x):
    return np.sqrt(-2*np.log(x)/x)

# Used to generate a bivariate normal distribution
# Z ~ N(0,I2), where I2 is the 2x2 identity matrix
def generateTerm():
    X = 100
    it = 0
    while X>1:
        it += 1
        u1 = np.random.rand()
        u2 = np.random.rand()
        u1 = 2*u1-1
        u2 = 2*u2-1
        X = u1*u1 + u2*u2
    y = Y(X)
    Z1 = u1*y
    Z2 = u2*y
    return Z1,Z2,it

# generates N(0,1) distibution
def generateDistribution(numTerms):
    X = []
    iterations = []
    for i in range(numTerms//2):
        x,y,it = generateTerm()
        X.append(x)
        X.append(y)
        iterations.append(it)
    return X,iterations

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

    plt.plot(buckets,freq,label = 'Marsgalia Bray')
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

    plt.plot(buckets,freq,label = 'Marsgalia Bray')
    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.legend(loc = 'upper right')
    plt.title('Number of Iterations = %s'%(numTerms))
    plt.show()
    plt.clf()

def marsgaliaBray(numTerms):
    mu = 0
    var = 1
    start = time.time()
    X,iterations = generateDistribution(numTerms)
    end = time.time()
    
    print("Number of iterations = %s"%(numTerms))
    print("Time elapsed =",np.round(end-start,5), "seconds")
    rejectionRatio = (sum(iterations) - len(X)/2)/sum(iterations)
    print("Rejection Ratio = " + str(rejectionRatio))
    print("Expected Rejection Ration = %s"%(1-np.pi/4))
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
    marsgaliaBray(100)
    marsgaliaBray(10000)

if __name__ == "__main__":
    main()