# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 15:01:15 2016

@author: shashank

Create a Queue
"""

class queues:
    def __init__(self, MaxSize = 5):
        self.queue = []
        self.top = None
        self.bottom = None
        self.MaxSize = MaxSize
        
    def enqueue(self, data):
        if (self.top==None and self.bottom ==None) or (self.top== -1 and self.bottom == -1) or (self.bottom < self.top):
            self.queue.append(data)
            self.top = 0
            self.bottom = 0
        elif (self.bottom - self.top + 1) == self.MaxSize:
            raise ValueError ("Queue is Full!")
            return None
        else:
            self.queue.append(data)
            self.bottom += 1
    
    def dequeue(self):
        if (self.top==None and self.bottom ==None) or (self.top== -1 and self.bottom == -1) or (self.bottom < self.top):
            self.bottom = -1
            self.top = -1
            self.queue = []
            raise ValueError ("Queue is Empty!")
            return None
        else:
            temp = self.queue[self.top]
            self.top += 1
            return temp
    
    def peek(self):
        if (self.top==None and self.bottom ==None) or (self.top== -1 and self.bottom == -1) or (self.bottom < self.top):
            raise ValueError ("Queue is Empty!")
            return None
        else:
            return self.queue[self.top]
    
    def display(self):
        if (self.top==None and self.bottom ==None) or (self.top== -1 and self.bottom == -1) or (self.bottom < self.top):
            raise ValueError ("Queue is Empty!")
            return None
        else:
            print(*self.queue[self.top:self.bottom+1])
    
    def size(self):
        if (self.top==None and self.bottom ==None) or (self.top== -1 and self.bottom == -1) or (self.bottom < self.top):
            raise ValueError ("Queue is Empty!")
            return None
        else:
            return (self.bottom - self.top +1)


q = queues(MaxSize = 5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

q.peek()
q.display()
q.size()
