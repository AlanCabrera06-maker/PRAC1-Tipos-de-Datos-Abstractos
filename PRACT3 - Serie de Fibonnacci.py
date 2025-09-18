def fibonacci(n):

    serie = [0, 1]
    for _ in range(2, n):
        serie.append(serie[-1] + serie[-2])
    return serie

def main():
    n = 10000 
    print(f"Calculando los primeros {n} números de Fibonacci...")

    serie = fibonacci(n)

    print("\nPrimeros 10 términos:")
    print(serie[:10])

    print(f"\nTérmino {n}:")
    print(f"{serie[-1]}")
    print(f"Este número tiene {len(str(serie[-1]))} dígitos.")

if __name__ == "__main__":
    main()
