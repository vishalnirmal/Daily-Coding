##############################################
# Graph                                      #
# by Vishal Nirmal                           #
#                                            #
# A Graph ADT implementation.                #
##############################################





class Graph:

    def __init__(self):

        self.adj_list = {}

        self.nodes = []

        self.edges = []

    def add_edge(self, edge):

        i, j = edge

        self.add_nodes([i, j])

        if edge not in self.edges:

            self.edges.append(edge)

            self.adj_list[i].append(j)

    def add_edges(self, edges):

        for i in edges:

            self.add_edge(i)

    def add_node(self, node):

        if node not in self.nodes:

            self.nodes.append(node)

            self.adj_list[node] = []

    def add_nodes(self, nodes):

        for i in nodes:

            self.add_node(i)

    def delete_node(self, node):

        if node not in self.nodes:

            return 

        for i in self.nodes:

            if (i, node) in self.edges:

                self.edges.remove((i, node))

            if  (node, i) in self.edges:

                self.edges.remove((node, i))

        for i in self.adj_list.keys():

            if node in self.adj_list[i]:

                self.adj_list[i].remove(node)

        self.nodes.remove(node)

        self.adj_list.pop(node)

    def outdegree(self, node):

        if node in self.nodes:

            return len(self.adj_list[node])

        return -1

    def indegree(self, node):

        if node in self.nodes:

            count = 0

            for i, j in self.edges:

                if j == node:

                    count+=1

            return count

        return -1

    def neighbors(self, node):

        if node in self.nodes:

            return self.adj_list[node]

    def bfs(self, node):

        arr = [node]

        visited = [node]

        while len(arr):

            n = arr[0]

            print(n, end= ' ')

            for i in self.adj_list[n]:

                if i not in visited:

                    arr.append(i)

                    visited.append(i)

            arr.remove(n)

    

    def dfs(self, node):

        arr = [node]

        visited = []

        self.dfs_util(node, visited)

    

    def dfs_util(self, node, visited):

        visited.append(node)

        print(node, end=' ')

        for i in self.adj_list[node]:

            if i not in visited:

                self.dfs_util(i, visited)

    

    def topological_sort(self):

        queue = []

        indegree = {}

        outdegree = {}

        result = []

        for i in self.nodes:

            indegree[i] = self.indegree(i)        

        for v in self.nodes:

            if self.indegree(v) == 0:

                queue.append(v)

        while len(queue):

            node = queue[0]

            result.append(node)

            for i in self.adj_list[node]:

                if indegree[i] - 1 == 0:

                    queue.append(i)

                indegree[i] -= 1

            queue.remove(node)

        return result

    def shortest_path(self, node):

        table = {}

        paths = {}

        for i in self.nodes:

            table[i] = {'distance': 99999999, 'pnode': None}

            paths[i] = ''

        table[node]['distance'] = 0

        arr = [node]

        while len(arr):

            n = arr[0]

            for i in self.adj_list[n]:

                if table[i]['distance'] > table[n]['distance'] + 1:

                    arr.append(i)

                    table[i]['distance'] = table[n]['distance'] + 1

                    table[i]['pnode'] = n

            arr.remove(n)

        for i in self.nodes:

            if i != node:

                n = i

                if table[i]['distance'] < 10:

                    paths[i] = str(n)+paths[i]

                    while n!=node:

                        n = table[n]['pnode']

                        paths[i] = str(n)+'-'+paths[i]

        return paths

    def has_cycle(self):

        visited = []

        rec_stack = []

        for i in self.nodes:

            if self.has_cycle_util(i, visited, rec_stack):

                return True

        return False

    def has_cycle_util(self, node, visited, rec_stack):

        visited.append(node)

        rec_stack.append(node)

        for i in self.adj_list[node]:

            if i not in visited:

                if self.has_cycle_util(i, visited, rec_stack):

                    return True

            if i in rec_stack:

                return True

        rec_stack.remove(node)

        return False

            