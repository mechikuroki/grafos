vertex_data = ['A', 'B', 'C', 'D']

adj_mat = [
#    A  B  C  D
    [0, 1, 1, 1], # A
    [1, 0, 1, 0], # B
    [1, 1, 0, 0], # C
    [1, 0, 0, 0]  # D
]

adj_list = {'A': ['B', 'C', 'D'] ,
                  'B': ['A', 'C'],
                  'C': ['A', 'B'],
                  'D': ['A']
                  }


def printMatrix(adj_mat):
    print("\nMatriz:")
    for i in adj_mat:
        print(i)

def printConnections(adj_mat, vertices):
    print("\nConexiones por nodo:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if adj_mat[i][j]:
                print(vertices[j], end=" ")
        print()

def printList(adj_list):
    print("\nLista/conexiones por nodo:")
    for a, b in adj_list.items():
        print(f"{a} : {b}")

def switchToMatrix(adj_list):
    nodes = list(adj_list.keys())
    node_to_idx = {node: i for i, node in enumerate(nodes)}

    n = len(nodes)
    adj_mat = [[0 for _ in range(n)] for _ in range(n)]

    for source, destinations in adj_list.items():
        i = node_to_idx[source]
        for dest in destinations:
            j = node_to_idx[dest]
            adj_mat[i][j] = 1

    return adj_mat

def switchToList(adj_mat):
    num_vertices = len(adj_mat)

    #por como hice esto, después de ir de A a Z de nombres de nodos se usarían los ASCII que los sigan
    adj_list = {chr(65 + i): []  for i in range(num_vertices)}

    for source in range(num_vertices):
        for destination in range(num_vertices):
            if adj_mat[source][destination] == 1:
                adj_list[chr(65 + source)].append(chr(65 + destination))

    return adj_list


print('Nodos:',vertex_data)
print()

printList(adj_list)
print("---------------------")

printMatrix(adj_mat)
print()
printConnections(adj_mat, vertex_data)

print()
printMatrix(switchToMatrix(adj_list))
print()
printList(switchToList(adj_mat))

