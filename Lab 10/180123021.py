import numpy as np

def uniform(N):
    U = []
    for i in range(N):
        u = np.random.rand()
        U.append(u)
    return U

def expectedVal(U):
    Y = []
    for ui in U:
        Yi = np.exp(np.sqrt(ui))
        Y.append(Yi)
    return Y

def expectedValArithmeticVariates(U):
    Y = []
    for ui in U:
        Yi = (np.exp(np.sqrt(ui)) + np.exp(np.sqrt(1-ui)))/2
        Y.append(Yi)
    return Y

def confidenceInterval(Y):
    M = len(Y)
    mu = np.mean(Y)
    sigma_square = np.var(Y)
    sigma = np.sqrt(sigma_square)

    low = mu - (1.96*sigma/np.sqrt(M))
    high = mu + (1.96*sigma/np.sqrt(M))

    return low, high

def calculate(M):
    U = uniform(M)
    Y = expectedVal(U)
    Y_hat = expectedValArithmeticVariates(U)

    Im = np.mean(Y)
    Im_hat = np.mean(Y_hat)

    Im_low, Im_high = confidenceInterval(Y)
    Im_hat_low, Im_hat_high = confidenceInterval(Y_hat)

    Im_len = Im_high - Im_low
    Im_hat_len = Im_hat_high - Im_hat_low

    ratio = Im_len/Im_hat_len

    print("****** Results for M = %d ******\n"%M)

    print("Im = %.6f"%Im)
    print("Im_hat = %.6f"%Im_hat)

    print("95%% Confidence interval for Im = [%.6f, %.6f]"%(Im_low, Im_high))
    print("95%% Confidence interval for Im_hat = [%.6f, %.6f]"%(Im_hat_low, Im_hat_high))

    print("Length of Confidence interval for Im = %.6f"%Im_len)
    print("Length of Confidence interval for Im_hat = %.6f"%Im_hat_len)

    print("Ratio of Lengths (Im_len/Im_hat_len) = %.6f"%ratio)

    print("\n\n")

def main():
    M = [100,1000,10000,100000]
    for m in M:
        calculate(m)
        
if __name__ == "__main__":
    main()