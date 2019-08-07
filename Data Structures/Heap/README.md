# Heap

The class Heap in heap.py implements all the basic operations of a Heap. Heap is a way of implementing the Priority Queue ADT. Priority Queue ADT is a data structure that stores value such that when we delete a value from it we will get either MAX or MIN.

Functions of Heap:

* ### insert(data): 
	#### arguments:
		data: value for the node you want to add
	> For adding a new node into the heap

* ### parent(i):
	#### arguments:
		i: position of the node
	> function to get the position of parent of a node at ith position

* ### left_child(i):
	#### arguments:
		i: position of the node
	> function to get the position of left child of a node at ith position

* ### right_child(i):
	#### arguments:
		i: position of the node
	> function to get the position of right_child of a node at ith position

* ### getMax():
	> Returns the max value from the heap

* ### getMin():
	> Returns the mix value from the heap

* ### deleteMax():
	> Returns and deletes the max value from the heap

* ### deleteMin():
	> Returns and deletes the min value from the heap

* ### resize():
	> Doubles the size of the heap

* ### printHeap():
	> Prints the data in heap in level order manner

* ### buildHeap(arr, n):
	#### arguments:
		arr: array to be converted into heap
		n: size of the array arr
	> Converting an array into heap