def warshall(grafo):
   
    num_nodos = len(grafo)
    
    
    alcanzabilidad = [[grafo[i][j] for j in range(num_nodos)] for i in range(num_nodos)]
    
    
    for k in range(num_nodos):
        for i in range(num_nodos):
            for j in range(num_nodos):
                
                alcanzabilidad[i][j] = alcanzabilidad[i][j] or (alcanzabilidad[i][k] and alcanzabilidad[k][j])
    
    return alcanzabilidad

grafo = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

matriz_alcanzabilidad = warshall(grafo)

for i in range(len(matriz_alcanzabilidad)):
    print(f"Alcanzabilidad desde el nodo {i}: {matriz_alcanzabilidad[i]}")