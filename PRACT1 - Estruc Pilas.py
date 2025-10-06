class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = []
        self.tope = 0  

    def insertar(self, valor):
        if self.tope < self.capacidad:  
            self.items.append(valor)
            self.tope += 1
            print(f"Insertar({valor}) → {self.items} (TOPE={self.tope})")
        else:
            print(f"Error: Desbordamiento al intentar insertar {valor}")

    def eliminar(self, etiqueta):
        if self.tope > 0:  
            eliminado = self.items.pop()
            self.tope -= 1
            print(f"Eliminar({etiqueta}) → se quitó {eliminado} → {self.items} (TOPE={self.tope})")
        else:
            print(f"Error: Subdesbordamiento al intentar eliminar {etiqueta}")

    def mostrar_estado(self):
        print(f"Pila actual: {self.items}, TOPE={self.tope}")



if __name__ == "__main__":
    pila = Pila(8)

    print("Pila inicialmente vacía:")
    pila.mostrar_estado()
    print()

   
    pila.insertar("X")   
    pila.insertar("Y")  
    pila.eliminar("Z")   
    pila.eliminar("T")   
    pila.eliminar("U")   
    pila.insertar("V")   
    pila.insertar("W")   
    pila.eliminar("p")  
    pila.insertar("R")   

    print("\n=== Estado final ===")
    pila.mostrar_estado()
