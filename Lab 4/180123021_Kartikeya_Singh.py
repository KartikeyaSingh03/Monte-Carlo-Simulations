import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

def B(a1,a2):
    return gamma(a1)*gamma(a2)/gamma(a1+a2)

def f(x,a1,a2):
    return (1/B(a1,a2))*(np.power(x,a1-1))*(np.power(1-x,a2-1))

def g(x):
    return 1

def xStar(a1,a2):
    return (a1-1)/(a1+a2-2)

def generateTerm(c,a1,a2):
    X = -1
    while True:
        X = np.random.rand()
        U = np.random.rand()
        if U <= f(X,a1,a2)/(c*g(X)):
            break    
    return X

def generateDistribution(c,a1,a2,numTerms):
    X = []
    for i in range(numTerms):
        X.append(generateTerm(c,a1,a2))
    return X

def findBucket(x):
    return int(np.floor(x*100))

def plot(X,numTerms,a1,a2):

    # bucket[0] = [0,0.01)
    # bucket[1] = [0.01,0.02) and so on
    term = 0
    buckets = []
    for i in range(100):
        term += 0.01
        buckets.append(term)

    # No of elements in each bucket
    frequency = [0]*100

    for x in X:
        frequency[findBucket(x)] += 1
   
    for i in range(100):
        frequency[i] *= 100/numTerms
    
    # Plotting the Frequencies
    plt.bar(buckets,frequency,width=0.01,edgecolor = 'black',label = 'Generated Distribution')
    
    # Plotting the actual Distribution Function
    x = np.linspace(0,1,5000,endpoint=True)
    plt.plot(x,f(x,a1,a2),color = 'r',label = 'Actual Distribution')
    
    plt.xlabel('Intervals')
    plt.ylabel('Scaled Frequencies')
    plt.title('Beta Distribution for a1 = %s, a2 = %s'%(a1,a2))
    plt.legend(loc = 'upper right')
    plt.show()
    plt.clf()



def simulate(a1,a2):

    # The value of x for which f(x) is maximum.
    x_star = xStar(a1,a2)
    print("x_star = " + str(x_star))
    # The maximum value of f(x)
    c = f(x_star,a1,a2)
    print("c = " + str(c))
    # Generating the distribution using the Acceptance-Rejection method
    numTerms = 100000
    X = generateDistribution(c,a1,a2,numTerms)    
    
    plot(X,numTerms,a1,a2)


def main():
    simulate(1,4)
    simulate(4,1)
    simulate(3,3)
    simulate(2,4)
    simulate(4,2)

if __name__ == "__main__":
    main()