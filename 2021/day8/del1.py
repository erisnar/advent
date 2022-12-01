#! /usr/bin/env python3

import numpy as np

def readFile():
    lines = np.loadtxt("input", delimiter=' | ', unpack=False, dtype=str)
    return lines

def main():
    sevenSegment = readFile()
    print(sevenSegment)
    appear = 0
    for row in sevenSegment:
        sparr = np.char.split(row)
        for number in sparr[1]:
            if len(number) == 2:
                appear += 1
            elif len(number) == 3:
                appear += 1
            elif len(number) == 4:
                appear += 1
            elif len(number) == 7:
                appear += 1
    print(appear)

# Control execution of code
if __name__ == "__main__":
    main()