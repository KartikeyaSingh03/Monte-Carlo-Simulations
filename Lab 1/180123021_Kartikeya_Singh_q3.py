import matplotlib.pyplot as plt
import random

def generatePlot(a,b,m,x0):    
    # values of u
    u = []
    xi = x0
    for i in range(10000):
        u.append(xi/m)    
        xi = (a*xi+b)%m
    
    # stores the values of u[i-1]
    ui1 = []
    
    # stores the values of u[i]
    ui = []

    for i in range(1,len(u)):
        ui1.append(u[i-1])
        ui.append(u[i])

    plt.scatter(ui1,ui,s = 0.05)
    plt.show()

def main():
    a = 1229
    b = 1
    m = 2048
    x0 = random.randint(0,m)
    generatePlot(a,b,m,x0)

if __name__ == '__main__':
    main()
        



    