class Nodo:
    def __init__(self, dato: int):
        self.dato = dato   
        self.siguiente = None 


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None 

    def agregar(self, dato: int):
        nuevo = Nodo(dato)
        if not self.cabeza:       
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:  
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def eliminar(self, dato: int):
        actual = self.cabeza
        anterior = None

        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if not actual:
            print("Elemento no encontrado")
            return

        if not anterior:  
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente



lista = ListaEnlazada()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

print("Lista inicial:")
lista.mostrar()

print("\nEliminando el 20:")
lista.eliminar(20)
lista.mostrar()
