##############################################
# Binary Search Tree                         #
# by Vishal Nirmal                           #
#                                            #
# A Binary Search Tree ADT implementation.   #
##############################################




class BST:

    def __init__(self, data=None):

        self.data = data

        self.left = None

        self.right = None

    def insert(self, data):

        if self.data == None:

            self.data = data

            return

        if self.data < data:

            if self.right:

                self.right.insert(data)

            else:

                self.right = BST(data)

        if self.data >= data:

            if self.left:

                self.left.insert(data)

            else:

                self.left = BST(data)

    def insertNodes(self, arr):

        for i in arr:

            self.insert(i)

    def inorder(self):

        if self == None:

            return None

        if self.left:

            self.left.inorder()

        print(self.data, end=' ')

        if self.right:

            self.right.inorder()

    def preorder(self):

        if self == None:

            return None

        print(self.data, end=' ')

        if self.left:

            self.left.preorder()

        if self.right:

            self.right.preorder()

    def postorder(self):

        if self == None:

            return None

        if self.left:

            self.left.postorder()

        if self.right:

            self.right.postorder()

        print(self.data, end=' ')

    def levelorder(self):

        if self == None:

            return None

        arr = [self]

        while len(arr):

            node = arr[0]

            if node.left:

                arr.append(node.left)

            if node.right:

                arr.append(node.right)

            print(node.data, end=' ')

            arr.pop(0)

    def min(self):

        if self == None:

            return None

        if self.left:

            return self.left.min()

        else:

            return self.data

    def max(self):

        if self == None:

            return None

        if self.right:

            return self.right.max()

        else:

            return self.data

    def delete(self, data):

#         print(self.data)

        if self == None:

            return None

        if data < self.data:

            if self.left:

#                 print('Going left side')

                self.left = self.left.delete(data)

            else:

                print('{} not present in the list.'.format(data))

        elif data > self.data:

            if self.right:

#                 print('Going right side.')

                self.right = self.right.delete(data)

            else:

                print('{} not present in the list.'.format(data))

        else:

            if self.left == None:

                temp = self.right

                self = None

                return temp

            if self.right == None:

                temp = self.left

                self = None

                return temp

            temp = self.right.min()

            self.data = temp

            self.right = self.right.delete(temp)

        return self

    def size(self):

        if self == None:

            return 0

        ls = rs = 0

        if self.left:

            ls = self.left.size()

        if self.right:

            rs = self.right.size()

        return ls+rs+1

    def height(self):

        if self == None:

            return None

        if self.left == None and self.right==None:

            return 0

        lh = rh = 0

        if self.left:

            lh = self.left.height()

        if self.right:

            rh = self.right.height()

        return max(lh, rh)+1

    def level(self):

        if self == None:

            return None

        if self.left == None and self.right==None:

            return 0

        lh = rh = 0

        if self.left:

            lh = self.left.level()

        if self.right:

            rh = self.right.level()

        return max(lh, rh)+1

    def search(self, data):

        if self == None:

            return None

        print(self.data, end=' ')

        if self==None:

            print('Nothing present in the tree.')

            return

        if data < self.data:

            if self.left:

                return self.left.search(data)

            else:

                return False

        elif data > self.data:

            if self.right:

                return self.right.search(data)

            else:

                return False

        return True

    def deepest(self):

        if self == None:

            return None

        arr = [self]

        while len(arr):

            node = arr[0]

            if node.left:

                arr.append(node.left)

            if node.right:

                arr.append(node.right)

            temp = arr[-1]

            arr = arr[1:]

        return temp.data

    def leafNodes(self):

        if self == None:

            return 0

        if self.left == None and self.right == None:

            return 1

        lh = rh = 0

        if self.left:

            lh = self.left.leafNodes()

        if self.right:

            rh = self.right.leafNodes()

        return lh+rh

    def fullNodes(self):

        if self == None:

            return 0

        lf = rf = 0

        if self.left:

            lf = self.left.fullNodes()

        if self.right:

            rf = self.right.fullNodes()

        if self.left and self.right:

            return lf+rf+1

        return lf+rf

    def halfNodes(self):

        if self == None:

            return 0

        lhf = rhf = 0

        if self.left:

            lhf = self.left.halfNodes()

        if self.right:

            rhf = self.right.halfNodes()

        if (self.left and self.right==None) or (self.right and self.left == None):

            return lhf+rhf+1

        return lhf+rhf

    def sum(self):

        if self == None:

            return None

        ls = rs = 0

        if self.left:

            ls = self.left.sum()

        if self.right:

            rs = self.right.sum()

        return rs+ls+self.data

    def allPaths(self, path, pathlen):

        if self == None:

            return None

        path[pathlen] = self.data

        pathlen+=1

        if self.left:

            self.left.printPaths(path, pathlen)

        if self.right:

            self.right.printPaths(path, pathlen)

        if self.right == None and self.left == None:

            arr = []

            for i in range(pathlen-1):

                print(path[i], end='->')

            print(path[pathlen-1])