from collections import defaultdict
INT_MAX = float('Inf')

# Função para encontrar o vértice com a menor distância ainda não visitado
def Min_Distance(dist, visit):
    (minimum, Minimum_Vertex) = (INT_MAX, 0)
    for vertex in range(len(dist)):
        if minimum > dist[vertex] and not visit[vertex]:
            (minimum, Minimum_Vertex) = (dist[vertex], vertex)
    return Minimum_Vertex

# Implementação do algoritmo de Dijkstra para encontrar os menores caminhos
def Dijkstra_Algorithm(graph, Altered_Graph, source, output_file, shortest_paths):
    tot_vertices = len(graph)
    sptSet = defaultdict(lambda: False)  # Conjunto de vértices incluídos no caminho mais curto
    dist = [INT_MAX] * tot_vertices  # Inicializa todas as distâncias como infinito
    dist[source] = 0  # A distância da fonte para ela mesma é 0

    for _ in range(tot_vertices):
        curVertex = Min_Distance(dist, sptSet)  # Encontra o vértice com menor distância
        sptSet[curVertex] = True  # Marca o vértice como visitado
        for vertex in range(tot_vertices):
            if (not sptSet[vertex] and  # Se ainda não foi visitado
                Altered_Graph[curVertex][vertex] != INT_MAX and  # Se há um caminho válido
                dist[curVertex] != INT_MAX and  # Se a distância não é infinita
                dist[vertex] > (dist[curVertex] + Altered_Graph[curVertex][vertex])):  # Se encontrou um caminho menor
                dist[vertex] = dist[curVertex] + Altered_Graph[curVertex][vertex]
    
    shortest_paths.append(dist)  # Adiciona o vetor de distâncias à matriz de caminhos mais curtos

# Algoritmo de Bellman-Ford para calcular as modificações de peso para Johnson
def BellmanFord_Algorithm(edges, graph, tot_vertices):
    dist = [INT_MAX] * (tot_vertices + 1)
    dist[tot_vertices] = 0  # Define a distância da fonte fictícia como 0
    for i in range(tot_vertices):
        edges.append([tot_vertices, i, 0])  # Adiciona arestas fictícias com peso 0
    for _ in range(tot_vertices + 1):  # Executa o algoritmo para detectar possíveis ciclos negativos
        for source, destn, weight in edges:
            if dist[source] != INT_MAX and dist[source] + weight < dist[destn]:
                dist[destn] = dist[source] + weight
    return dist[:tot_vertices]  # Retorna os pesos alterados para os vértices originais

# Implementação do algoritmo de Johnson para encontrar caminhos mais curtos entre todos os pares
def JohnsonAlgorithm(graph, output_file):
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])  # Constrói a lista de arestas do grafo
    
    Alter_weights = BellmanFord_Algorithm(edges, graph, len(graph))  # Obtém os pesos alterados
    
    # Inicializa a matriz alterada com valores infinitos
    Altered_Graph = [[INT_MAX] * len(graph) for _ in range(len(graph))]
    
    for i in range(len(graph)):
        Altered_Graph[i][i] = 0  # Define a diagonal principal como zero
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                Altered_Graph[i][j] = graph[i][j] + Alter_weights[i] - Alter_weights[j]  # Ajusta os pesos
    
    shortest_paths = []  # Matriz para armazenar os menores caminhos
    for source in range(len(graph)):
        Dijkstra_Algorithm(graph, Altered_Graph, source, output_file, shortest_paths)  # Executa Dijkstra para cada fonte
    
    # Escreve a matriz final de menores caminhos no arquivo de saída
    with open(output_file, 'w') as f:
        f.write('Shortest Matrix:\n')
        for row in shortest_paths:
            f.write(" ".join("INF" if val == INT_MAX else str(val) for val in row) + "\n")

# Função para ler um grafo de um arquivo de entrada
def read_graph_from_file(input_file):
    with open(input_file, 'r') as f:
        return [list(map(int, line.split())) for line in f.readlines()]

# Definição dos arquivos de entrada e saída
input_file = 'input.txt'
output_file = 'output.txt'

# Lê o grafo do arquivo e executa o algoritmo de Johnson
graph = read_graph_from_file(input_file)
JohnsonAlgorithm(graph, output_file)
