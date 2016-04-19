# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:10:12 2016

@author: shashank

Creating Trees
"""

class trees:
    
    def __init__(self, tree, root):
        self.tree = tree
        self.root = root
        
    def TreeValidation(self):
        if type(self.tree) != type({}):
            raise ValueError("Not a dictionary!")
            return None
        
        if self.tree == {}:
            raise ValueError("Empty Tree!")
            return None
        
        if self.root == None:
            raise ValueError("Empty Root !")
            return None
        
        if self.root not in self.tree:
            raise ValueError("Root is not present in the tree!")
            return None
        
    def PreOrder(self,node):
        print(node)
        
        if len(self.tree[node])>0:
            if len(self.tree[node]) == 1:
                self.PreOrder(self.tree[node][0])
            if len(self.tree[node]) == 2:
                self.PreOrder(self.tree[node][0])
                self.PreOrder(self.tree[node][1])
    
    def InOrder(self, node):
        if len(self.tree[node]) > 0:
            if len(self.tree[node]) == 1:
                if self.tree[node] > node:
                    print(node)
                    self.InOrder(self.tree[node][0])
                else:
                    self.InOrder(self.tree[node][0])
            if len(self.tree[node]) == 2:
                self.InOrder(self.tree[node][0])
                print(node)
                self.InOrder(self.tree[node][1])
        else:
            print(node)

    def PostOrder(self, node):
        if len(self.tree[node]) > 0:
            if len(self.tree[node]) == 1:
                self.PostOrder(self.tree[node][0])
                print(node)
            if len(self.tree[node]) == 2:
                self.PostOrder(self.tree[node][0])
                self.PostOrder(self.tree[node][1])
                print(node)
        else:
            print(node)
	
		

tree = {15:[7,20], 7:[4,12], 20:[16,23], 4:[], 12:[], 16:[], 23:[]}

t1 = trees(tree,15)

t1.PreOrder(15)

t1.InOrder(15)

t1.PostOrder(15)