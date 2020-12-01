import matplotlib.pyplot as plt

# Linear Congruence generator to generate first 17 values of the sequence
def linearCongruenceGenerator(a,b,m,x0,numTerms,u):
    xi = x0
    for i in range(numTerms):
        u.append(xi/m)
        xi = (a*xi+b)%m

def nextTerm(u):
    n = len(u)-1
    ui = u[n-17] - u[n-5]
    if ui < 0:
        ui += 1
    return ui

# used to generate a sequence of length n
def generate(u,n):
    linearCongruenceGenerator(17,1,31,1,18,u)
    while len(u) < n:
        u.append(nextTerm(u))

def plotGraphs(u):
    # stores the values of u[i-1]
    ui1 = []
    
    # stores the values of u[i]
    ui = []

    for i in range(1,len(u)):
        ui1.append(u[i-1])
        ui.append(u[i])

    plt.scatter(ui1,ui,s = 0.5)
    plt.xlabel('Value of u[i-1]')
    plt.ylabel('Value of u[i]')
    plt.title('u[i-1] vs u[i] (n = ' + str(len(u)) + ')')
    plt.show()
    plt.clf()

    ticks = []
    val = 0
    for i in range(21):
        ticks.append(val)
        val += 0.05

    num_bars = 20
    plt.xlabel('Value of ui')
    plt.ylabel('Frequency')
    plt.title('Frequency for various intervals (n = ' + str(len(u)) + ')')
    plt.tight_layout()
    plt.xticks(ticks,rotation='vertical') 
    frequencies,bins,patches = plt.hist(u,num_bars,edgecolor = 'black')
    plt.show()
    plt.clf()



def main():
    u1 = []
    u2 = []
    u3 = []
    generate(u1,1000)
    generate(u2,10000)
    generate(u3,100000)
    plotGraphs(u1)
    plotGraphs(u2)
    plotGraphs(u3)

if __name__ == '__main__':
    main()