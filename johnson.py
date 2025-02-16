from collections import defaultdict
INT_MAX = float('Inf')

def Min_Distance(dist, visit):
    (minimum, Minimum_Vertex) = (INT_MAX, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and not visit[vertex]:
            (minimum, Minimum_Vertex) = (dist[vertex], vertex)
    return Minimum_Vertex

def Dijkstra_Algorithm(graph, Altered_Graph, source, output_file):
    tot_vertices = len(graph)
    sptSet = defaultdict(lambda: False)
    dist = [INT_MAX] * tot_vertices
    dist[source] = 0

    for _ in range(tot_vertices):
        curVertex = Min_Distance(dist, sptSet)
        sptSet[curVertex] = True
        for vertex in range(tot_vertices):
            if (not sptSet[vertex] and
                dist[vertex] > (dist[curVertex] + Altered_Graph[curVertex][vertex]) and
                graph[curVertex][vertex] != 0):
                dist[vertex] = dist[curVertex] + Altered_Graph[curVertex][vertex]

def BellmanFord_Algorithm(edges, graph, tot_vertices):
    dist = [INT_MAX] * (tot_vertices + 1)
    dist[tot_vertices] = 0
    for i in range(tot_vertices):
        edges.append([tot_vertices, i, 0])
    for _ in range(tot_vertices):
        for source, destn, weight in edges:
            if dist[source] != INT_MAX and dist[source] + weight < dist[destn]:
                dist[destn] = dist[source] + weight
    return dist[:tot_vertices]

def JohnsonAlgorithm(graph, output_file):
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])
    Alter_weights = BellmanFord_Algorithm(edges, graph, len(graph))
    Altered_Graph = [[INT_MAX] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                Altered_Graph[i][j] = graph[i][j] + Alter_weights[i] - Alter_weights[j]
    
    with open(output_file, 'w') as f:
        f.write('Modified Graph:\n')
        for row in Altered_Graph:
            f.write(" ".join("INF" if val == INT_MAX else str(val) for val in row) + "\n")
        f.write("\n")
    
    for source in range(len(graph)):
        Dijkstra_Algorithm(graph, Altered_Graph, source, output_file)

def read_graph_from_file(input_file):
    with open(input_file, 'r') as f:
        return [list(map(int, line.split())) for line in f.readlines()]

input_file = 'input.txt'
output_file = 'output.txt'

graph = read_graph_from_file(input_file)
JohnsonAlgorithm(graph, output_file)
