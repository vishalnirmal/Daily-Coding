##############################################
# Heap                                       #
# by Vishal Nirmal                           #
#                                            #
# A Heap ADT implementation.                 #
##############################################




class Heap:
    def __init__(self, capacity=1, heap_type='max'):     # INITIALIZING THE HEAP
        self.capacity = capacity 
        self.arr = list([0]*capacity)
        self.heap_type = heap_type.lower()
        self.count = 0
    def parent(self, i):                                 # FUNCTION TO GET THE PARENT OF NODE AT iTH POSITION.
        if i<=0 or i >= self.count:                      # CHECKING FOR POSITION OUTSIDE THE BOUND OF HEAP.
            return -1
        return (i-1)//2
    def left_child(self, i):                             # FUNCTION TO GET THE POSITION OF LEFT CHILD OF NODE AT iTH POSITION.
        left = 2*i+1                                     # FORMULA FOR GETTING THE POSITION OF LEFT CHILD.
        if left>=self.count:                             # CHECKING IF THE POSITION OF LEFT CHILD IS OUTSIDE THE BOUND OF HEAP.
            return -1
        return left
    def right_child(self, i):                            # FUNCTION TO GET THE POSITION OF RIGHT CHILD OF NODE AT iTH POSITION.
        right = 2*i+2                                    # FORMULA FOR GETTING THE POSITION OF RIGHT CHILD.
        if right>=self.count:                            # CHECKING IF THE POSITION OF RIGHT CHILD IS OUTSIDE THE BOUND OF HEAP.
            return -1
        return right
    def getMax(self):                                    # FUNCTION TO GET THE MAX VALUE FROM THE HEAP
        if self.heap_type == 'max':                      # IF THE HEAP IS MAX_HEAP THEN THE MAX VALUE WILL BE AT POSITION 0.
            mx = 0                                          
        if self.heap_type == 'min':                      # FINDING THE POSITION OF MAX VALUE IF THE HEAP_TYPE IS MIN.
            n = (self.count+1)//2                        # FORMULA FOR GETTING THE STARTING OF LEAF NODES.
            mxn = 0
            for i in range(n, self.count):               # THE MAX VALUE IN THE MIN HEAP WILL BE SURELY IN THE LEAF NODES SO 
                if self.arr[i] > mxn:                    # TRAVERSING THROUGH THE LEAVES TO FIND IT.
                    mx = i
                    mxn = self.arr[i]
        return self.arr[mx]
    def getMin(self):                                    # FUNCTION TO GET THE MIN VALUE FROM THE HEAP.
        if self.heap_type == 'min':                      # IF THE HEAP IS MIN_HEAP THEN THE MIN VALUE WILL BE AT POSITION 0.
            mn = 0
        if self.heap_type == 'max':                      # FINGDING THE POSITION OF MIN VALUE IF THE HEAP_TYPE IS MAX.
            n = (self.count+1)//2                        # FORMULA FOR GETTING THE STARTING OF LEAF NODES.
            mnn = 999999999
            for i in range(n, self.count):               # THE MIN VALUE IN THE MAX HEAP WILL BE SURELY IN THE LEAF NODES SO
                if self.arr[i] < mnn:                    # TRAVERSING THROUGH LEAF NODES TO FIND IT
                    mnn = self.arr[i]
                    mn = i
        return self.arr[mn]
    def percolateDown(self, i):                          # FUNCTION TO HEAPIFY THE HEAP.
        l = self.left_child(i)
        r = self.right_child(i)
        pos = i
        if self.heap_type == 'max':                      # HEAPIFYING DEPENDING ON THE TYPE OF HEAP.
            if l!=-1 and self.arr[l] > self.arr[i]:
                pos = l
            if r!=-1 and self.arr[r] > self.arr[pos]:
                pos = r
        else:
            if l!=-1 and self.arr[l] < self.arr[i]:
                pos = l
            if r!=-1 and self.arr[r] < self.arr[pos]:
                pos = r
        if pos != i:                                     # SWAPPING THE NODE IF NECESSARY AND CALLING THE FUNCTION AGAIN ON 
            temp = self.arr[i]                           # SWAPPED POSITION pos.
            self.arr[i] = self.arr[pos]
            self.arr[pos] = temp
            self.percolateDown(pos)
    def deleteMax(self):                                 # FUNCTION FOR RETURNING AND DELETING THE MAX NODE FROM HEAP.
        if self.count == 0:                              # CHECKING IF THE HEAP IS EMPTY OR NOT.
            return -1
        if self.heap_type == 'max':                      # IN MAX_HEAP THE MAX VALUE IS AT POSITION 0.
            mx = 0
        if self.heap_type == 'min':                      # IN MIN_HEAP THE MAX VALUE IS IN ITS LEAF NODES.
            mxn = 0
            for i in range((self.count+1)//2, self.count):
                if self.arr[i] > mxn:                    # TRAVERSING THE LEAF NODES TO FIND MAX VALUE.
                    mxn = self.arr[i]
                    mx = i
        data = self.arr[mx]                              
        self.arr[mx] = self.arr[self.count-1]            # REPLACING THE MAX VALUE WITH THE LAST LEAF IN THE HEAP.
        self.count -= 1
        self.percolateDown(mx)                           # HEAPIFYING AFTER THE CHANGES.
        return data
    def deleteMin(self):                                 # FUNCTION FOR RETURNING AND DELETING THE MIN NODE FROM HEAP.
        if self.count == 0:                              # CHECKING IF THE HEAP IS EMPTY OR NOT.
            return -1
        if self.heap_type == 'min':                      # IN MIN_HEAP THE MIN VALUE IS AT POSITION 0.
            mn = 0
        if self.heap_type == 'max':                      # IN MAX_HEAP THE MIN VALUE IS IN ITS LEAF NODES.
            mnn = 9999999999
            for i in range((self.count+1)//2, self.count):
                if mnn > self.arr[i]:                    # TRAVERSING THE LEAF NODES TO FIND MIN VALUE.
                    mnn = self.arr[i]
                    mn = i
        data = self.arr[mn]
        self.arr[mn] = self.arr[self.count-1]            # REPLACING THE MIN VALUE WITH THE LAST LEAF IN THE HEAP.
        self.count -= 1
        self.percolateDown(mn)                           # HEAPIFYING AFTER THE CHANGES.
        return data
    def resize(self):                                    # FUNCTION TO DOUBLE THE SIZE OF ARRAY WHENEVER THE ARRAY IS FULL.
        narr = list([0]*(self.capacity*2))
        for i in range(self.count):
            narr[i] = self.arr[i]
        self.capacity *= 2
        self.arr = narr
    def insert(self, data):                              # FUNCTION TO INSERT A NODE INTO THE HEAP.
        if self.count == self.capacity:                  # IF THE HEAP IS FULL...DOUBLING THE SIZE OF HEAP.
            self.resize()
        i = self.count
        self.count+=1                                    # INCREASING THE COUNT AS WE ARE ADDING A NODE.
        if self.heap_type == 'max':                      # APPLYING PERCOLATE_UP IF IT IS MAX_HEAP.
            while i>0 and data > self.arr[(i-1)//2]:
                self.arr[i] = self.arr[(i-1)//2]
                i = (i-1)//2
        else:                                            # APPLYING PERCOLATE_UP IF IT IS MIN_HEAP.
            while i>0 and data < self.arr[(i-1)//2]:
                self.arr[i] = self.arr[(i-1)//2]
                i = (i-1)//2
        self.arr[i] = data
    def buildHeap(self, arr, n):                         #FUNCTION FOR BUILDING A HEAP FROM AN ARRAY.
        while self.capacity < n:
            self.resize()
        for i in range(n):
            self.arr[i] = arr[i]
        self.count = n
        for i in range((n-1)//2, -1, -1):                # THE CONCEPT IS THAT WE JUST NEED TO HEAPIFY ALL THE NON-LEAF NODES.
            self.percolateDown(i)
    def printHeap(self):                                 # FUNCTION FOR PRINTING THE HEAP.
        for i in range(self.count):
            print(self.arr[i], end=' ')
        print()