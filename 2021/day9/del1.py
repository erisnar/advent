#! /usr/bin/env python3

import numpy as np
import pandas as pd

class Position:
    def __init__(self):
        self.number = 99
        self.up = 99
        self.down = 99
        self.left = 99
        self.right = 99

def split(word):
    return [char for char in word]

def readFile():
    lines = np.loadtxt("input", unpack=False, dtype=str)
    return lines

def main():
    heightmap = readFile()
    print(heightmap)
    positions = []
    lowPoints = []
    sum = []
    heightmap = np.array([split(x) for x in heightmap.ravel()])
    df = pd.DataFrame(heightmap)
    print(df)
    for i, row in df.iterrows():
        for j, element in enumerate(row):
            p = Position()
            p.number = int(df.iloc[i][j])
            if i-1 >= 0 and i-1 < df.shape[0]:
                p.up = int(df.iloc[i-1][j])
            if i+1 >= 0 and i+1 < df.shape[0]:
                p.down = int(df.iloc[i+1][j])
            if j+1 >= 0 and j+1 < df.shape[1]:
                p.right = int(df.iloc[i][j+1])
            if j-1 >= 0 and j-1 < df.shape[1]:
                p.left = int(df.iloc[i][j-1])
            positions.append(p)
    
    risk = 0
    for p in positions:
        if p.number < p.up and p.number < p.down and p.number < p.left and p.number < p.right:
            print(p.number)
            risk = risk + p.number + 1
    print(risk)
    
# Control execution of code
if __name__ == "__main__":
    main()