##############################################
# Binary Tree                                #
# by Vishal Nirmal                           #
#                                            #
# A Binary Tree ADT implementation.          #
##############################################




class BinaryTree:

    def __init__(self, data=None):

        self.data = data

        self.left = None

        self.right = None

    def insert(self, data):

        if self.data != None:

            arr = [self]

            while len(arr) > 0:

                node = arr[0]

                if node.left:

                    arr.append(node.left)

                else:

                    node.left = BinaryTree(data)

                    break

                if node.right:

                    arr.append(node.right)

                else:

                    node.right = BinaryTree(data)

                    break

                arr = arr[1:]

        else:

            self.data = data

    def insertNodes(self, arr):

        for i in arr:

            self.insert(i)

    def preorder(self):

        print(self.data, end=' ')

        if self.left:

            self.left.preorder()

        if self.right:

            self.right.preorder()

    def inorder(self):

        if self.left:

            self.left.inorder()

        print(self.data, end=' ')

        if self.right:

            self.right.inorder()

    def postorder(self):

        if self.left:

            self.left.postorder()

        if self.right:

            self.right.postorder()

        print(self.data, end=' ')

    def levelorder(self):

        arr = [self]

        while len(arr):

            node = arr[0]

            print(node.data, end=' ')

            if node.left:

                arr.append(node.left)

            if node.right:

                arr.append(node.right)

            arr = arr[1:]

    def height(self):

        if self.left == None or self.right==None:

            return 0

        lh = self.left.height()

        rh = self.right.height()

        return max(lh, rh)+1

    def level(self):

        if self.left == None or self.right==None:

            return 0

        lh = self.left.level()

        rh = self.right.level()

        return max(lh, rh)+1

    def search(self, data):

        if self == None:

            return False

        if self.data == data:

            return True

        if self.left and self.left.search(data) == True:

            return True

        if self.right:

            return self.right.search(data)

    def size(self):

        if self == None:

            return 0

        ls = rs = 0

        if self.left:

            ls = self.left.size()

        if self.right:

            rs = self.right.size()

        return ls + rs + 1

    def max(self):

        if self == None:

            return 0

        lmx = rmx = 0

        if self.left:

            lmx = self.left.max()

        if self.right:

            rmx = self.right.max()

        return max(lmx, rmx, self.data)

    def min(self):

        if self == None:

            return 0

        lmn = rmn = 0

        if self.left:

            lmn = self.left.min()

        if self.right:

            rmn = self.right.min()

        return min(lmn, rmn, self.data)

    def deepest(self):

        if self==None:

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

        if self.left == None and self.right == None:

            return 1

        lln = rln = 0

        if self.left:

            lln = self.left.leafNodes()

        if self.right:

            rln = self.right.leafNodes()

        return lln + rln

    def fullNodes(self):

        if self==None:

            return 0

        arr = [self]

        count = 0

        while len(arr):

            node = arr[0]

            if node.left:

                arr.append(node.left)

            if node.right:

                arr.append(node.right)

            if node.left and node.right:

                count+=1

            arr = arr[1:]

        return count

    def halfNodes(self):

        if self==None:

            return 0

        arr = [self]

        count = 0

        while len(arr):

            node = arr[0]

            if node.left:

                arr.append(node.left)

            if node.right:

                arr.append(node.right)

            if (node.left==None and node.right) or (node.left and node.right==None):

                count+=1

            arr = arr[1:]

        return count

    def allPaths(self, path=[0]*1000, pathlen=0):

        if self == None:

            return

        path[pathlen] = self.data

        pathlen+=1

        if self.left == None and self.right == None:

            for i in range(pathlen-1):

                print(path[i], end='->')

            print(path[pathlen])

            return

        if self.left:

            self.left.allPaths(path, pathlen)

        if self.right:

            self.right.allPaths(path, pathlen)
        
    def sum(self):

        if self == None:

            return 0

        ls = rs = 0

        if self.left:

            ls = self.left.sum()

        if self.right:

            rs = self.right.sum()

        return self.data+ls+rs

    def delete(self):

        arr = [self]

        while len(arr):

            node = arr[0]

            if node.left:

                arr.append(node.left)

            if node.right:

                arr.append(node.right)

            temp = arr[-1]

            arr = arr[1:]

        temp = None