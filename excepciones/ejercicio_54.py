# Ejercicio 52 Simulador de Reservas en un Hotel
#
# Desarrolla un programa que simule la reserva de habitaciones en un hotel. El programa debe permitir:
#
# Agregar una reserva (nombre del cliente, número de noches, tipo de habitación).
# Cancelar una reserva.
# Calcular el costo total de una reserva.
# Mostrar el resumen de todas las reservas.
# Salir.
# Requerimientos:
#
# Usa un diccionario para almacenar las reservas, donde las claves son los nombres de los clientes y los valores son otro diccionario con el número de noches y tipo de habitación.
# Usa comprehensions para calcular costos de reserva.
# Usa un menú estilo switch para navegar entre las opciones.
# Implementa manejo de excepciones para validar entradas numéricas y gestionar errores.

reservas = {}


def menu():
    print(
        f"1. Agregar una reserva (nombre del cliente, número de noches, tipo de habitación)."
    )
    print(f"2. Cancelar una reserva.")
    print(f"3. Calcular el costo total de una reserva.")
    print(f"4. Mostrar el resumen de todas las reservas.")
    print(f"5. Salir.")

    op = input("Introduce una opción: ")

    match op:
        case 1:
            return
        case 2:
            return
        case 3:
            return
        case 4:
            return
        case 5:
            return
        case _:
            return


menu()
