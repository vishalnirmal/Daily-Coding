##############################################
# Stack using Linked List                    #
# by Vishal Nirmal                           #
#                                            #
# A Stack ADT implementation.                #
##############################################




class Stack:

    class Node:

        def __init__(self, data=None):

            self.data = data

            self.next = None

    def __init__(self):

        self.start = None

        self.top = -1

    def push(self, data):

        nnode = Stack.Node(data)

        if self.top==-1:

            self.start = nnode

            self.top+=1

            return

        nnode.next = self.start

        self.start = nnode

        self.top+=1

    def pop(self):

        if self.top==-1:

            print('Stack is empty.')

            return None

        data = self.start.data

        self.start = self.start.next

        self.top-=1

        return data

    def Top(self):

        if self.top==-1:

            print('Stack is empty.')

            return None

        return self.start.data

    def size(self):

        return self.top+1

    def printStack(self):

        if self.top==-1:

            print('Stack is empty.')

            return 

        current = self.start

        while current:

            print(current.data, end = ' ')

            current = current.next