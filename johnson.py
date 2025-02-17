from bellman_ford_aux import BellmanFord_Algorithm
from dijkstra_aux import Dijkstra_Algorithm

INT_MAX = float('Inf')

def JohnsonAlgorithm(graph, output_file):
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])  # Constrói a lista de arestas do grafo
    
    Alter_weights = BellmanFord_Algorithm(edges, graph, len(graph))  # Obtém os pesos alterados

    if Alter_weights == [-1]:
        print('O grafo tem ciclo negativo\n')
        return
    
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
    
    with open(output_file, 'w') as f:
        f.write('Matrix Final:\n')
        for row in shortest_paths:
            f.write(" ".join("INF" if val == INT_MAX else str(val) for val in row) + "\n")

    return Altered_Graph

def read_graph_from_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        nomes = f.readline().split(', ')
        return nomes, [list(map(int, line.split())) for line in f.readlines()]

input_file = input("Digite o nome do arquivo de entrada: ")
output_file = 'output.txt'
graphviz_file = 'graphviz.txt'

nomes, graph = read_graph_from_file(input_file)
graph = JohnsonAlgorithm(graph, output_file)

if graph is None:
    exit()

# Gera o código para o graphviz
with open(graphviz_file, 'w', encoding='utf-8') as f:
    f.write('digraph G {\n')
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                f.write(f'"{nomes[i]}" -> "{nomes[j]}" [label="{graph[i][j]}"];\n')
    f.write('}')

print("Saída gravada em graphviz.txt e output.txt\n")
