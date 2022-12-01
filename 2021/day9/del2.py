#! /usr/bin/env python3

import numpy as np
import pandas as pd
import sys
sys.setrecursionlimit(10000)

def neighbors(df, basin, i, j, basinNumber):

    if i < df.shape[0] and j < df.shape[1] and i >= 0 and j >= 0:
        if int(df.iloc[i][j]) < 9:
            if int(basin.iloc[i][j]) == basinNumber:
                return basin
            basin[j][i] = basinNumber
            basin = neighbors(df, basin, i, j+1, basinNumber)
            basin = neighbors(df, basin, i+1, j, basinNumber)
            basin = neighbors(df, basin, i, j-1, basinNumber)
            basin = neighbors(df, basin, i-1, j, basinNumber)
    return basin

def split(word):
    return [char for char in word]

def readFile():
    lines = np.loadtxt("input", unpack=False, dtype=str)
    return lines

def main():
    heightmap = readFile()
    sum = []
    heightmap = np.array([split(x) for x in heightmap.ravel()])
    df = pd.DataFrame(heightmap)
    basin = pd.DataFrame(np.zeros((df.shape[0], df.shape[1])))
    basinNumber = 1

    i = 0
    j = 0
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if int(df.iloc[i][j]) < 9:
                if basinNumber == 1:
                    basin = neighbors(df, basin, i, j, basinNumber)                
                    basinNumber += 1
                elif int(basin.iloc[i][j]) == 0.0:
                    basin = neighbors(df, basin, i, j, basinNumber)
                    basinNumber += 1
            j += 1
        i += 1
    print(basin)
    max_value = 0
    for row in basin:
        if max_value < basin[row].max():
            max_value = basin[row].max()

    print(max_value)

    dicts = {}
    keys = range(int(max_value))
    for row in basin:
        print((basin[row] == 3).sum())
        
        for i in keys:
            dicts[i] = dicts.get(i, 0) + (basin[row] == i+1).sum()
    print(dicts)
    my_keys = sorted(dicts, key=dicts.get, reverse=True)[:3]
    print(my_keys)
    mult = []
    for key in my_keys:
        mult.append(dicts[key])

    result = np.prod(mult)
    print(result)


# Control execution of code
if __name__ == "__main__":
    main()