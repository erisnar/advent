#! /usr/bin/env python3

import numpy as np
import pandas as pd
import sys
sys.setrecursionlimit(10000)

def neighbors(df, flashed, i, j, flash):

    if i < df.shape[0] and j < df.shape[1] and i >= 0 and j >= 0:

        if flashed.iloc[i][j] == 1:
            return df, flashed, flash

        if df.iloc[i][j] == 9:
            flashed.iloc[i][j] = 1
            flash +=1
            df.iloc[i][j] = 0
            if i+1 < df.shape[0] and j+1 < df.shape[1]:
                df, flashed, flash = neighbors(df, flashed, i+1, j+1, flash)
            if j+1 < df.shape[1]:
                df, flashed, flash = neighbors(df, flashed, i, j+1, flash)
            if i+1 < df.shape[0]:
                df, flashed, flash = neighbors(df, flashed, i+1, j, flash)
            if i-1 >= 0 and j-1 >= 0:
                df, flashed, flash = neighbors(df, flashed, i-1, j-1, flash)
            if j-1 >= 0:
                df, flashed, flash = neighbors(df, flashed, i, j-1, flash)
            if i-1 >= 0:
                df, flashed, flash = neighbors(df, flashed, i-1, j, flash)
            if i-1 >= 0 and j+1 < df.shape[1]:
                df, flashed, flash = neighbors(df, flashed, i-1, j+1, flash)
            if j-1 >= 0 and i+1 < df.shape[0]:
                df, flashed, flash = neighbors(df, flashed, i+1, j-1, flash)

        if flashed.iloc[i][j] == 0:
            df.iloc[i][j] += 1
            return df, flashed, flash

    return df, flashed, flash

def split(word):
    return [char for char in word]

def readFile():
    lines = np.loadtxt("input", dtype=str)
    return lines

def main():
    energyLevel = readFile()
    print(energyLevel)
    energyLevel = np.array([split(x) for x in energyLevel.ravel()])
    df = pd.DataFrame(energyLevel)
    flashed = pd.DataFrame(np.zeros((df.shape[0], df.shape[1])))
    df = df.astype(int)
    flash = 0
    step = 0
    steps = 100
    while step < steps:
        flashed = pd.DataFrame(np.zeros((df.shape[0], df.shape[1])))
        for i, row in df.iterrows():
            for j, element in enumerate(row):
                df, flashed, flash = neighbors(df, flashed, i, j, flash)
                
        print(step)
        step += 1
    print(df)
    print(flash)

    
    
# Control execution of code
if __name__ == "__main__":
    main()

