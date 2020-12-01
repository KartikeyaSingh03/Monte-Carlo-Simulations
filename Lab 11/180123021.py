def linearCongruenceGenerator(a,b,m,x0,numTerms):
    xi = x0
    u = []
    for i in range(numTerms):
        u.append(xi/m)
        xi = (a*xi+b)%m
    return u

def count(x,i,N):
    size = 1/N
    left = i*size
    right = (i+1)*size
    cnt = 0
    for a in x:
        if a >= left and a < right:
            cnt += 1
    return cnt

def calcDiscrepancy(x,N):
    discTillNow = 0
    n = len(x)
    vol = 1/N
    for i in range(N):
        disc = abs(count(x,i,N)/n - vol)
        discTillNow = max(discTillNow,disc)
    return discTillNow
    
def main():
    m = 2048
    a = 1229
    b = 9
    x0 = 417
    
    x = linearCongruenceGenerator(a,b,m,x0,m-1)
    
    N = [10,20,50,100]

    for n in N:
        d = calcDiscrepancy(x,n)
        print("Discrepancy for N = %d is %.6f"%(n,d))
    
if __name__ == '__main__':
    main()