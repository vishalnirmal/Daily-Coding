##############################################
# Queue using Linked List                    #
# by Vishal Nirmal                           #
#                                            #
# A Queue ADT implementation.                #
##############################################




class Queue:

    class Node:

        def __init__(self, data=None):

            self.data = data

            self.next = None

    def __init__(self):

        self.front = None

        self.rear = None

    def isEmpty(self):

        return self.front == None

    def enQueue(self, data):

        nnode = Queue.Node(data)

        if self.front == None:

            self.front = self.rear = nnode

            return

        self.rear.next = nnode

        self.rear = nnode

    def deQueue(self):

        if self.isEmpty():

            print('Queue is empty.')

            return

        data = self.front.data

        self.front = self.front.next

        return data

    def count(self):

        current = self.front

        count = 0

        while current:

            count+=1

            current = current.next

        return count

    def printQueue(self):

        if self.isEmpty():

            print('Queue is empty.')

            return

        current = self.front

        while current:

            print(current.data, end=' ')

            current = current.next

    def Front(self):

        if self.isEmpty():

            print('Queue is empty.')

            return

        return self.front.datah