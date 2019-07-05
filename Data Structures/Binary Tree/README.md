# BINARY TREE

A tree is a data structure similar to a linked list but instead of each node pointing simply to the next node in a linear fashion, each node points to a number of nodes. Tree is an example of a non-linear data structure. A tree structure is a way of representing heirarchical nature of a structure in the graphical form. Binary Tree is a type of tree where each node has either zero, one or two children only. The class depicts operations of a binary tree.

Functions of BinaryTree:
* ### insert(data): 
	#### arguments:
		data: value for the node you want to add
	> Is used to add a node to the binary tree. The node is added in LEVEL ORDER manner

* ### insertNodes(arr):
	#### arguments:
		arr: array, tupple, set or any iterable object whose data you want to add to the binary tree. The nodes are added in LEVEL ORDER manner
	> For adding all the elements of 'arr' to the binary tree

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
	> Returns the number of nodes in the binary tree

* ### max():
	> Returns the highest value of the binary tree

* ### min():
	> Returns the lowest value of the binary tree

* ### deepest():
	> Returns the value of the deepest node in the binary tree

* ### fullNodes():
	> Returns the number of full nodes (with 2 children) in the binary tree

* ### halfNodes():
	> Returns number of half nodes (with 1 child) in the binary tree

* ### leafNodes():
	> Returns number of leaf nodes (with no children) in the binary tree

* ### allPaths():
	> Prints the path from root to all the leaf nodes

* ### sum():
	> Returns the sum of all the nodes in the binary tree

* ### delete():
	> Deletes the last node entered into the binary tree