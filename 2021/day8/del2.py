#! /usr/bin/env python3

import numpy as np
import re

def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
        if sorted(val) == sorted(value):
            return key
 
    return "key doesn't exist"

def readFile():
    lines = np.loadtxt("input", delimiter=' | ', unpack=False, dtype=str)
    return lines

def main():

    sevenSegment = readFile()
    results = []
    sum = 0
    for a in sevenSegment:
        print(a)

        sparr = np.char.split(a)
        print(sparr)
        output = ""

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
        test = 0

        while test < 10:
            for number in sparr[0]:
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
                    elif decode["6"] != "":
                        c = 0
                        for i in number:
                            if re.search(i,decode["6"]):
                                c=c+1
                        if c == 5:
                            decode["5"] = number
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
                    else:
                        c = 0
                        for i in number:
                            if re.search(i,decode["7"]):
                                c=c+1
                        if c == 3:
                            decode["0"] = number
                        else:
                            decode["6"] = number
                elif len(number) == 7:
                    decode["8"] = number
            test += 1
        
        print(decode)
        for number in sparr[1]:
            print(number)
            output = output + get_key(number, decode)
        results.append(output)
    print(results)
    for number in results:
        sum += int(number)
    print(sum)
# Control execution of code
if __name__ == "__main__":
    main()