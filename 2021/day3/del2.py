#! /usr/bin/env python3

from collections import Counter
import collections
from operator import itemgetter
import numpy

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

def main():
    
    lst = []

    with open('input') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            num = line
            x = [int(a) for a in str(num)]
            lst.append(x)

    arr1 = numpy.array(lst)
    arr2 = arr1

    # lol så skittent
    for i in range(12):
        extractedData = arr1[:,i]
        counts = numpy.bincount(extractedData)
        countone = numpy.count_nonzero(extractedData == 0)
        countzero = numpy.count_nonzero(extractedData == 1)
        if countone == countzero:
            number = 1
        else:
            number = numpy.argmax(counts)
        arr1 = arr1[arr1[:,i] == number]
        num_rows, num_cols = arr2.shape
        if num_rows == 1:
            break

    for list in arr1:
        binary = convert(list)
        oxygen = binaryToDecimal(binary)
        print(oxygen)

    # burde fjerne repitativ kode
    for i in range(12):
        extractedData = arr2[:,i]
        counts = numpy.bincount(extractedData)
        countone = numpy.count_nonzero(extractedData == 0)
        countzero = numpy.count_nonzero(extractedData == 1)
        if countone == countzero:
            number = 0
        else:
            number = numpy.argmin(counts)
        arr2 = arr2[arr2[:,i] == number]
        num_rows, num_cols = arr2.shape
        if num_rows == 1:
            break

    for list in arr2:
        binary = convert(list)
        co2 = binaryToDecimal(binary)
        print(co2)

    print(oxygen*co2)

# Control execution of code
if __name__ == "__main__":
    main()


#3570354