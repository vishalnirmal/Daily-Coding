##############################################
# Queue using Arrays                         #
# by Vishal Nirmal                           #
#                                            #
# A Queue ADT implementation.                #
##############################################




class Queue:

    def __init__(self, size=5):

        self.front = -1

        self.rear = 0

        self.size = size

        self.arr = [-1]*self.size

    def isEmpty(self):

        return self.front == -1

    def isFull(self):

        return self.front == self.rear

    def enQueue(self, data):

        if self.isFull():

            print('Queue is full.')

            return

        if self.isEmpty():

            self.front = 0

        self.arr[self.rear] = data

        self.rear = (self.rear + 1) % self.size

    def deQueue(self):

        if self.isEmpty():

            print('Queue is empty.')

            return

        data = self.arr[self.front]

        self.arr[self.front] = -1

        self.front += 1

        return data

    def printQueue(self):

        if self.isEmpty():

            print('Queue is empty.')

            return

        i = self.front

        while True:

            print(self.arr[i], end=' ')

            i = (i + 1) % self.size

            if i == self.rear:

                print()

                break

    def count(self):

        if self.isEmpty():

            return 0

        if self.rear < self.front:

            return self.rear + self.size - self.front

        else:

            return (self.rear - 1) % self.size + 1 - self.front

    def Front(self):

        if self.isEmpty():

            print('Queue is empty.')

            return

        return self.arr[self.front]