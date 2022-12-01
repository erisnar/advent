#! /usr/bin/env python3

import numpy as np

def readFile():
    lines = np.loadtxt("input", delimiter=",", unpack=False, dtype=int)
    return lines

def triangular_number(n):
    return n * (n + 1) // 2

def main():
    crabs = readFile()
    print(crabs)
    sum = []
    for i in range(len(crabs)):
        pos = 0
        for crab in crabs:
            fuel = abs(i-crab)
            fuel = triangular_number(fuel)
            pos = pos + fuel
        sum.append(pos)
    
    print(sum)
    min_value = min(sum)
    print("Smallest element is:", min_value)
    min_index = sum.index(min_value)
    print("Smallest element is on index:", min_index)

    

# Control execution of code
if __name__ == "__main__":
    main()