#!/bin/python3
import time

''' Lab 1 Practice '''

## Pythagorean Theorem
## sqrt(a^2 + b^2) = c
def PyCalc(a, b):
    print("Pythagorean calculator")
    
    ## solving the exponents
    a_side = a ** 2     # a^2
    b_side = b ** 2     # b^2


    #print(a_side)
    #print(b_side)

    c_side = (a_side + b_side)**(1/2)   # sqrt(a^2 + b^2)

    print(c_side)


## Slope Formula
def SlopeCalc():
    print("\nSlope calculator")

    point1_x = int(input("Point 1 x-value: "))
    point1_y = int(input("Point 1 y-value: "))


    point2_x = int(input("Point 2 x-value: "))
    point2_y = int(input("Point 2 y-value: "))


    rise = point2_y - point1_y
    run = point2_x - point1_x

    slope = rise / run
    print(slope)

PyCalc(4, 6)
SlopeCalc()
