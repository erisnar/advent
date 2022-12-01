#! /usr/bin/env python3

import numpy as np

def readFile():
    lines = np.loadtxt("input", delimiter=",", unpack=False, dtype=int)
    return lines

def main():
    school = readFile()
    print(school)

    i = 1
    while(i < 81):
        for j in range(len(school)):
            if school[j] == 0:
                school[j] = 6
                school = np.append(school, 8)
            else:
                school[j] = school[j] - 1
        print("After ", i, " days:", school)
        i += 1

    print(len(school))

# Control execution of code
if __name__ == "__main__":
    main()