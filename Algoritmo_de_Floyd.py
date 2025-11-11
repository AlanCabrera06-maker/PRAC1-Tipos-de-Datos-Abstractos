def floyd_warshall(grafo):
    
    num_nodos = len(grafo)
    
   
    distancias = [[float('inf')] * num_nodos for _ in range(num_nodos)]
    
    
    for i in range(num_nodos):
        for j in range(num_nodos):
            distancias[i][j] = grafo[i][j]
            if i == j:  
                distancias[i][j] = 0
    
   
    for k in range(num_nodos):
        for i in range(num_nodos):
            for j in range(num_nodos):
                
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])
    
    return distancias


grafo = [
    [0, 3, float('inf'), 7, float('inf')],
    [8, 0, 2, float('inf'), 4],
    [5, float('inf'), 0, 1, 7],
    [2, float('inf'), float('inf'), 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 6, 0]
]

distancias_minimas = floyd_warshall(grafo)


for i in range(len(distancias_minimas)):
    print(f"Distancias desde el nodo {i}: {distancias_minimas[i]}")