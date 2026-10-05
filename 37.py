import sys
class Stack:
    def __init__(self,size):
        self.Stacksize = size
        self.myStack = []
    def isFull(self):
        if len(self.myStack) == self.Stacksize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
    def push(self,data):
        if self.isFull():
            print("Stack is Full")
        else:
            self.myStack.append(data)
            print("Element pushed")
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack.pop())
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(("Top Element = " ,self.myStack[-1]))
    def deletestack(self):
        self.myStack=None
        print("Delete Stack Done")
    def displayStack(self):
        print(self.myStack)    
    def maxnumber(self):
        if self.isEmpty():
           print("Stack is Empty")
        else:
           print("Max Element =", max(self.myStack))     
size = int(input("Enter the size of Stack :")) #Execution Starts from here
obj = Stack(size)
while True:
    print("1. Push Operation")
    print("2. Pop Operation")
    print("3. Peek Operation")
    print("4. isEmpty Operation")
    print("5. isFull Operation")
    print("6. Delete Complete Stack")
    print("7. Display Stack")
    print("8. Maximum Number in the Stack")
    print("9. Exit")

    choice = int(input("Enter your Choice : "))
    if choice == 1:
        value = int(input("Enter the value to push in the stack :"))
        obj.push(value)
    elif choice == 2:
        obj.pop()
    elif choice == 3:
        obj.peek()
    elif choice == 4:
        print(obj.isEmpty())
    elif choice == 5:
        print(obj.isFull())
    elif choice == 6:
        obj.deletestack()
    elif choice == 7:
        obj.displayStack()
    elif choice == 8:
        obj.maxnumber()
    else:
        sys.exit()
# Recursion - a way of solving a problem by having a function calling itself
# Performing the same operation multiple times with different inputs
# In every step we try smaller inputs to make the problem smaller
# Base conditions is needed to stop the recursion, otherwise infinite loop will occur
# Usage of recursion in data structure like trees and graphs
# used in many algorithms (divide and conquer, greedy and dynamic programming)
# Recursion uses Stack Memory
