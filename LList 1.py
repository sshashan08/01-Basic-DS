# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:56:28 2016

@author: shashank
Creating a linked list

"""

########################################################################
### Defining the Node Structure
########################################################################
class Node:
    
    # initialize the constructor
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    # pulling the value
    def getdata(self):
        return self.data

    # pulling the next node    
    def getnext(self):
        return self.next

    # changing the data value in the node    
    def setdata(self, newdata):
        self.data = newdata

    # changing the next node    
    def setnext(self, newnext):
        self.next = newnext


########################################################################
### Defining the single linked list class and its operations
########################################################################
class LinkedList:
    
    # initializing the default head node
    def __init__(self, head = None):
        self.head = head
    
    # inserting new node into the list
    def insert(self, newdata):
        new_node = Node(newdata)
        new_node.setnext(self.head)
        self.head = new_node
        
    # checking the size of the list
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.getnext()
            if current == None:
                break
        return count

    # Searching the list for a specified value    
    def search(self, data):
        found = False
        current = self.head
        while current and found is False:
            if current.getdata() == data:
                found = True
            else:
                current = current.getnext()
        if current is None:
            raise ValueError("Data not found !!")
            return None
        return current.getdata()
    
    # Deleting an element from the list    
    def delete(self, data):
        found = False
        previous = None
        current = self.head
        
        while current and found is False:
            if current.getdata() == data:
                found = True
            else:
                previous = current
                current = current.getnext()
        if current == None:
            raise ValueError("Data not found !!")
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())
    
    
    # displaying the entire linked list    
    def display(self):
        current = self.head
        
        while current:
            print(current.getdata())
            current = current.getnext()
            if current == None:
                break




############################################################################
### | Using the linked list
############################################################################
mylist = LinkedList()

mylist.insert(10)

mylist.insert(20)

mylist.insert(30)

mylist.insert(40)

print(mylist.size())

mylist.display()

mylist.delete(30)
        