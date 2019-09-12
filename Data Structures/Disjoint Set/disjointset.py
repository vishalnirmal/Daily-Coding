class DisjointSet:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.arr = list([0]*self.capacity)
        self.makeset()
    
    def makeset(self):
        for i in range(self.capacity):
            self.arr[i] = -1
    
    def UnionBySize(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y and x != -1:
            return
        if self.arr[y] > self.arr[x]:
            self.arr[x]+=self.arr[y]
            self.arr[y] = x
        else:
            self.arr[y] += self.arr[x]
            self.arr[x] = y
    def UnionByHeight(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y and x != -1:
            return
        if self.arr[y] > self.arr[x]:
             self.arr[y] = x
        elif self.arr[x] > self.arr[y]:
             self.arr[x] = y
        else:
            self.arr[x] = y
            self.arr[y] -= 1
    def find(self, x):
        if not(x >= 0 and x < self.capacity):
            return
        if self.arr[x] < 0:
            return x
        else:
            self.arr[x] = self.find(self.arr[x])
            return self.arr[x]

