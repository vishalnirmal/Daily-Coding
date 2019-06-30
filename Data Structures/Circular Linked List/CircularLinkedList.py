##############################################
# Circular Linked List                       #
# by Vishal Nirmal                           #
#                                            #
# A Circular Linked List ADT implementation. #
##############################################




class CLL:

    class Node:

        def __init__(self, data=None):

            self.data = data

            self.next = None

    def __init__(self):

        self.start = None

    def count(self):

        if self.start == None:

            return 0

        current = self.start

        c=0

        while True:

            c+=1

            current = current.next

            if current == self.start:

                break

        return c

    def traverseList(self):

        if self.start == None:

            print('The list is empty.')

            return

        current = self.start

        while True:

            print(current.data, '->', end=' ')

            current = current.next

            if current == self.start:

                break

    def insertAtBeginning(self, data):

        nnode = CLL.Node(data)

        nnode.next = nnode

        if self.start == None:

            self.start = nnode

            return

        current = self.start

        while current.next != self.start:

            current = current.next

        current.next = nnode

        nnode.next = self.start

        self.start = nnode

    def insertAtEnd(self, data):

        nnode = CLL.Node(data)

        nnode.next = nnode

        if self.start == None:

            self.start = nnode

            return 

        current = self.start

        while current.next != self.start:

            current = current.next

        current.next = nnode

        nnode.next = self.start

    def deleteAtFront(self):

        if self.start == None:

            print('The list is empty.')

            return

        if self.start.next == self.start:

            temp = self.start

            del(temp)

            self.start = None

            return

        current = self.start

        temp = self.start

        while current.next != self.start:

            current = current.next

        current.next = self.start.next

        self.start = self.start.next

        del(temp)

    def deleteAtEnd(self):

        if self.start == None:

            print('The list is empty.')

            return

        if self.start.next == self.start:

            temp = self.start

            self.start = None

            del(temp)

            return

        current = temp = self.start

        while current.next != self.start:

            temp = current

            current = current.next

        temp.next = self.start

        del(current)

    def insert(self, data, pos=1):

        if self.start == None and pos != 1 and pos != -1:

            print('Invalid position.')

            return

        if pos == 1:

            self.insertAtBeginning(data)

            return

        if pos == -1:

            self.insertAtEnd(data)

            return

        k = 1

        nnode = CLL.Node(data)

        nnode.next = nnode

        current = self.start

        while current.next != self.start and k<pos:

            temp = current

            current = current.next

            k+=1

        if k != pos:

            print('Invalid position.')

            return

        temp.next = nnode

        nnode.next = current

    def delete(self, pos=-1):

        if self.start == None:

            print('The list is empty.')

            return

        if pos == 1:

            self.deleteAtFront()

            return

        if pos == -1:

            self.deleteAtEnd()

            return

        k=1

        current = self.start

        while current.next != self.start and k < pos:

            temp = current

            current = current.next

            k+=1

        if k != pos:

            print('Invalid position.')

            return

        temp.next = current.next

        del(current)

    def insertNodes(self, arr):

        if self.start != None:

            print('The items are appended to the list.')

        for i in arr:

            self.insert(i, -1)

    def get(self, pos=1):

        if self.start == None:

            print('The list is empty.')

            return

        if pos == 1:

            return self.start.data

        k = 1

        current = self.start

        while current.next != self.start and k<pos:

            k+=1

            current = current.next

        if k != pos:

            print('Invalid position.')

            return

        return current.data

    def search(self, data):

        if self.start == None:

            print('The list is empty.')

            return

        current = self.start

        k=1

        while True:

            if current.data == data:

                return k

            current = current.next

            if current == self.start:

                break

            k+=1

        return -1











# >>> l1 = CLL()

# >>> l1.insertAtBeginning(79)

# >>> l1.traverseList()

# 79 -> 

# >>> l1.insertAtEnd(65)

# >>> l1.traverseList()

# 79 -> 65 -> 

# >>> l1.insert(46, 2)

# >>> l1.traverseList()

# 79 -> 46 -> 65 -> 

# >>> l1.insertNodes([34,23,90,23,63])

# The items are appended to the list.

# >>> l1.traverseList()

# 79 -> 46 -> 65 -> 34 -> 23 -> 90 -> 23 -> 63 -> 

# >>> l1.count()

# 8

# >>> l1.get(3)

# 65

# >>> l1.search(90)

# 6

# >>> l1.deleteAtFront()

# >>> l1.traverseList()

# 46 -> 65 -> 34 -> 23 -> 90 -> 23 -> 63 -> 

# >>> l1.deleteAtEnd()

# >>> l1.traverseList()

# 46 -> 65 -> 34 -> 23 -> 90 -> 23 -> 

# >>> l1.delete(3)

# >>> l1.traverseList()

# 46 -> 65 -> 23 -> 90 -> 23 -> 