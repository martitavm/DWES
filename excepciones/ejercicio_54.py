# Desarrolla un programa que simule la reserva de habitaciones en un hotel. El programa debe permitir:

# Agregar una reserva (nombre del cliente, número de noches, tipo de habitación).
# Cancelar una reserva.
# Calcular el costo total de una reserva.
# Mostrar el resumen de todas las reservas.
# Salir.
# Requerimientos:

# Usa un diccionario para almacenar las reservas, donde las claves son los nombres de los clientes y los valores son otro diccionario con el número de noches y tipo de habitación.
# Usa comprehensions para calcular costos de reserva.
# Usa un menú estilo switch para navegar entre las opciones.
# Implementa manejo de excepciones para validar entradas numéricas y gestionar errores.


def menu_opciones():
    print("M E N Ú   D E   O P C I O N E S")
    print("---------------------------------")
    print("1. Agregar reserva.")
    print("2. Cancelar reserva.")
    print("3. Calcular coste total de una reserva.")
    print("4. Mostrar el resumen de todas las reservas.")
    print("5. Salir.")
    opcion = 0
    while opcion != 5:
        try:
            opcion = int(input("\nElige una opcion: "))
            print(switch(opcion))
        except ValueError:
            print("Introduce una opción válida.")


reservas = {}


def switch(opcion):
    match opcion:
        case 1:
            print("Has elegido 'Agregar reserva'.")
            return agregar_reserva()
        case 2:
            print("Has elegido 'Cancelar reserva'.")
            return cancelar_reserva()
        case 3:
            print("Has elegido 'Calcular coste total de una reserva'.")
            return calcular_coste()
        case 4:
            print("Has elegido 'Mostrar resumen de todas las reservas'.")
            return mostrar_resumen()
        case 5:
            return "Has salido de la aplicación"
        case _:
            return "Opción inválida."


def agregar_reserva():
    nombre = input("Nombre del cliente: ").strip().lower()
    try:
        noches = int(input("Número de noches: "))
        tipo_habitacion = (
            input("Tipo de habitación (simple, doble, suite): ").strip().lower()
        )
        if tipo_habitacion not in ["simple", "doble", "suite"]:
            return "Tipo de habitación no válido."
        if nombre not in reservas:
            reservas[nombre] = {"noches": noches, "tipo": tipo_habitacion}
            return f"Reserva agregada para {nombre}: {noches} noches en habitación {tipo_habitacion}."
        else:
            return "Ya existe una persona con ese nombre en las reservas."
    except ValueError:
        return "Por favor, introduce un número válido para el número de noches."


def cancelar_reserva():
    nombre = input("Nombre del cliente: ").strip().lower()
    try:
        del reservas[nombre]
        return f"Reserva cancelada para {nombre}."
    except KeyError:
        return "No se encontró una reserva para este cliente."


def calcular_coste():
    nombre = input("Nombre del cliente: ").strip().lower()
    if nombre in reservas:
        noches = reservas[nombre]["noches"]
        tipo = reservas[nombre]["tipo"]
        precio_por_noche = {"simple": 50, "doble": 75, "suite": 100}
        try:
            coste_total = noches * precio_por_noche[tipo]
            return f"El coste total de la reserva para {nombre} es: {coste_total}€."
        except KeyError:
            return "No hay tarifa para ese tipo de habitación."
    else:
        return "No se encontró una reserva para este cliente."


def mostrar_resumen():
    if not reservas:
        return "No hay reservas en el sistema."

    resumen = "\nResumen de todas las reservas:\n"
    for cliente, datos in reservas.items():
        resumen += (
            f"-> Cliente: {cliente}, Noches: {datos['noches']}, Tipo: {datos['tipo']}\n"
        )
    return resumen


menu_opciones()
