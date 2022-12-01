
import numpy as np

def readFile():
    lines = np.loadtxt("input", dtype=str)
    return lines

    
if __name__ == "__main__":

        caves = readFile()
    cavesTuples = []

    for pair in caves:
        cavesTuples.append(tuple(map(str, pair.split('-'))))

    for edge in cavesTuples:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph