import matplotlib.pyplot as plt
import random

# Function to generate the plot
def generatePlot(a,b,m,x0,file,image_name):
    
    # ticks on  the x-axis (0, 0.05, 0.10, .. , 1.00)
    ticks = []
    val = 0
    for i in range(21):
        ticks.append(val)
        val += 0.05

    # values of u
    u = []
    xi = x0
    for i in range(100000):
        u.append(xi/m)    
        xi = (a*xi+b)%m
        
    vals = "a = " + str(a) + ", x0 = " + str(x0)

    num_bars = 20
    plt.xlabel('Value of ui')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.xticks(ticks,rotation='vertical') 
    frequencies,bins,patches = plt.hist(u,num_bars,edgecolor = 'black',label=vals)
    plt.legend(loc='upper right')
    plt.savefig(image_name)
    plt.clf()
    
    file.write(vals)
    file.write("\n")
    file.write("Range, Frequency, ")
    file.write("\n")
    low = 0
    high = 0.05
    for i in range(20):
        file.write(str(round(low,2)) + " - " + str(round(high,2)) + ", ")
        file.write(str(frequencies[i]) + ", ")
        file.write("\n")
        low += 0.05
        high += 0.05


def main():
    m = 244944
    b = 3436
    file = open("180123021_q2_output.csv","a")
    img_no = 1

    # generates 5 random (and distinct) values of x0 such that 0 <= x < m (assuming m >= 5)
    nums = random.sample(range(m),5)

    # Part 1 ->  m = 244944, a = 1597, b = 3436
    a = 1597
    for x0 in nums:
        image_name = "180123021_q2_fig"+str(img_no)+".png"
        img_no += 1 
        generatePlot(a,b,m,x0,file,image_name)
        file.write("\n")

    # Part 2 -> m = 244944, a = 51749, b = 3436
    a = 51749
    for x0 in nums: 
        image_name = "180123021_q2_fig"+str(img_no)+".png"
        img_no += 1 
        generatePlot(a,b,m,x0,file,image_name)
        file.write("\n")

if __name__ == '__main__':
    main()
    