def burbuja(lista):
    n = len(lista)
    print("\n--- ORDENAMIENTO POR BURBUJA ---")
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        print(f"Paso {i+1}: {lista}")
    return lista


def insercion(lista):
    print("\n--- ORDENAMIENTO POR INSERCIÓN ---")
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
        print(f"Paso {i}: {lista}")
    return lista


def seleccion(lista):
    print("\n--- ORDENAMIENTO POR SELECCIÓN ---")
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
        print(f"Paso {i+1}: {lista}")
    return lista




print("===== MÉTODOS DE ORDENAMIENTO =====")
numeros_str = input("Ingresa una lista de números separados por espacios: ")


lista = [int(x) for x in numeros_str.split()]

print("\nSelecciona el método de ordenamiento:")
print("1. Burbuja")
print("2. Inserción")
print("3. Selección")

opcion = input("Opción: ")

if opcion == "1":
    lista_ordenada = burbuja(lista)
elif opcion == "2":
    lista_ordenada = insercion(lista)
elif opcion == "3":
    lista_ordenada = seleccion(lista)
else:
    print("Opción inválida.")
    exit()

print("\nRESULTADO FINAL ORDENADO:")
print(lista_ordenada)

