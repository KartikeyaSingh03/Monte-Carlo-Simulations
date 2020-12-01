import matplotlib.pyplot as plt

def linearCongruenceGenerator(a,b,m,x0,numTerms):
    xi = x0
    u = []
    for i in range(numTerms):
        u.append(xi/m)
        xi = (a*xi+b)%m
    return u

def phi(k,b):
    y = 0 
    temp = k
    bj = 1 
    while temp > 0:
        aj = temp%b
        bj1 = bj*b
        y += aj/bj1
        bj = bj1
        temp //= b
    return y

def generateSequence(b,n):
    x = []
    for i in range(n):
        xi = phi(i,b)
        x.append(xi)
    return x

def plotScatter(x):
    xi1 = []
    xi = []
    for i in range(1,len(x)):
        xi1.append(x[i-1])
        xi.append(x[i])
    
    plt.scatter(xi1,xi,s=0.5)
    plt.xlabel('x[i-1]')
    plt.ylabel('x[i]')
    plt.title('x[i-1] vs x[i] for n = %d terms'%len(x))
    plt.show()
    plt.clf()

def plotDistribution(x,y):
    fig, ax = plt.subplots(1,2)
   
    ax[0].hist(x,bins = 20,range = [0,1],edgecolor='black')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('Frequency')
    ax[0].set_title('Van der Corput Distribution for n = %d terms'%len(x))

    ax[1].hist(y,bins = 20,range = [0,1],edgecolor='black')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('Frequency')
    ax[1].set_title('LCG Distribution for n = %d terms'%len(x))
    
    plt.show()
    plt.clf()

def Halton(n):
    phi2 = generateSequence(2,n)
    phi3 = generateSequence(3,n)

    plt.scatter(phi2, phi3, s = 0.5)
    plt.xlabel('Phi2(i)')
    plt.ylabel('Phi3(i)')
    plt.title('Phi2 vs Phi3 for n = %d terms'%n)
    plt.show()
    plt.clf()

def main():
    x1 = generateSequence(2,25)
    print(x1)

    x2 = generateSequence(2,1000)
    plotScatter(x2)

    x3 = generateSequence(2,100)
    y3 = linearCongruenceGenerator(1229,9,2048,417,100)
    plotDistribution(x3,y3)

    x4 = generateSequence(2,100000)
    y4 = linearCongruenceGenerator(12205,9,65536,5357,100000)
    plotDistribution(x4,y4)

    Halton(100)
    Halton(100000)
    
if __name__ == '__main__':
    main()