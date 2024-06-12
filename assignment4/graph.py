import sys
from collections import defaultdict
import heapq

#const
INF = float('inf')

#class
class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.key = INF
        self.before = "NIL"

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return f"Vertex(id={self.id}, key={self.key}, before={self.before})"

#implement priority queue
class priority_queue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}

    def add_vertex(self, vertex):
        if vertex.id in self.entry_finder:
            self.remove_vertex(vertex)
        entry = [vertex.key, vertex]
        self.entry_finder[vertex.id] = entry
        heapq.heappush(self.heap, entry)

    def remove_vertex(self, vertex):
        entry = self.entry_finder.pop(vertex.id)
        entry[-1] = None
        self.__rebuild_heap()

    def __rebuild_heap(self):
        self.heap = [entry for entry in self.heap if entry[-1] is not None]
        heapq.heapify(self.heap)

    def pop_vertex(self):
        while self.heap:
            entry = heapq.heappop(self.heap)
            vertex = entry[-1]
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
vertices_mst[start_vertex_id].key = 0

while pq_mst.heap:
    vertex = pq_mst.pop_vertex()
    for adjacent_vertex_id, weight in graph_mst[vertex.id]:
        if adjacent_vertex_id in pq_mst.entry_finder and weight < vertices_mst[adjacent_vertex_id].key:
                vertices_mst[adjacent_vertex_id].key = weight
                vertices_mst[adjacent_vertex_id].before = vertex.id
                pq_mst.decrease_key(vertices_mst[adjacent_vertex_id], weight)

for vertex_id in range(9):
    output_mst.write(str(vertices_mst[vertex_id].id) + '\t' + str(vertices_mst[vertex_id].before) + '\n')


#SP#

line = input_sp.readline().strip()
num_vertices = int(line)

#initial value settings shortest-path weight matrix, predecessor matrix
D = [[[INF for _ in range(num_vertices)] for _ in range(num_vertices)] for _ in range(num_vertices)]
P = [[["NIL" for _ in range(num_vertices)] for _ in range(num_vertices)] for _ in range(num_vertices)]

#setting W
row_index = 0
while True:
    #remove \n
    line = input_sp.readline().strip()
    if not line: 
        break
    line_array = line.split()
    for col_index in range(num_vertices):
        if line_array[col_index] == 'INF': 
            D[0][row_index][col_index] = INF
        else:
            D[0][row_index][col_index] = int(line_array[col_index])

            #apply in predecessor matrix
            if int(line_array[col_index]) != 0:
                P[0][row_index][col_index] = row_index + 1

    row_index = row_index + 1



def print_3d_array(array, name):
    depth = len(array)
    rows = len(array[0])
    cols = len(array[0][0])

    for k in range(depth):
        print(f"{name}[{k}]:")
        for i in range(rows):
            print(array[k][i])
        print()  # 각 depth 구분을 위해 빈 줄 출력

# 최종 결과 출력
print_3d_array(D, "D")
print_3d_array(P, "P")



#close file
input_sp.close()
output_sp.close()
input_mst.close()
output_mst.close()