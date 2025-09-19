import random

class SistemaAcademico:
    def __init__(self):
        self.calificaciones = [
            [random.randint(50, 100) for _ in range(6)]
            for _ in range(500)
        ]
    
    def asignar_calificacion(self, alumno_id, materia_id, calificacion):
        if 0 <= alumno_id < 500 and 0 <= materia_id < 6:
            self.calificaciones[alumno_id][materia_id] = calificacion
            return True
        return False
    
    def buscar_alumno_materia(self, alumno_id, materia_id):
        if 0 <= alumno_id < 500 and 0 <= materia_id < 6:
            calificacion = self.calificaciones[alumno_id][materia_id]
            return {
                'alumno_id': alumno_id,
                'materia_id': materia_id,
                'calificacion': calificacion,
                'existe': True
            }
        return {'error': 'Índices fuera de rango'}
    
    def mostrar_tabla_completa(self):
    
        print("\n=== TABLA COMPLETA DE CALIFICACIONES ===")
        print("Alumno\tM1\tM2\tM3\tM4\tM5\tM6")
        for i, fila in enumerate(self.calificaciones, start=1):
            print(f"{i}\t" + "\t".join(f"{x:5.1f}" for x in fila))

def main():
    sistema = SistemaAcademico()

    while True:
        print("\n" + "="*60)
        print("MENÚ DEL SISTEMA ACADÉMICO")
        print("1. Consultar calificación de un alumno en una materia")
        print("2. Mostrar toda la tabla de calificaciones (500 x 6)")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            alumno = int(input("Número de alumno (1 a 500): ")) - 1
            materia = int(input("Número de materia (1 a 6): ")) - 1
            resultado = sistema.buscar_alumno_materia(alumno, materia)
            if 'error' in resultado:
                print("Error:", resultado['error'])
            else:
                print(f"\nAlumno {resultado['alumno_id']+1}, "
                      f"Materia {resultado['materia_id']+1}: "
                      f"{resultado['calificacion']}")
        elif opcion == "2":
            sistema.mostrar_tabla_completa()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
