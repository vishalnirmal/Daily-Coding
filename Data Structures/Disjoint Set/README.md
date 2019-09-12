# DISJOINT SET

A disjoint-set data structure is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets

Functions of DLL:
* ### makeset(): 
	> Used to create an array with default value -1

* ### UnionBySize(x, y): 
	#### arguments:
		x, y: a value on which union operation is to be performed
	> Merging the two sets x and y by size

* ### UnionByHeight(x, y): 
	#### arguments:
		x, y: a value on which union operation is to be performed
	> Merging the two sets x and y by height

* ### find(x):
	#### arguments:
		x: value whose set you want to find
	> Finding the set of x