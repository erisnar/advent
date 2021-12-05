#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

class Position:
    def __init__(self):
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0

def plotDiagram(positions):
    for p in positions:
        x_values = [p.startX, p.endX]
        y_values = [p.startY, p.endY]

        plt.plot(x_values, y_values)
    
    # setting x and y axis range
    plt.ylim(-1,1000)
    plt.xlim(-1,1000)
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    plt.gca().invert_yaxis()
    
    # function to show the plot
    plt.show()


def horizontal(p, points):
    start = f"{p.startX},{p.startY}"
    if start not in points.keys():
        points[start] = 1
    else:
        points[start] = points[start] + 1
    temp = p.startY
    while temp != p.endY:
        if temp < p.endY:
            temp = temp + 1
        else:
            temp = temp - 1
        point = f"{p.startX},{temp}"
        if point not in points.keys():
            points[point] = 1
        else: 
            points[point] = points[point] + 1
    return points

def vertical(p, points):
    start = f"{p.startX},{p.startY}"
    if start not in points.keys():
        points[start] = 1
    else:
        points[start] = points[start] + 1
    temp = p.startX
    while temp != p.endX:
        if temp < p.endX:
            temp = temp + 1
        else:
            temp = temp - 1
        point = f"{temp},{p.startY}"
        if point not in points.keys():
            points[point] = 1
        else: 
            points[point] = points[point] + 1
    return points

def diagonally(p, points):
    start = f"{p.startX},{p.startY}"
    if start not in points.keys():
        points[start] = 1
    else:
        points[start] = points[start] + 1
    tempX = p.startX
    tempY = p.startY
    while tempX != p.endX:
        if tempX < p.endX:
            tempX = tempX + 1
        else:
            tempX = tempX - 1
        if tempY < p.endY:
            tempY = tempY + 1
        else:
            tempY = tempY - 1
        point = f"{tempX},{tempY}"
        if point not in points.keys():
            points[point] = 1
        else: 
            points[point] = points[point] + 1
    return points

def readFile():
    lines = np.loadtxt("input", delimiter=" -> ", unpack=False, dtype=str)
    for line in lines:
        print(line)
    return lines

def main():
    points = {}
    positions = []
    file = readFile()
    for line in file:
        p = Position()
        p.startX = int(line[0].split(",")[0])
        p.startY = int(line[0].split(",")[1])
        p.endX = int(line[1].split(",")[0])
        p.endY = int(line[1].split(",")[1])
        positions.append(p)
        if p.startX == p.endX:
            points = horizontal(p, points)
        elif p.startY == p.endY:
            points = vertical(p, points)
        elif abs(p.endX-p.startX) == abs(p.endY-p.startY): # vertical line at 45 degrees
            points = diagonally(p, points)
    print(points) 
    overlapping = 0 
    for i in points.keys(): 
        if points[i] > 1:
            overlapping += 1 
    print("Number of overlapping positions: ", overlapping)

    plotDiagram(positions)

# Control execution of code
if __name__ == "__main__":
    main()