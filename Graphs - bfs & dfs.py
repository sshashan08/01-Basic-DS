# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:54:27 2016

@author: shashank

Graph Traversal
"""

class graphs:
    def __init__(self, G, start):
        self.G = G
        self.start = start
        self.visited = []
        self.stack = []
        self.queue = []
    
    def dfs(self):
        if self.start == None:
            raise ValueError ("Start Node Absent!")
            return None
        
        if type(self.G) != type({}):
            raise ValueError ("Not a dictionary graph input!")
            return None
        
        if self.G == {}:
            raise ValueError ("Empty Graph!")
            return None
            
        if self.start not in self.G:
            raise ValueError ("Starting node is not present in graph!")
            return None
            
        self.stack = [self.start,]
        
        while self.stack:
            node = self.stack.pop()
            
            if node not in self.visited:
                self.visited.append(node)
                self.stack.extend([x for x in self.G[node] if x not in self.visited])
        
        return self.visited
    
    def bfs(self):
        if self.start == None:
            raise ValueError ("Start Node Absent!")
            return None
        
        if type(self.G) != type({}):
            raise ValueError ("Not a dictionary graph input!")
            return None
        
        if self.G == {}:
            raise ValueError ("Empty Graph!")
            return None
            
        if self.start not in self.G:
            raise ValueError ("Starting node is not present in graph!")
            return None
            
        self.queue = [self.start,]
        self.visited = []
        
        while self.queue:
            node = self.queue.pop(0)
            
            if node not in self.visited and node not in self.queue:
                self.visited.append(node)
                self.queue.extend([x for x in self.G[node] if x not in self.visited])
                
        return self.visited
        


graph1 = {'A': ['B' , 'C'],
          'B': ['A', 'D', 'E'],
          'C': ['A', 'F'],
          'D': ['B'],
          'E': ['B','F'],
          'F': ['C','E']}

g = graphs(graph1,'A')

print(*g.dfs())

print(*g.bfs())

