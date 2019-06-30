##############################################
# Doubly Linked List                         #
# by Vishal Nirmal                           #
#                                            #
# A Doubly Linked List ADT implementation.   #
##############################################




class DLL:

    class DLLNode:

        def __init__(self, data=None):

            self.data = data

            self.next = None

            self.prev = None

    def __init__(self):

        self.start = None

    def traverseList(self):

        if self.start == None:

            print('The list is empty.')

            return

        else:

            current = self.start

            while current.next:

                print(current.data, '<->', end=' ')

                current = current.next

            print(current.data)

    def insertAtBeginning(self, data):

        nnode = DLL.DLLNode(data)

        if self.start == None:

            self.start = nnode

        else:

            nnode.next = self.start

            self.start.prev = nnode

            self.start = nnode

    def insertAtEnd(self, data):

        nnode = DLL.DLLNode(data)

        if self.start == None:

            self.start = nnode

        else:

            current = self.start

            while current.next:

                current = current.next

            current.next = nnode

            nnode.prev = current

    def insert(self, data, pos):

        k=1

        nnode = DLL.DLLNode(data)

        if self.start == None and pos != 1:

            print('Invalid position.')

            return 

        if pos == 1:

            if self.start == None:

                self.start = nnode

            else:

                self.start.prev = nnode

                nnode.next = self.start

                self.start = nnode

            return

        p = self.start

        while p and k < pos:

            q = p

            p = p.next

            k+=1

        if k!=pos:

            print('Invalid position.')

            return

        nnode.prev = q

        q.next = nnode

        nnode.next = p

        if p:

            p.prev = nnode

    def deleteAtBeginning(self):

        if self.start == None:

            print('The list is empty.')

            return

        else:

            data = self.start.data

            self.start = self.start.next

            self.start.prev = None

            return data

    def deleteAtEnd(self):

        if self.start == None:

            print('The list is empty.')

            return

        else:

            current = self.start

            temp = None

            while current.next:

                temp = current

                current = current.next

            if temp:

                temp.next = None

            else:

                self.start = None

    def delete(self, pos):

        if self.start == None:

            print('The list is empty.')

            return

        if pos == 1:

            self.start = self.start.next

            return

        current = self.start

        temp = None

        k=1

        while current and k<pos:

            temp = current

            current = current.next

            k+=1

        if current == None:

            print('Invalid position.')

            return

        if current.next:

            current.next.prev = temp

        temp.next = current.next

    def get(self, pos):

        if self.start == None:

            print('The list is empty.')

            return

        current = self.start

        k = 1

        while current and k < pos:

            current = current.next

            k+=1

        if current == None:

            print('Invalid position.')

            return

        return current.data

    def search(self, data):

        if self.start == None:

            print('The list is empty.')

            return

        current = self.start

        k=1

        while current and current.data != data:

            current = current.next

            k+=1

        if current:

            return k

        print('{} not present in the list.'.format(data))

    def addNodes(self, arr):

        nnode = DLL.DLLNode(arr[0])

        n1 = nnode

        for i in arr[1:]:

            node = DLL.DLLNode(i)

            n1.next = node

            node.prev = n1

            n1 = node

        if self.start != None:

            print('Appending the data at the end of the list.')

            current = self.start

            while current.next:

                current = current.next

            current.next = nnode

            nnode.prev = current

        else:

            self.start = nnode

    def count(self):

        current = self.start

        c=0

        while current:

            current = current.next

            c+=1

        return c

    def reverseList(self):

        current = self.start

        while current.next:

            temp = current.next

            current.next = current.prev

            current.prev = temp

            current = temp

        temp = current.next

        current.next = current.prev

        current.prev = temp

        self.start = current







# >>> l1 = DLL()

# >>> l1.insertAtBeginning(34)

# >>> l1.traverseList()

# 34

# >>> l1.insertAtEnd(12)

# >>> l1.traverseList()

# 34 <-> 12

# >>> l1.insert(8, 2)

# >>> l1.traverseList()

# 34 <-> 8 <-> 12

# >>> l1.addNodes([1, 4, 2, 7, 3])

# Appending the data at the end of the list.

# >>> l1.traverseList()

# 34 <-> 8 <-> 12 <-> 1 <-> 4 <-> 2 <-> 7 <-> 3

# >>> l1.deleteAtBeginning()

# 34

# >>> l1.traverseList()

# 8 <-> 12 <-> 1 <-> 4 <-> 2 <-> 7 <-> 3

# >>> l1.deleteAtEnd()

# >>> l1.traverseList()

# 8 <-> 12 <-> 1 <-> 4 <-> 2 <-> 7

# >>> l1.delete(3)

# >>> l1.traverseList()

# 8 <-> 12 <-> 4 <-> 2 <-> 7

# >>> l1.count()

# 5

# >>> l1.get(3)

# 4

# >>> l1.search(2)

# 4