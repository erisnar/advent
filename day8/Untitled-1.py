#! /usr/bin/env python3

import numpy as np
import re

class sevenSegment:
    def __init__(self):
        self.a = 0
        self.b = 99
        self.c = 99
        self.d = 99
        self.e = 99
        self.f = 99
        self.g = 99

def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def readFile():
    lines = np.loadtxt("input3", delimiter=' | ', unpack=False, dtype=str)
    return lines

def main():

    sevenSegment = readFile()
    results = []
    rad = ""
    for row in sevenSegment:
        decode =	{
            "0": "",
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": "",
            "9": ""
        }

        rad = rad + " " + row
    print(rad)

    x = rad.split()

    sparr = np.char.split(sevenSegment)
    print(sparr)

    for number in x:
        print(number)
        if len(number) == 2:
            decode["1"] = number
        elif len(number) == 3:
            decode["7"] = number
        elif len(number) == 4:
            decode["4"] = number
        # 2, 3, 5
        elif len(number) == 5:
            c = 0
            for i in number:
                if re.search(i,decode["1"]):
                    c=c+1
            if c == 2:
                decode["3"] = number
                break
            if decode["6"] != "":
                c = 0
                for i in number:
                    if re.search(i,decode["6"]):
                        c=c+1
                if c == 5:
                    decode["5"] = number
                    break
                else:
                    decode["2"] = number
        # 0, 9, 6
        elif len(number) == 6:
            c = 0
            for i in number:
                if re.search(i,decode["4"]):
                    c=c+1
            if c == 4:
                decode["9"] = number
                break
            c = 0
            for i in number:
                if re.search(i,decode["7"]):
                    c=c+1
            if c == 3:
                decode["0"] = number
                break
            decode["6"] = number
        elif len(number) == 7:
            decode["8"] = number
    for number in sparr[1]:
        output = output + get_key(number, decode)
    results.append(output)
    print(results)

# Control execution of code
if __name__ == "__main__":
    main()