# BINARY SEARCH TREE

A tree is a data structure similar to a linked list but instead of each node pointing simply to the next node in a linear fashion, each node points to a number of nodes. Tree is an example of a non-linear data structure. A tree structure is a way of representing heirarchical nature of a structure in the graphical form. Binary Search Tree is a type of tree where each node has either zero, one or two children only. It has such name because of the way an node is inserted. If the value of the data to be inserted is smaller than the current node, it is sent to the left sub-tree for repeating the same process, but if the value is greater than the current node it is sent to the right sub-tree.

Functions of BST:
* ### insert(data): 
	#### arguments:
		data: value for the node you want to add
	> Is used to add a node to the tree

* ### insertNodes(arr):
	#### arguments:
		arr: array, tupple, set or any iterable object whose data you want to add to the binary tree. The nodes are added in LEVEL ORDER manner
	> For adding all the elements of 'arr' to the tree

* ### preorder():
	> For traversing and printing the data in PREORDER manner, i.e. root, left sub-tree, right sub-tree

* ### postorder():
	> For traversing and printing the data in POSTORDER manner, i.e. left sub-tree, right sub-tree, root

* ### inorder():
	> For traversing and printing the data in INORDER manner, i.e. left sub-tree, root,  right sub-tree

* ### levelorder():
	> For traversing and printing the data in LEVEL ORDER manner, i.e. in breadth first search manner

* ### height():
	> Returns the maximum height of the tree

* ### level():
	> Returns the maximum level of the tree

* ### search(data):
	#### arguments:
		data: value that is to be searched
	> Returns boolean value for indicating the presence of the value in the binary tree

* ### size():
	> Returns the number of nodes in the tree

* ### max():
	> Returns the highest value of the tree

* ### min():
	> Returns the lowest value of the tree

* ### deepest():
	> Returns the value of the deepest node in the tree

* ### fullNodes():
	> Returns the number of full nodes (with 2 children) in the tree

* ### halfNodes():
	> Returns number of half nodes (with 1 child) in the tree

* ### leafNodes():
	> Returns number of leaf nodes (with no children) in the tree

* ### allPaths():
	> Prints the path from root to all the leaf nodes

* ### sum():
	> Returns the sum of all the nodes in the tree

* ### delete():
	> Deletes the last node entered into the tree