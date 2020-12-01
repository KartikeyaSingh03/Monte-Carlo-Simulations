import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal

# Univariate Normal Distribution 
def N(x,mu,var):
    return (1/(np.sqrt(2*var*np.pi)))*(np.exp((-0.5)*(x-mu)*(x-mu)/var))

def plotFunction(a,mu,sigma):
    # Range for the X-Y plane 
    # nearly all the values would lie in this range
    xlow = mu[0] - 4*(np.sqrt(sigma[0][0]))
    xhigh = mu[0] + 4*(np.sqrt(sigma[0][0]))
    ylow = mu[1] - 4*(np.sqrt(sigma[1][1]))
    yhigh = mu[1] + 4*(np.sqrt(sigma[1][1]))
    

    x = np.linspace(xlow,xhigh,5000,endpoint=True)
    y = np.linspace(ylow,yhigh,5000,endpoint=True)
    X,Y = np.meshgrid(x,y)
    
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y
    
    # 2- Dimennsional distribution
    Z = (multivariate_normal(mu,sigma)).pdf(pos)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z,cmap='viridis',linewidth=0)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('N(mu,sigma)')
    plt.title('Actual Distribution for a = %s'%(a))
    plt.show()
    fig.clf()
    plt.clf()

   

# Used to generate N(0,1) distribution.
def generateNormal(numTerms):
    return np.random.normal(0,1,numTerms)

# Returns the cholesky factorization of the variance-covariance matrix
def cholesky(sigma):
    sigma1 = np.sqrt(sigma[0][0])
    sigma2 = np.sqrt(sigma[1][1])
    rho = (sigma[0][1])/(sigma1*sigma2)
    A = np.array([[sigma1,0],[rho*sigma2,sigma2*(np.sqrt(1-rho**2))]])
    return A

def findBucket(x,low,high,num_buckets):
    bucket_size = (high-low)/num_buckets
    return int(np.floor((x-low)/bucket_size))

# plot simulated two-dimensional distribution and marginal one-dimensional distributions
def plotDistribution(a,X,mu,sigma):
    xlow = mu[0] - 4*(np.sqrt(sigma[0][0]))
    xhigh = mu[0] + 4*(np.sqrt(sigma[0][0]))
    ylow = mu[1] - 4*(np.sqrt(sigma[1][1]))
    yhigh = mu[1] + 4*(np.sqrt(sigma[1][1]))
    x = np.linspace(xlow,xhigh,40,endpoint=True)
    y = np.linspace(ylow,yhigh,40,endpoint=True)
    X1,X2 = np.meshgrid(x,y)
    pos = np.empty(X1.shape + (2,))
    pos[:, :, 0] = X1
    pos[:, :, 1] = X2

    num_bucketsX = 40
    bucket_sizeX = (xhigh-xlow)/num_bucketsX

    bucketsX = []
    curr = xlow
    for i in range(num_bucketsX):
        bucketsX.append(curr)
        curr += bucket_sizeX

    num_bucketsY = 40
    bucket_sizeY = (yhigh-ylow)/num_bucketsY

    bucketsY = []
    curr = ylow
    for i in range(num_bucketsY):
        bucketsY.append(curr)
        curr += bucket_sizeY

    freq = np.zeros([num_bucketsX,num_bucketsY],dtype= int)
    freqX = [0]*num_bucketsX
    freqY = [0]*num_bucketsY
    
    for b in X:
        xBucket = findBucket(b[0],xlow,xhigh,num_bucketsX)
        yBucket = findBucket(b[1],ylow,yhigh,num_bucketsY)
        if b[0] >= xlow and b[0] < xhigh and b[1] >= ylow and b[1] < yhigh:    
            freq[xBucket][yBucket] += 1
        if b[0] >= xlow and b[0] < xhigh:
            freqX[xBucket] += 1
        if b[1] >= ylow and b[1] < yhigh:
            freqY[yBucket] += 1

    areaX = bucket_sizeX*len(X)
    
    for i in range(len(freq)):
        freqX[i] /= areaX

    areaY = bucket_sizeY*len(X)
    
    for i in range(len(freq)):
        freqY[i] /= areaY
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X1, X2, freq,cmap='viridis',linewidth=0)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Frequency')
    plt.title('Simulated Distribution for a = %s'%(a))
    plt.show()
    fig.clf()
    plt.clf()

    # Simulated Marginal Distribution (X1)
    plt.plot(bucketsX,freqX,color = 'b',label = 'Simulated')

    # Actual Marginal distribution (X1)
    plt.plot(x,N(x,mu[0],sigma[0][0]),color = 'r',label = 'Actual')
    plt.xlabel('x')
    plt.ylabel('N(%s,%s)'%(mu[0],sigma[0][0]))
    plt.title('Marginal Distribution for a = %s and mu = %s'%(a,mu[0]))
    plt.legend(loc = 'upper right')
    plt.show()
    plt.clf()

    # Simulated Marginal Distribution (X2)
    plt.plot(bucketsY,freqY,color = 'b',label = 'Simulated')  
    
    # Actual Marginal distribution (X2)
    plt.plot(y,N(y,mu[1],sigma[1][1]),color = 'r',label = 'Actual')
    plt.xlabel('x')
    plt.ylabel('N(%s,%s)'%(mu[1],sigma[1][1]))
    plt.title('Marginal Distribution for a = %s and mu = %s'%(a,mu[1]))
    plt.legend(loc = 'upper right')
    plt.show()
    plt.clf()
        
def generateDistribution(mu,sigma,n,numTerms):
    Z = []
    for i in range(n):
        Zi = generateNormal(numTerms)
        Z.append(Zi)
    Z = np.array(Z)
    A = cholesky(sigma)
    MU = np.array([[mu[0]]*numTerms,[mu[1]]*numTerms])
    X = MU + A.dot(Z)
    X1 = np.transpose(X)
    return X1

def plot(a):
    mu = np.array([5,8])
    sigma = np.array([[1,2*a],[2*a,4]])
    
    X = generateDistribution(mu,sigma,2,1000)
    plotDistribution(a,X,mu,sigma)

    # If the variance covariance matrix is singular,
    # the Value of a is modified slightly
    # The modification is done 
    if(np.linalg.det(sigma) == 0):
        a -= 0.001
    sigma = np.array([[1,2*a],[2*a,4]])
    plotFunction(a,mu,sigma)
    

def main():
    a = 0.5
    plot(a)

    a = -0.5
    plot(a)

    a = 1
    plot(a)

if __name__ == "__main__":
    main()    