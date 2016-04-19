# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:58:48 2016

@author: shashank

Creating a stack
"""

class Stacks:
    
    def __init__(self, top = None, MaxSize = 5):
        self.stack=[]
        self.top = top
        self.MaxSize = MaxSize
        
    def push(self, data):
        if self.top == None:
            self.stack.append(data)
            self.top = 0
        elif self.top ==self.MaxSize -1:
            raise ValueError("Stack is full!")
            return None
        else:
            self.stack.append(data)
            self.top += 1
    
    def pop(self):
        if self.top == None or self.top == -1:
            raise ValueError("Stack is empty!")
            return None
        else:
            temp = self.stack[self.top]
            self.top -= 1
            self.stack.pop()
            return temp
        
    def peek(self):
        if self.top == None or self.top == -1:
            raise ValueError("Stack is empty!")
            return None
        else:
            return self.stack[self.top]


st = Stacks(top = None, MaxSize = 3)
st.push(10)
st.push(20)
st.push(30)
st.push(40)
print(st.pop())
print(st.peek())