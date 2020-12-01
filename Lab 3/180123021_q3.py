import matplotlib.pyplot as plt
import numpy as np

def f(probs,x):
    return probs[x-1]

def g(x):
    return 1/10

def generateDiscreteRandom(q):
    u = np.random.rand()
    for i in range(1,10):
        if u <= q[i]:
            return i+1

def generateTerm(c,probs,q):
    iterations = 0
    X = -1
    while True:
        iterations += 1
        X = generateDiscreteRandom(q)
        U = np.random.rand()
        if U <= f(probs,X)/(c*g(X)):
            break    
    return X,iterations

def generateDistribution(c,numTerms,probs,q):
    X = []
    iterations = []
    for i in range(numTerms):
        x,it = generateTerm(c,probs,q)
        X.append(x)
        iterations.append(it)
    return X,iterations

def plot(c,q1,numTerms,probs,q):
    x_vals = []
    for i in range(10):
        x_vals.append(i+1)
    
    plt.plot(x_vals,q1,color = 'r',label = 'Actual Distribution')
    
    X, iterations = generateDistribution(c,numTerms,probs,q)
    
    frequency = [0]*10

    for x in X:
        frequency[x-1] += 1
    
    cumulative_frequency = [0]*10
    cumulative_frequency[0] = frequency[0]
    for i in range(1,10):
        cumulative_frequency[i] = cumulative_frequency[i-1] + frequency[i]
    
    for i in range(10):
        cumulative_frequency[i] /= numTerms
    
    plt.plot(x_vals,cumulative_frequency,color = 'b',label = 'Generated Distribution (c = %s)' %(c))
    plt.xlabel('Values of X')
    plt.ylabel('Cumulative Frequency')
    plt.legend(loc = 'upper left')
    plt.show()
    plt.clf()

    meanIterations = np.mean(iterations)
    print(meanIterations)



def main():
    probs = [0.11, 0.12, 0.09, 0.08, 0.12, 0.10, 0.09, 0.09, 0.10, 0.10]
    
    # For Uniform Discrete Random Variable 
    q = []
    for i in range(10):
        q.append((i+1)/10)

    q1 = [0]*10
    q1[0] = probs[0]
    for i in range(1,len(probs)):
        q1[i] = q1[i-1] + probs[i]

    numTerms = 10000
    
    c = 8
    plot(c,q1,numTerms,probs,q)

    c = 16
    plot(c,q1,numTerms,probs,q)




if __name__ == "__main__":
    main()
