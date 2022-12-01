
from collections import defaultdict
import numpy as np
import itertools

def readFile():
    lines = np.loadtxt("input", dtype=str)
    return lines

# Function to build the graph
def build_graph():

    graph = defaultdict(list)
    
    caves = readFile()
    cavesTuples = []

    for pair in caves:
        cavesTuples.append(tuple(map(str, pair.split('-'))))

    for edge in cavesTuples:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph
  
def find_all_paths(graph, start, end, path =[]):
    newpaths = []
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node.isupper():
            newpaths = find_all_paths(graph, node, end, path)
        elif node not in path:
            newpaths = find_all_paths(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths
    
if __name__ == "__main__":

    graph = build_graph()
    all_paths = find_all_paths(graph, 'start', 'end')
    all_paths.sort()
    all_paths = list(all_paths for all_paths,_ in itertools.groupby(all_paths))

    for a in all_paths:
        print(a)
    
    print(len(all_paths))