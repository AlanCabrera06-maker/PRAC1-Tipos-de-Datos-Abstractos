
def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

entrada = input("Ingrese una lista de palabras separadas por espacios: ")
palabras = entrada.split() 

palindromas = [p for p in palabras if es_palindromo(p)]

print("\nPalabras ingresadas:", palabras)
if palindromas:
    print("Palíndromas encontradas:", palindromas)
else:
    print("No se encontraron palíndromas.")
