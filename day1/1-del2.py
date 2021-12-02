#! /usr/bin/env python3
import itertools

def main():

    with open('input') as file:
        lines = file.readlines()
        lines = [int(line) for line in lines]
    
    larger = 0
    sum = 0
    prev = 0
    
    for a, b, c in zip(lines, lines[1:], lines[2:]):
        sum = a+b+c
        if ( sum > prev ):
            if ( prev != 0 ):
                larger += 1
        print(larger)
        prev = sum

# Control execution of code
if __name__ == "__main__":
    main()