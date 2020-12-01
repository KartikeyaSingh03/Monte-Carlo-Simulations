import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 20*x*(1-x)*(1-x)*(1-x)

# Cumulative Distribution Function
def F(x):
    return -4*(x**5) + 15*(x**4) - 20*(x**3) + 10*(x**2)

def g(x):
    return 1

def plotFunction():
    x = np.linspace(0,1,5000,endpoint=True)
    plt.plot(x,F(x),color = 'r')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Distribution Functions')
    plt.show()
    plt.clf()    

def plotDistribution(buckets,cumulative_frequency,c):
    plt.scatter(buckets,cumulative_frequency,color = 'b',s=0.5)
    plt.xlabel('Intervals')
    plt.ylabel('Cumulative Frequency')
    plt.title('Generated Distribution (c = ' + str(c) + ')')
    plt.show()
    plt.clf()

def generateTerm(c):
    iterations = 0
    X = -1
    while True:
        iterations += 1
        X = np.random.rand()
        U = np.random.rand()
        if U <= f(X)/(c*g(X)):
            break    
    return X,iterations

def generateDistribution(c,numTerms):
    X = []
    iterations = []
    for i in range(numTerms):
        x,it = generateTerm(c)
        X.append(x)
        iterations.append(it)
    return X,iterations

def findBucket(x):
    return int(np.floor(x*100))

def plot(c):
    numTerms = 100000
    X,iterations = generateDistribution(c,numTerms)
    
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
    
    cumulative_frequency = [0]*100
    cumulative_frequency[0] = frequency[0]
    for i in range(1,100):
        cumulative_frequency[i] = cumulative_frequency[i-1] + frequency[i]
    
    plotDistribution(buckets,cumulative_frequency,c)
    meanIterations = np.mean(iterations)
    print(meanIterations)

def main():
    plotFunction()

    c = 2.109375
    plot(c)

    c = 2.5
    plot(c)

    c = 3
    plot(c)

if __name__ == "__main__":
    main()