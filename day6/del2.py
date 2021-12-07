#! /usr/bin/env python3

from collections import defaultdict
import numpy as np

def readFile():
    fish_data = defaultdict(int)

    with open("input", "r") as f:
        input = f.read() # Read all file in case values are not on a single line
        fish_raw_data = [ int(x) for x in input.split(",") ] # Convert strings to ints
        for i in fish_raw_data:
            fish_data[i] += 1
    return fish_data

def main():
    d = readFile()
    print(d)

    i = 1
    while(i < 257):
        tmp_fish_data = defaultdict(int)
        for fish_state, count in d.items():
            if fish_state == 0:
                tmp_fish_data[8] += count
                tmp_fish_data[6] += count
            else:
                tmp_fish_data[fish_state -1] += count
        d = tmp_fish_data 
        # print("After ", i, " days:", school)
        i += 1

    print(sum(d.values()))

# Control execution of code
if __name__ == "__main__":
    main()