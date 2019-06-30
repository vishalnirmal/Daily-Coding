##############################################
# Stack using Array                          #
# by Vishal Nirmal                           #
#                                            #
# A Stack ADT implementation.                #
##############################################




class Stack:

    def __init__(self):

        self.top = -1

        self.arr = []

    def push(self, data):

        self.top+=1

        self.arr.append(data)

    def pop(self):

        if self.top==-1:

            print("Stack is empty.")

            return None

        data = self.arr[self.top]

        self.arr.pop(self.top)

        self.top-=1

        return data

    def Top(self):

        if self.top==-1:

            return None

        return self.arr[self.top]

    def size(self):

        return self.top+1

    def printStack(self):

        if self.top == -1:

            print('The stack is empty.')

            return

        for i in self.arr[-1::-1]:

            print(i, end=' ')