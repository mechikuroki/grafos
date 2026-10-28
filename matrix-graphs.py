vertex_data = ['A', 'B', 'C', 'D']

adjacency_matrix = [
#    A  B  C  D
    [0, 1, 1, 1], # A
    [1, 0, 1, 0], # B
    [1, 1, 0, 0], # C
    [1, 0, 0, 0]  # D
]

def printMatrix(matrix):
    print("\nMatriz:")
    for i in matrix:
        print(i)

def printConnections(matrix, vertices):
    print("\nConexiones por nodo:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:
                print(vertices[j], end=" ")
        print()

print('Nodos:',vertex_data)
printMatrix(adjacency_matrix)
print()
printConnections(adjacency_matrix, vertex_data)
