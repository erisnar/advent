#! /usr/bin/env python3

import numpy as np

class Board:
    def __init__(self):
        self.bingo = False
        self.index = 0

def checkRowBingo(array3d):
    b = Board()
    count = 0
    for array in array3d:
        for i in range(array.shape[0]):
            if np.all(array[i]==1):
                print('Bingo på rad: ', i)
                b.bingo = True
                b.index = count
                return b
        count += 1
    return b

def checkColumnBingo(array3d):
    b = Board()
    count = 0
    for array in array3d:
        trans_arr = array.T
        for i in range(trans_arr.shape[0]):
            if np.all(trans_arr[i] == 1):
                print('Bingo på kolonne: ', i)
                b.bingo = True
                b.index = count
                return b
        count += 1
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

    for number in arr_data:
        print(number)

        for i in range(empty_line_count):
            #print(arr_3d[i])
            for j in range(5):
                #print(arr_3d[i][j])
                for k in range(5):
                    #print(arr_3d[i][j][k])
                    if arr_3d[i][j][k] == number:
                        a_3d_array[i][j][k] = 1
                        cBoard = checkColumnBingo(a_3d_array)
                        rBoard = checkRowBingo(a_3d_array)
                        if cBoard.bingo:
                            print(arr_3d[cBoard.index])
                            print(a_3d_array[cBoard.index])
                            sum = 0
                            for l in range(5):
                                for m in range(5):
                                    if a_3d_array[rBoard.index][l][m] == 0:
                                        sum += arr_3d[rBoard.index][l][m]
                            print(sum*number)
                            break
                        elif rBoard.bingo:
                            print(arr_3d[rBoard.index])
                            print(a_3d_array[rBoard.index])
                            sum = 0
                            for l in range(5):
                                for m in range(5):
                                    if a_3d_array[rBoard.index][l][m] == 0:
                                        sum += arr_3d[rBoard.index][l][m]
                            print(sum*number)

                            break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break


# Control execution of code
if __name__ == "__main__":
    main()