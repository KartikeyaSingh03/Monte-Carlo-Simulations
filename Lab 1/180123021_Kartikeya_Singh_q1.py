def linearCongruenceGenerator(a,b,m,x0,numTerms,file):
    xi = x0
    for i in range(numTerms):
        file.write(str(xi)+", ")
        xi = (a*xi+b)%m
    file.write("\n")

def main():
    # Part 1 -> a = 6, b = 0, m = 11
    file = open("180123021_q1_part1_output.csv","a")
    for i in range(100):
        file.write("x" + str(i) + ", ")
    file.write("\n")
    for x0 in range(0,11):
        linearCongruenceGenerator(6,0,11,x0,100,file)
    file.close()

    # Part 2 -> a = 3,b = 0,m = 11
    file = open("180123021_q1_part2_output.csv","a")
    for i in range(100):
        file.write("x" + str(i) + ", ")
    file.write("\n")
    for x0 in range(0,11):
        linearCongruenceGenerator(3,0,11,x0,100,file)
    file.close()

if __name__ == '__main__':
    main()

