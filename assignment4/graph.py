import sys
from collections import defaultdict
import heapq

#const
INF = float('inf')

#define vertex class
class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        #setting vertex initial value
        self.key = INF
        self.before = "NIL"

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return f"Vertex(id={self.id}, key={self.key}, before={self.before})"

#implement priority queue to class
class priority_queue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}

    #maintain the heap structure
    def _heapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        #check if the left child exists and is smaller than the current element
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left

        #check if the right child exists and is smaller than the current element
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        #if the smallest element is not the current element, swap and continue heapifying
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._heapify(smallest)

    #new element is added to the heap
    def _sift_up(self, idx):
        parent = (idx - 1) // 2

        #while the element is not at the root and it is smaller than its parent, swap it with the parent
        while idx > 0 and self.heap[idx][0] < self.heap[parent][0]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    #put vertex in queue
    def add_vertex(self, vertex):
        if vertex.id in self.entry_finder:
            self.remove_vertex(vertex)
        entry = [vertex.key, vertex]
        self.entry_finder[vertex.id] = entry
        self.heap.append(entry)
        self._sift_up(len(self.heap) - 1)

    #remove vertex in queue (used at key update)
    def remove_vertex(self, vertex):
        idx = self.heap.index(self.entry_finder.pop(vertex.id))
        last_entry = self.heap.pop()
        if idx < len(self.heap):
            self.heap[idx] = last_entry
            if self.heap[idx][0] < last_entry[0]:
                self._sift_up(idx)
            else:
                self._heapify(idx)

    #pop vertex in queue
    def pop_vertex(self):
        if not self.heap:
            raise KeyError("pop from an empty priority queue")
        smallest = self.heap[0]
        self.remove_vertex(smallest[1])
        return smallest[1]

    #vertex key update
    def decrease_key(self, vertex, new_key):
        #remove vertex
        self.remove_vertex(vertex)
        vertex.key = new_key
        #add vertex
        self.add_vertex(vertex)

#floyd warshall
def floyd_warshall(graph):
    #define matrix
    n = len(graph)
    dist = [[INF] * n for _ in range(n)]
    pred = [[-1] * n for _ in range(n)]

    #set W (1st dist, pred matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            #if vertexs connect
            elif graph[i][j] != INF:
                dist[i][j] = graph[i][j]
                pred[i][j] = i

    #determine the next dist, pred matrix based on the results of the previous loop
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    for i in range(n):
        for j in range(n):
            if i != j and pred[i][j] != -1:
                pred[i][j] = pred[pred[i][j]][j]

    return dist, pred

#open file
input_sp = open(sys.argv[1],"r")
input_mst = open(sys.argv[2],"r")
output_sp = open(sys.argv[3],"w")
output_mst = open(sys.argv[4],"w")

#MST#
#set mst
line = input_mst.readline().strip()
num_vertices, num_edges, start_vertex_id = map(int, line.split())

graph_mst = defaultdict(list)
vertices_mst = {}
pq_mst = priority_queue()

#initial value settings vertex, graph
#push in priority queue
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

#implement prim algorism
for vertex_id in range(9):
    pq_mst.add_vertex(vertices_mst[vertex_id])

pq_mst.decrease_key(vertices_mst[start_vertex_id], 0)
#set start vertex
vertices_mst[start_vertex_id].key = 0

while pq_mst.heap:
    #pop target vertex from queue
    vertex = pq_mst.pop_vertex()
    #get adjacent vertex 
    for adjacent_vertex_id, weight in graph_mst[vertex.id]:
        if adjacent_vertex_id in pq_mst.entry_finder and weight < vertices_mst[adjacent_vertex_id].key:
                vertices_mst[adjacent_vertex_id].key = weight
                vertices_mst[adjacent_vertex_id].before = vertex.id
                #update vertex key in queue
                pq_mst.decrease_key(vertices_mst[adjacent_vertex_id], weight)

#write file
for vertex_id in range(9):
    output_mst.write(str(vertices_mst[vertex_id].id) + '\t' + str(vertices_mst[vertex_id].before) + '\n')


#SP#
#set sp
vertex_num_sp = int(input_sp.readline().strip())
graph = []
for _ in range(vertex_num_sp):
    row = input_sp.readline().strip().split()
    row = [float('inf') if x == 'INF' else int(x) for x in row]
    graph.append(row)

dist, pred = floyd_warshall(graph)

#write file
n = len(dist)
output_sp.write(f"D\t{n}\n")
for i in range(n):
    output_sp.write("\t".join(map(str, dist[i])) + "\n")
    
output_sp.write(f"P\t{n}\n")
for i in range(n):
    output_sp.write("\t".join(map(lambda x: 'NIL' if x == -1 else str(x + 1), pred[i])) + "\n")



#close file
input_sp.close()
output_sp.close()
input_mst.close()
output_mst.close()