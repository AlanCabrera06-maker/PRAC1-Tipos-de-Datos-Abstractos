import sys
sys.setrecursionlimit(20000)  # Con recursividad 

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    print("Calculando términos de Fibonacci hasta llegar a 10,000 dígitos en total...\n")

    total_digitos = 0
    n = 0
    numeros = []

    while total_digitos < 10000:
        num = fibonacci(n)
        numeros.append(num)
        total_digitos += len(str(num))
        n += 1

    print(f"Se generaron {len(numeros)} términos para alcanzar 10,000 dígitos.")
    print("Primeros 10 términos:", numeros[:10])
    print(f"Último término calculado: {numeros[-1]}")
    print(f"Cantidad total de dígitos generados: {total_digitos}")

if __name__ == "__main__":
    main()





def fibonacci(): #Sin recursividad
    a, b = 0, 1
    numeros = [a, b]
    total_digitos = len(str(a)) + len(str(b))

    while total_digitos < 10000:
        a, b = b, a + b
        numeros.append(b)
        total_digitos += len(str(b))
    
    return numeros, total_digitos

def main():
    print("Calculando términos de Fibonacci hasta alcanzar 10,000 dígitos...\n")
    
    serie, total = fibonacci_hasta_10000_digitos()

    print(f"Se generaron {len(serie)} términos para alcanzar {total} dígitos.")
    print("Primeros 10 términos:", serie[:10])
    print(f"Último término calculado: {serie[-1]}")
    print(f"El último término tiene {len(str(serie[-1]))} dígitos.")

if __name__ == "__main__":
    main()
