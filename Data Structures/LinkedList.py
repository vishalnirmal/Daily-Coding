##############################################
# Simple Linked List                         #
# by Vishal Nirmal                           #
#                                            #
# A Single Linked List ADT implementation.   #
##############################################



class LinkedList:
    class Node:
        def __init__(self):
            self.data = None
            self.next = None
    def __init__(self):
        self.start = None
        self.length = None
    def traverseList(self):
        if self.start == None:
            print('The list is empty.')
            return
        current = self.start
        while current.next:
            print(current.data, '->', end=' ')
            current = current.next
        print(current.data)
    def insertAtBeginning(self, data):
        if self.start == None:
            self.start = LinkedList.Node()
            self.start.data = data
        else:
            nnode = LinkedList.Node()
            nnode.data = data
            nnode.next = self.start
            self.start = nnode
    def insertAtEnd(self, data):
        if self.start == None:
            self.start = LinkedList.Node()
            self.start.data = data
        else:
            current = self.start
            while current.next:
                current = current.next
            nnode = LinkedList.Node()
            nnode.data = data
            current.next = nnode
    def insert(self, data, pos):
        k = 1
        if self.start == None and pos!=1:
            print('Invalid position.')
            return
        nnode = LinkedList.Node()
        nnode.data = data
        if pos == 1:
            nnode.next = self.start
            self.start = nnode
        else:
            n1 = self.start
            while n1 and k<pos:
                n2 = n1
                n1 = n1.next
                k+=1
            n2.next = nnode
            nnode.next = n1
    def deleteAtBeginning(self):
        if self.start == None:
            print('The list is empty.')
            return 
        data = self.start.data
        self.start = self.start.next
        return data
    def deleteAtEnd(self):
        if self.start == None:
            print('The list is empty.')
            return
        elif self.start.next == None:
            data = self.start.data
            self.start = None
            return data
        else:
            n1 = self.start
            while n1.next.next:
                n1 = n1.next
            data = n1.next.data
            n1.next = None
            return data
    def delete(self, pos):
        k=1
        if self.start == None:
            print('The list is empty.')
            return
        p = self.start
        if pos == 1:
            data = self.start.data
            self.start = self.start.next
            return data
        else:
            while p and k < pos:
                k+=1
                q = p
                p = p.next
            if p == None:
                print('Invalid position.')
                return
            else:
                data = p.data
                q.next = p.next
                return data
    def get(self, pos):
        if self.start == None:
            print('The list is empty.')
            return
        else:
            k=1
            current = self.start
            while current and k != pos:
                current = current.next
                k+=1
            if current == None:
                print('Invalid position.')
                return
            return current.data
    def search(self, data):
        current = self.start
        k=1
        while current:
            if current.data == data:
                return k
            k+=1
            current = current.next
        print('{} does not exist in the list.'.format(data))
    def addNodes(self, arr):
        nnode = LinkedList.Node()
        nnode.data = arr[0]
        n1 = nnode
        for i in arr[1:]:
            node = LinkedList.Node()
            node.data = i
            n1.next = node
            n1 = node
        if self.start != None:
            print('Appending the data at the end of the list.')
            current = self.start
            while current.next:
                current = current.next
            current.next = nnode
        else:
            self.start = nnode
    def count(self):
        current = self.start
        c = 0
        while current:
            current = current.next
            c+=1
        return c
    def reverseList(self):
        current = self.start
        prev = None
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.start = prev

############################################################
# >>> l1 = LinkedList()                                    #
# >>> l1.insertAtBeginning(8)                              #
# >>> l1.insertAtEnd(12)                                   #
# >>> l1.traverseList()                                    #
# 8 -> 12                                                  #
# >>> l1.addNodes([4, 5, 6, 3, 1])                         #
# Appending the data at the end of the list.               #
# >>> l1.traverseList()                                    #
# 8 -> 12 -> 4 -> 5 -> 6 -> 3 -> 1                         #
# >>> l1.deleteAtBeginning()                               #
# 8                                                        #
# >>> l1.deleteAtEnd()                                     #
# 1                                                        #
# >>> l1.delete(3)                                         #
# 5                                                        #
# >>> l1.traverseList()                                    #
# 12 -> 4 -> 6 -> 3                                        #
# >>> l1.search(6)                                         #
# 3                                                        #
# >>> l1.get(4)                                            #
# 3                                                        #
############################################################