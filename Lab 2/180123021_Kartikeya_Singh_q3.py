import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (2/np.pi)*(np.arcsin(np.sqrt(x)))

def X(u):
    return 0.5 - 0.5*(np.cos((np.pi)*u))

def expMean(x_vals):
    return np.mean(x_vals)

def expVariance(x_vals):
    return np.var(x_vals)

def update_freq(freq,x):
    if x < 1:
        index = int(np.floor(100*x))
        freq[index] += 1

def plotFunction():
    x = np.linspace(0,1,5000,endpoint=True)
    plt.plot(x,f(x),color = 'r')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Actual Distribution Function')
    plt.show()
    plt.clf()

def plotGraphs(n,file):

    # x_vals would be 100 intervals of size 0.01 each 
    # storing the midpoint of each interval
    intervals = []
    curr_mid = 0.005
    interval_size = 0.01
    for i in range(100):
        intervals.append(curr_mid)
        curr_mid += interval_size

    # freq would be the frequency of the values in each interval
    # initially frequencies are set to 0 
    freq = [0]*100

    # stores the values of xi
    x_vals = []

    # generating n random values between 0 and 1
    # assuming that the random number generator genrates numbers uniformly
    # as the values are generated uniformly it can be assumed that the distribution is U[0,1]
    for i in range(n):
        u = np.random.rand()
        x = X(u)
        x_vals.append(x)
        update_freq(freq,x)

    # stores the cumulative frequency
    cum_freq = [0]*100
    cum_freq[0] = freq[0]
    for i in range(1,100):
        cum_freq[i] = cum_freq[i-1] + freq[i]

    # Calculating the mean and variance
    experimental_mean = expMean(x_vals)
    experimental_variance = expVariance(x_vals)

    file.write("Data for " + str(n) + " rounds\n")
    file.write("Experimental Mean = " + str(experimental_mean) + "\n")
    file.write("Experimental Variance = " + str(experimental_variance) + "\n")

    # Display the graphs
    plt.plot(intervals,cum_freq,color = 'b',label = 'experimental')
    plt.title('Distribution Function using genrated values (n = ' + str(n) + ')')
    plt.xlabel('values of x')
    plt.ylabel('Cumulative Frequency')
    plt.legend(loc = 'lower right')
    plt.show()
    plt.clf()

def main():
    file = open("180123021_q3_data.txt","a")
    plotFunction()
    plotGraphs(1000,file)
    plotGraphs(10000,file)
    plotGraphs(100000,file)
    
if __name__ == '__main__':
    main()