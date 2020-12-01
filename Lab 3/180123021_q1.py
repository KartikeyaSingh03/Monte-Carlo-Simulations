import matplotlib.pyplot as plt
import numpy as np

def findIndex(u,q):
    for i in range(1,5000):
        if u <= q[i]:
            return i

def main():
    c = []
    for i in range(5000):
        c.append(2*i+1)

    p = 1/5000

    q = [0]*5000
    q[0] = p
    for i in range(5000):
        q[i] = q[i-1] + p

    x = []
    numTerms = 100000
    for i in range(numTerms):
        # To generate a U[0,1] distribution
        u = np.random.rand()

        # find the number which has to be incremented
        k = findIndex(u,q)
        x.append(c[k])
    
    with open('q1_data.txt', 'w') as f:
        for num in x:
            f.write("%s\n" % num)
    
if __name__ == "__main__":
    main()    