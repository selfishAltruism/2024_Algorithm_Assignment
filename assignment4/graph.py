import sys
from collections import defaultdict

BIG_NUM = 10**100
NULL = -1

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.key = BIG_NUM
        self.before = NULL

    def __repr__(self):
        return f"Vertex(id={self.id}, key={self.key}, before={self.before})"
    

#open file
input_sp = open(sys.argv[1],"r")
input_mst = open(sys.argv[2],"r")
output_sp = open(sys.argv[3],"w")
output_mst = open(sys.argv[4],"w")

#mst
num_vertices, num_edges, start_vertex_id = map(int, input_mst.readline().split('\t'))

graph_mst = defaultdict(list)
vertices_mst = {}

while True:
    #remove \n
    line = input_mst.readline().strip()
    if not line: 
        break
    u, v, weight = map(int, line.split('\t'))

    #because of undirected graph
    graph_mst[u].append((v, weight))
    graph_mst[v].append((u, weight))

    #add vertex
    if u not in vertices_mst:
        vertices_mst[u] = Vertex(u)
    if v not in vertices_mst:
        vertices_mst[v] = Vertex(v)




#close file
input_sp.close()
output_sp.close()
input_mst.close()
output_mst.close()