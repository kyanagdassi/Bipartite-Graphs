from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other Attributes as necessary'''
        self.id = key
        self.adjacent_to = []


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.adjacency_dict={}
        with open(filename, 'r') as file:
            for line in file:
                line_lst = line.split()
                vertex_1 = line_lst[0]
                vertex_2 = line_lst[1]
                self.add_vertex(vertex_1)
                self.add_vertex(vertex_2)
                self.add_edge(vertex_1, vertex_2)
        for keys, objects in self.adjacency_dict.items():
            objects.adjacent_to.sort()


    def add_vertex(self, key):
        # Should be called by init
        '''Add vertex to graph only if the vertex is not already in the graph.'''
        if key not in self.adjacency_dict:
            self.adjacency_dict[key]=Vertex(key)

    def add_edge(self, v1, v2):
        # Should be called by init
        '''v1 and v2 are vertex ID's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.adjacency_dict[v1].adjacent_to.append(v2)
        self.adjacency_dict[v2].adjacent_to.append(v1)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the ID. If ID is not in the graph, return None'''
        try:
            self.adjacency_dict[key]
        except KeyError:
            return None

    def get_vertices(self):
        '''Returns a list of ID's representing the vertices in the graph, in ascending order'''
        lst_ids = list(self.adjacency_dict.keys())
        lst_ids.sort()
        return lst_ids

    def conn_components(self): 
        '''Return a Python list of lists.  For example: if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending alphabetical order) in the connected component represented by that list.
           The overall list will also be in ascending alphabetical order based on the first item in each sublist.'''
        #This method MUST use Depth First Search logic!
        returned_list=[]
        visited_total_nodes={}
        i=0
        while len(visited_total_nodes)<len(self.adjacency_dict):
            for key in self.adjacency_dict.keys():
                if key not in visited_total_nodes:
                    start_node = key
                    break
            visited_nodes={}
            new_subtree=self.depth_first_search(start_node, visited_nodes)
            new_subtree = sorted(list(new_subtree.keys()))
            returned_list.append(new_subtree)
            visited_total_nodes.update((key, None) for key in new_subtree)
            i+=1
        returned_list=sorted(returned_list)
        return returned_list

    def depth_first_search(self, key, visited):
        stack = Stack(len(self.adjacency_dict))
        stack.push(key)
        while not stack.is_empty():
            current = stack.pop()
            visited[current]=None
            for adjacency_node in self.adjacency_dict[current].adjacent_to:
                if adjacency_node not in visited:
                    stack.push(adjacency_node)
                    visited[adjacency_node] = None
        return visited
    
    
    def is_bipartite(self):
        '''Return True if the graph is bipartite, False otherwise.'''
        #This method MUST use Breadth First Search logic!
        queue = Queue(len(self.adjacency_dict))
        vertice_color_dict={}
        visited_nodes=[]
        subgraphs = self.conn_components()
        for i in range(len(subgraphs)):
            start_node = subgraphs[i][0]
            queue.enqueue(start_node)
            vertice_color_dict[start_node]='red'
            while not queue.is_empty():
                parent=queue.dequeue()
                parent_color = vertice_color_dict[parent]
                child_color=''
                for adjacent_node in self.adjacency_dict[parent].adjacent_to:
                    visited_nodes.append(adjacent_node)
                    if parent_color == 'red':
                        child_color = 'black'
                    else:
                        child_color ='red'
                    if adjacent_node in vertice_color_dict:
                        if vertice_color_dict[adjacent_node]!=child_color:
                            return False
                            
                    else:
                        vertice_color_dict[adjacent_node]=child_color
                        queue.enqueue(adjacent_node)
        
        return True

        
