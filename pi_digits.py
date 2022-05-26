from math import sqrt
from random import *
import matplotlib.pyplot as plt



def leibniz_method():
    # initialize the denominator
    d = 1
    # initialize sum
    s = 0
    l = input("How many numbers? ")
    if l == "":
        return
    else:
        l = int(l)
    # user input (number of digits)

    for i in range(l):

        if i % 2 == 0:
            s += 4 / d
        else:
            s -= 4 / d
        d += 2
    print(s)


def square_method():
    #plot initialize 
    x = []
    y = []
    plt.axes([0,2,0,2])
    
    l = 1000
    inside = 0
    all_p = 0

    for i in range(l):
        xes = random()
        x.append(xes)
        ys = random()
        y.append(ys)
        
        if sqrt(xes * xes + ys * ys) < 1:
            inside += 1
        
        plt.scatter(x, y , s = 1)   
        plt.pause(0.01)     # pause for 0.05 seconds
        
        all_p += 1
        
        
    pi = 4 * inside / all_p
    plt.show()
    print(pi)


if __name__ == "__main__":
    leibniz_method()
    #square_method()
