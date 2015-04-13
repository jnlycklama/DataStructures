

import random
from collections import defaultdict
from heapq import *
from collections import deque


print "Testing using the graph given below: "

def breadthFirstSearch(graph, start):
    
        queue = []
        visited = []
        totalWeight = 0
        visited.append(start)
        queue.append(start)
        while len(queue) > 0:
            
            vertex = queue[0]
            del queue[0]
            for i in graph[vertex]:
                
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                    totalWeight += graph[vertex][i]
                    
        print "BFS Tree : ", visited;
        return totalWeight
                
def primMST(vertices, edges):
    
    connected = defaultdict(list)
    for vertex_one, vertex_two, c in edges:
        
        connected[vertex_one].append((c,vertex_one,vertex_two))
        connected[vertex_two].append((c,vertex_two,vertex_one))
    MST = []
    totalWeight = 0
    visited = set(vertices[0])
    unvisited = connected[vertices[0]][:]
    heapify(unvisited)
    while unvisited:
                                     
        weight, vertex_one, vertex_two = heappop(unvisited)
        if vertex_two not in visited:
                                     
            visited.add(vertex_two)
            MST.append((vertex_one, vertex_two, weight))
            totalWeight += weight
            for edge in connected[vertex_two]:
                                     
                if edge[2] not in visited:
                    heappush(unvisited, edge)
    print "Prim Tree: ", MST;
    return totalWeight
    

# Dictorionary for BFS
graph = {'A':{'B':15, 'D':7, 'E':10},
         'B':{'A':15,'C':9, 'D':11, 'F':9},
         'C':{'B':9, 'E':12, 'F':7},
         'D':{'A':7, 'B':11, 'E':8, 'F':14},
         'E':{'A':10, 'C':12, 'D':8, 'F':8},
         'F':{'B':9, 'C':7,'D':14,'E':8}
        }

# List for Prim's Algorithm
vertices = list("ABCDEF")
edge1 = [("A","B",15), ("F", "C", 7), ("A","D",7), ("A","E",10),
         ("B","C",9),("B","D",11),("B","F",9),
         ("C", "B", 9),("C","E",12), ("C","F",7),
         ("D","A",7), ("B", "A", 15),("D","E",8),("D","F",14),
         ("E", "A", 10), ("E","C",12),("E","D",8),("E","F",8),("D", "B", 11),
         ("F","B",9),  ("F","E",8)]

print "\n"
print breadthFirstSearch(graph, 'A')
print primMST(vertices, edge1)

print "\n"
print "Testing using randomly generated graphs, sizes 100 - 500"
print "\n"

class vertex(object):
    def __init__(self, value):
        self.value = value
        self.neighbours = []
        
    def addNeighbour(self, friend):
        self.neighbours.append(friend)

class graph(object):
    def __init__(self):
        self.numOfVertices = 0
        self.vertices = []
        
    def addVertex(self):
        self.vertices.append(vertex(self.numOfVertices))
        self.numOfVertices += 1
        
    def addEdge(self, x, y):
        self.vertices[x].addNeighbour(y)
        self.vertices[y].addNeighbour(x)

    def addWeight(self, x, y):
        weight = random.randint(10,100)
        return weight

    def getWeight(self, x, y):
        weight = addWeight(self, x, y)
        return weight
    
    def neighbours(self):
        for i in range(self.numOfVertices):
            print i, self.vertices[i].neighbours

    def isEdge(self, x, y):
        return y in self.vertices[x].neighbours
    
    #created given notes in class
    def primMST(self, vertices, edges):
        connected = defaultdict(list) # dictionary that will hold the verticies
        for vertex_one, vertex_two, c in edges:
            connected[vertex_one].append((c,vertex_one,vertex_two))
            connected[vertex_two].append((c,vertex_two,vertex_one))

        MST = []
        totalWeight = 0
        visited = set(vertices[0]) 
        unvisited = connected[vertices[0]][:]
        heapify(unvisited) #heap of unvisited verticies

        while unvisited:
            weight, vertex_one, vertex_two = heappop(unvisited)
            if vertex_two not in visited:
                visited.add(vertex_two)
                MST.append((vertex_one, vertex_two, weight))
                totalWeight += weight

                for edge in connected[vertex_two]:
                    if edge[2] not in visited:
                        heappush(unvisited, edge) 
        return totalWeight

    #created given notes in class
    def breadthFirstSearch(self, graph, start):
        queue = []
        visited = []
        totalWeight = 0
        visited.append(start)
        queue.append(start)

        while len(queue) > 0:
            vertex = queue[0]
            del queue[0]
            for neighbour in graph[vertex]: # for every neighbour of the vertex
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
                    totalWeight += graph[vertex][neighbour]
        return totalWeight
    

"""
Running the experiments below, using objects above
List size starts at 100 and goes to 500
"""
n = 100

agents = []
f = open('top_secret_agent_aliases_2015.txt', 'r')
text = f.readlines()
for line in range(500):
    agents.append(text[line].rstrip('\n'))
for test in range(5):
    lis = agents[0:n]
    for trials in range(n):

        Graph = graph()
        Graph.addVertex()
        temp_two = {}
        adjacent = {}
        nbr = {}
        temporary = []
        edges = []
        averages = 0
        ratio = 0
        bfsPrimRatio = 0
        for i in range(1, n):
            
            Graph.addVertex()
            neighbour = random.randint(0, i-1)
            Graph.addEdge(i, neighbour)
            weight = Graph.addWeight(i, neighbour)
            temporary.append([lis[i], lis[neighbour], weight]) #adds two agents and the weight between

        # since prim needs tuples, you must convert the graph to tuples
        for tup in temporary:
            tupleSet = tuple(tup)
            edges.append(tupleSet)
            
        # BFS requires dictionary, so you must convert the graph again
        # Format so each key is the agent name, and the value is another dictionary of the neighbours
        for value in lis:
            temp_two.clear()
            adjacent.update({value:{}})
            
            for x in temporary:
                if x[0] == value:
                    temp_two[x[1]] = x[2]
                elif x[1] == value:
                    temp_two[x[0]] = x[2]
                    
                nbr = temp_two.copy()
                adjacent.update({value:nbr})
                
        #starts at frothing because that is the first word in the text file
        bfs = Graph.breadthFirstSearch(adjacent, 'frothing')
        prim = Graph.primMST(lis, edges)
        bfsPrimRatio = float(prim)/bfs
        averages += bfsPrimRatio
    print "Test with", n
    ratio = averages/n
    print "Ratio: ", ratio;
    n += 100


print "\n"
