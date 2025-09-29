class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):

        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        if self.es_vacia():
            print("La pila está vacía.")
        else:
            print("Contenido de la pila (tope → base):")
            for elem in reversed(self.items):
                print(f"| {elem} |")


if __name__ == "__main__":
    pila = Pila()

    while True:
        print("\n=== MENÚ DE PILAS ===")
        print("1. Apilar elemento")
        print("2. Desapilar elemento")
        print("3. Verificar si está vacía")
        print("4. Mostrar pila")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            valor = input("Ingresa el valor a apilar: ")
            pila.apilar(valor)
            print(f"Elemento '{valor}' apilado correctamente.")

        elif opcion == "2":
            try:
                elem = pila.desapilar()
                print(f"Elemento desapilado: {elem}")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            if pila.es_vacia():
                print("La pila está vacía.")
            else:
                print("La pila NO está vacía.")

        elif opcion == "4":
            pila.mostrar()

        elif opcion == "5":
            print("¡Saliendo del programa!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")