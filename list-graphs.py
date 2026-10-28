vertex_data = ['A', 'B', 'C', 'D']

adjacency_list = {'A': ['B', 'C', 'D'] ,
                  'B': ['A', 'C'],
                  'C': ['A', 'B'],
                  'D': ['A']
                  }



def printList(adj_list):
    print("\nLista/conexiones por nodo:")
    for a, b in adj_list.items():
        print(f"{a} : {b}")


print('Nodos:',vertex_data)
print()
printList(adjacency_list)
