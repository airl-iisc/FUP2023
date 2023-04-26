#!usr/bin/env python3
import sys
filename = sys.argv[1]
score = 0 

# x position :0.4740000069141388
# Y position :0.15249998927116393


with open(filename) as f:
    tokens = f.readlines()

    x1e = abs(float(tokens[1][1:])-0.16)
    y1e = abs(float(tokens[2][1:])-0.475)

    x2e = abs(float(tokens[5][1:])-0.105)
    y2e = abs(float(tokens[6][1:])-0.45)

    x3e = abs(float(tokens[9][1:])-0.335)
    y3e = abs(float(tokens[10][1:])-0.63)
    
    print("Errors in each point")
    print(x1e,y1e)
    print(x2e,y2e)
    print(x3e,y3e)

    print("Total Error")
    score =  ((x1e+x2e+x3e+y1e+y2e+y3e))

    print(round(score,5))
