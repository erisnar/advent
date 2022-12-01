#! /usr/bin/env python3

from collections import Counter
import collections
from operator import itemgetter

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal) 

def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s))
      
    return(res)

def mostCommon(lst):
          
    return [Counter(col).most_common(1)[0][0] for col in zip(*lst)]

def main():
    
    lst = []

    with open('input') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            num = line
            x = [int(a) for a in str(num)]
            lst.append(x)

    most = mostCommon(lst)
    binary = convert(most)
    gamma = binaryToDecimal(binary)
    least = most

    for n, i in enumerate(least):
        if i == 1:
            least[n] = 0
        elif i == 0:
            least[n] = 1

    binary = convert(most)
    epsilon = binaryToDecimal(binary)
    power = gamma*epsilon

    print(power)

# Control execution of code
if __name__ == "__main__":
    main()