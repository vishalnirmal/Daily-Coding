# Graph

A graph is a data structure which represents objects and connection between the objects. A graph is a pair (V, E), where V is the set of vertices and E is set of edges connecting the vertices. Graphs are used in various application such as representing connection between components in electronic circuit, transportation networks, computer networks, representing ER diagrams in databases etc.

Functions of Graph:

* ### add_edge(edge): 
	#### arguments:
		edge: a tupple which has the value of node connecting each other
	> For adding an edge in the graph

* ### add_edges(edges):
	#### arguments:
		edges: a list containg tupple which has the value of node connecting each other
	> For adding multiple edges in the graph

* ### add_node(node):
	#### arguments:
		node: name of node to be added
	> For adding the node to the graph

* ### add_nodes(nodes):
	#### arguments:
		nodes: list of nodes to be added
	> For adding the multiple nodes to the graph

* ### delete_node(node):
	#### arguments:
		node: name of node to be deleted
	> For deleting a node from the graph

* ### indegree(node):
	#### arguments:
		node: name of a node
	> For getting indegree of a node

* ### outdegree(node):
	#### arguments:
		node: name of a node
	> For getting outdegree of a node

* ### neighbors(node):
	#### arguments:
		node: name of a node
	> For getting all neighbors of a node

* ### bfs():
	> For applying Breadth First Search on the graph

* ### dfs():
	> For applying Depth First Search on the graph

* ### topological_sort():
	> For applying topological sort on the graph

* ### shortest_path(node):
	#### argments:
		node: name of the node
	> To get shortest path from a node to all nodes

* ### has_cycle():
	> Returns a boolean value depending whether the graph contains cycle