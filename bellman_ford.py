from typing import List

def bellman_ford(edges: List[tuple], src: int) -> List[int]:
    inf = float('inf')
    if not edges: return []

    # número de vértices é o maior valor de u ou v + 1
    V = max(max(u, v) for u, v, _ in edges) + 1
    dist = [inf] * V
    dist[src] = 0

    # relaxamento das arestas
    for _ in range(V - 1):
        updated = False
        for u, v, weight in edges:
            if dist[u] != inf and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                updated = True
            # para grafo não-direcionado
            if dist[v] != inf and dist[v] + weight < dist[u]:
                dist[u] = dist[v] + weight
                updated = True
        if not updated: break

    # verifica se tem ciclo negativo
    for u, v, weight in edges:
        if dist[u] != inf and dist[u] + weight < dist[v]:
            return [-1]

    return dist

# leitura é possível com/sem separação dos elementos por vírgula
def matrizAdjacencia(arquivo):
    matriz = [[int(num.split(',')[0]) for num in line.split()] for line in arquivo]
    arestas = []
    num_vertices = len(matriz)

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if matriz[i][j] != 0:
                arestas.append((i, j, matriz[i][j]))

    return arestas

def matrizIncidencia(arquivo):
    matriz = [[int(num.split(',')[0]) for num in line.split()] for line in arquivo]
    arestas = []

    num_vertices = len(matriz)
    num_arestas = len(matriz[0])

    for j in range(num_arestas):
        origem = -1
        destino = -1
        peso = 1

        for i in range(num_vertices):
            if matriz[i][j] != 0:
                if origem == -1:
                    origem = i
                    peso = matriz[i][j]
                else:
                    destino = i
                    break

        if origem != -1 and destino != -1:
            arestas.append((origem, destino, peso))

    return arestas

# TODO: Implementar
def listaAdjacencia(arquivo):
    return []

# TODO: Implementar
def listaIncidencia(arquivo):
    return []

def main():
    try:
        # TODO: permitir escolha do tipo de grafo (orientado ou não-orientado)
        opc = int(input("""Qual o formato de representação do grafo?
[1] Matriz de adjacência
[2] Matriz de incidência
[3] Lista de adjacência
[4] Lista de incidência
[0] Sair
:"""))

        while opc not in range(5):
            opc = int(input("Opção inválida. Digite novamente: "))

        if opc == 0:
            print("Programa encerrado.")
            return
        
        arquivo = input("Digite o nome do arquivo para leitura do grafo: ")

        ler = [matrizAdjacencia, matrizIncidencia, listaAdjacencia, listaIncidencia]

        with open(arquivo, 'r') as file:
            G = ler[opc - 1](file)

        if len(G) == 0:
            print("Grafo está vazio.")
            return
        
        print("Grafo lido:", G)

        org = int(input("Digite o vértice de origem: "))

        while org not in range(len(G)):
            org = int(input("Vértice inválido. Digite novamente: "))

        result = bellman_ford(G, org)

        print(f"Lista de distâncias: {result if result != [-1] else 'Ciclo negativo detectado'}")

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except ValueError:
        print("Erro: Entrada inválida, foram encontrados valores inesperados no grafo.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
