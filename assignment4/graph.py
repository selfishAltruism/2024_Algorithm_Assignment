import sys
from collections import defaultdict

#open file
input_sp = open(sys.argv[1],"r")
input_mst = open(sys.argv[2],"r")
output_sp = open(sys.argv[3],"w")
output_mst = open(sys.argv[4],"w")

#mst
num_vertices, num_edges, start_vertex_id = map(int, input_mst.readline().split('\t'))

graph = defaultdict(list)

while True:
    #remove \n
    line = input_mst.readline().strip()
    if not line: 
        break
    u, v, weight = map(int, line.split('\t'))

    #because of undirected graph
    graph[u].append((v, weight))
    graph[v].append((u, weight))


#close file
input_sp.close()
output_sp.close()
input_mst.close()
output_mst.close()