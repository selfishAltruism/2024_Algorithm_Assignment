import sys
from collections import defaultdict
import heapq

#const
BIG_NUM = 10**100
NULL = -1

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.key = BIG_NUM
        self.before = NULL

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return f"Vertex(id={self.id}, key={self.key}, before={self.before})"


#implement priority queue
class priority_queue:
    def __init__(self):
        self.heap = []
        #mapping of tasks to entries
        self.entry_finder = {}  

    def add_vertex(self, vertex):
        if vertex.id in self.entry_finder:
            self.remove_vertex(vertex)
        entry = [vertex.key, vertex]
        self.entry_finder[vertex.id] = entry
        heapq.heappush(self.heap, entry)

    def remove_vertex(self, vertex):
        entry = self.entry_finder.pop(vertex.id)
        entry[-1] = None  # Mark as removed

    def pop_vertex(self):
        while self.heap:
            key, vertex = heapq.heappop(self.heap)
            if vertex is not None:
                del self.entry_finder[vertex.id]
                return vertex
        raise KeyError("pop from an empty priority queue")

    def decrease_key(self, vertex, new_key):
        self.remove_vertex(vertex)
        vertex.key = new_key
        self.add_vertex(vertex)

#open file
input_sp = open(sys.argv[1],"r")
input_mst = open(sys.argv[2],"r")
output_sp = open(sys.argv[3],"w")
output_mst = open(sys.argv[4],"w")

#set mst
line = input_mst.readline().strip()
num_vertices, num_edges, start_vertex_id = map(int, line.split())

graph_mst = defaultdict(list)
vertices_mst = {}

while True:
    #remove \n
    line = input_mst.readline().strip()
    if not line: 
        break
    u, v, weight = map(int, line.split())

    #because of undirected graph
    graph_mst[u].append((v, weight))
    graph_mst[v].append((u, weight))

    #add vertex
    if u not in vertices_mst:
        vertices_mst[u] = Vertex(u)
    if v not in vertices_mst:
        vertices_mst[v] = Vertex(v)

pq = priority_queue()
for vertex in vertices_mst:
    pq.add_vertex(vertex)

while True:
    try:
        vertex = pq.pop_vertex()
        print(vertex)
    except KeyError:
        break

#close file
input_sp.close()
output_sp.close()
input_mst.close()
output_mst.close()