import random
import collections
import time

class ColaCircular:
    """Implementación sencilla de cola circular con capacidad fija."""
    def __init__(self, capacidad):
        assert capacidad > 0
        self.capacidad = capacidad
        self.buffer = [None] * capacidad
        self.head = 0
        self.tail = 0
        self.size = 0

    def encolar(self, item):
        """Intenta encolar. Devuelve True si tuvo éxito, False si está llena."""
        if self.size == self.capacidad:
            return False
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacidad
        self.size += 1
        return True

    def desencolar(self):
        """Desencola y devuelve el elemento; devuelve None si está vacía."""
        if self.size == 0:
            return None
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacidad
        self.size -= 1
        return item

    def esta_llena(self):
        return self.size == self.capacidad

    def esta_vacia(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def elementos(self):
        """Devuelve lista de elementos de frente a fondo (visualización)."""
        elems = []
        idx = self.head
        for _ in range(self.size):
            elems.append(self.buffer[idx])
            idx = (idx + 1) % self.capacidad
        return elems

    def __repr__(self):
        return f"Cola({self.elementos()})"


class Peaje:
    """Contiene N colas circulares (carriles) y una cola de espera FIFO."""
    def __init__(self, n_carriles, capacidad_por_carril):
        assert n_carriles >= 1
        self.carriles = [ColaCircular(capacidad_por_carril) for _ in range(n_carriles)]
        self.espera = collections.deque()   # vehículos esperando si no hay espacio

    def asignar_vehiculo(self, vehiculo):
        """
        Asigna 'vehiculo' al carril con menos vehículos. 
        Si todos están llenos, lo coloca en la cola de espera.
        """
        # Buscar el carril con menor tamaño; en empate, el índice más bajo
        min_len = min(len(c) for c in self.carriles)
        if min_len == self.carriles[0].capacidad and all(c.esta_llena() for c in self.carriles):
            # todos llenos -> espera
            self.espera.append(vehiculo)
            return False, "espera"
        # elegir primer carril con tamaño == min_len que no esté lleno
        for idx, cola in enumerate(self.carriles):
            if len(cola) == min_len and not cola.esta_llena():
                cola.encolar(vehiculo)
                return True, idx
        # fallback: si ninguno por alguna razón pudo recibir, ir a espera
        self.espera.append(vehiculo)
        return False, "espera"

    def intentar_asignar_espera(self):
        """Después de salidas, intentar mover vehículos de la espera a carriles libres."""
        asignados = 0
        while self.espera:
            veh = self.espera[0]  # mirar primero en espera
            # buscar carril con menos vehículos
            min_len = min(len(c) for c in self.carriles)
            # si todos llenos -> no hay más asignaciones
            if all(c.esta_llena() for c in self.carriles):
                break
            # asignar al primer carril con len == min_len y no lleno
            for cola in self.carriles:
                if len(cola) == min_len and not cola.esta_llena():
                    cola.encolar(veh)
                    self.espera.popleft()
                    asignados += 1
                    break
        return asignados

    def procesar_salidas(self, prob_salida):
        """
        Para cada carril, con probabilidad prob_salida (0..1) se desapila un vehículo (si existe).
        Devuelve lista de (indice_carril, vehiculo_salido) para cada salida.
        """
        salidas = []
        for idx, cola in enumerate(self.carriles):
            if not cola.esta_vacia() and random.random() < prob_salida:
                veh = cola.desencolar()
                salidas.append((idx, veh))
        # después de salidas, intentar mover de la espera (FIFO)
        asignados = self.intentar_asignar_espera()
        return salidas, asignados

    def estado(self):
        """Devuelve una representación del estado actual para imprimir."""
        estado = []
        for idx, cola in enumerate(self.carriles, start=1):
            estado.append((idx, list(cola.elementos())))
        espera_list = list(self.espera)
        return estado, espera_list

    def __repr__(self):
        s = []
        for i, c in enumerate(self.carriles, start=1):
            s.append(f"Carril {i}: {c.elementos()}")
        s.append(f"Espera: {list(self.espera)}")
        return "\n".join(s)


def simular(n_carriles=3, capacidad=4, timesteps=20, p_llegada=0.6, p_salida=0.4, max_intentos_por_tiempo=2, seed=None, sleep_per_step=0.0):
    """
    Simula el peaje:
      - n_carriles: número de carriles
      - capacidad: capacidad por carril (cola circular)
      - timesteps: cuantos pasos de tiempo simular
      - p_llegada: probabilidad de generar un vehículo en cada intento de llegada
      - p_salida: probabilidad de que en un carril salga un vehículo en cada timestep
      - max_intentos_por_tiempo: hasta cuántas llegadas se intentan por timestep (puede ser 0,1,2,...)
      - seed: semilla para reproducibilidad
      - sleep_per_step: segundos a esperar entre pasos (0 para ejecutar rápido)
    """
    if seed is not None:
        random.seed(seed)

    peaje = Peaje(n_carriles, capacidad)
    veh_id = 1

    print(f"Simulación: {n_carriles} carriles, capacidad {capacidad} cada uno, {timesteps} pasos")
    print("-" * 60)

    for t in range(1, timesteps + 1):
        print(f"Tiempo t={t}")

        # 1) Generar llegadas: hasta max_intentos_por_tiempo intentos, cada uno con prob p_llegada
        llegadas = 0
        for attempt in range(max_intentos_por_tiempo):
            if random.random() < p_llegada:
                label = f"A{veh_id}"
                veh_id += 1
                llegadas += 1
                ok, info = peaje.asignar_vehiculo(label)
                if ok:
                    print(f"  Llegada: {label} -> asignado al carril {info + 1}")
                else:
                    print(f"  Llegada: {label} -> puesto en espera (todos ocupados)")
        if llegadas == 0:
            print("  (No hubo nuevas llegadas)")

        # 2) Procesar salidas
        salidas, asignados_espera = peaje.procesar_salidas(p_salida)
        if salidas:
            for idx, veh in salidas:
                print(f"  Salida: {veh} salió del carril {idx + 1}")
        else:
            print("  (No hubo salidas este paso)")

        if asignados_espera:
            print(f"  {asignados_espera} vehículo(s) de la cola de espera fueron asignados a carriles tras salidas")

        # 3) Mostrar estado
        estado, espera = peaje.estado()
        for idx, elems in estado:
            print(f"  Carril {idx}: {elems} (ocupado {len(elems)}/{capacidad})")
        print(f"  Espera: {espera}")
        print("-" * 60)

        if sleep_per_step > 0:
            time.sleep(sleep_per_step)

    print("Simulación finalizada.")
    print(peaje)  # resumen final


if __name__ == "__main__":
    # Parámetros por defecto — puedes modificarlos aquí o llamar simular(...) con otros valores
    simular(
        n_carriles=3,
        capacidad=4,
        timesteps=25,
        p_llegada=0.7,      # probabilidad de llegada por intento
        p_salida=0.45,      # probabilidad de salida por carril
        max_intentos_por_tiempo=2,
        seed=42,            # semilla para reproducibilidad
        sleep_per_step=0.0  # poner >0.0 para ver paso a paso pausado
    )
