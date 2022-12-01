#! /usr/bin/env python3

import numpy as np

class Board:
    def __init__(self):
        self.bingo = False
        self.index = 0

def checkRowBingo(array2d, index):
    b = Board()
    for i in range(array2d.shape[0]):
        if np.all(array2d[i]==1):
            b.bingo = True
            b.index = index
            return b
    return b

def checkColumnBingo(array2d, index):
    b = Board()
    trans_arr = array2d.T
    for i in range(trans_arr.shape[0]):
        if np.all(trans_arr[i] == 1):
            b.bingo = True
            b.index = index
            return b
    return b

def create3dArray(filename, empty_line_count):
    with open(filename) as my_file:
        lines = (line for line in my_file if not ',' in line)
        FH = np.loadtxt(lines, dtype ='int', skiprows=1)
        arr_3d = np.reshape(FH, (empty_line_count, 5, 5))

    return arr_3d

def main():
    empty_line_count = 0 

    with open('input','r') as fh:
        for line in fh:
            if line.split() == []:
                    empty_line_count += 1

    print('Empty Line Count : ' , empty_line_count)

    with open('input') as my_file:
        first_line = my_file.readline()

    values = [int(i) for i in first_line.split(',')]
    arr_data = np.array(values)

    arr_3d = create3dArray('input', empty_line_count)
    a_3d_array = np.zeros((empty_line_count, 5, 5), dtype=int)

    print (arr_3d)

    brett = []

    for number in arr_data:
        for i in range(empty_line_count):
            for j in range(5):
                for k in range(5):
                    if arr_3d[i][j][k] == number:
                        a_3d_array[i][j][k] = 1
                        cBoard = checkColumnBingo(a_3d_array[i], i)
                        rBoard = checkRowBingo(a_3d_array[i], i)
                        if cBoard.bingo:
                            if not any(x.index == cBoard.index for x in brett):                            
                                print(cBoard.index)
                                sum = 0
                                for l in range(5):
                                    for m in range(5):
                                        if a_3d_array[cBoard.index][l][m] == 0:
                                            sum += arr_3d[cBoard.index][l][m]
                                brett.append(cBoard)
                                print(number)
                                print(sum)
                                print(sum*number)
                                print(a_3d_array[cBoard.index])
                                print(arr_3d[cBoard.index])
                        elif rBoard.bingo:
                            if not any(x.index == rBoard.index for x in brett):
                                sum = 0
                                for l in range(5):
                                    for m in range(5):
                                        if a_3d_array[rBoard.index][l][m] == 0:
                                            sum += arr_3d[rBoard.index][l][m]
                                brett.append(rBoard)
                                print(sum)
                                print(sum*number)
                                print(a_3d_array[rBoard.index])
                                print(arr_3d[rBoard.index])
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

    for a in brett:
        print(a.index)

# Control execution of code
if __name__ == "__main__":
    main()