# Agregar un nuevo estudiante con su información.
# Actualizar la lista de asignaturas de un estudiante existente.
# Consultar la información de un estudiante y mostrarla.
# Eliminar a un estudiante del diccionario.
# Comprobar si un estudiante existe en el diccionario.
# Obtener todas las claves (nombres de los estudiantes).
# Obtener todos los valores (información de los estudiantes).
# Recorrer el diccionario y mostrar la información de cada estudiante.

estudiantes = {
    "Anita":[27,["Encantamientos", "Herbología", "Artes Oscuras"]],
    "Alesito": [28, ["Alquimia", "Pociones", "Vuelo"]],
    "Martita": [20, ["Encantamientos", "Astronomía", "Artes Oscuras"]],
    "IsmaJefazo": [22, ["Vuelo", "Astronomía", "Transformaciones"]],
}
print(estudiantes)
estudiantes.update({"Rivas": [37,["Coro del sapo", "Teoría mágica"]]})
print(estudiantes)

estudiantes.update({"Rivas": [37,["Coro del sapo", "Artes Oscuras"]]})
print(estudiantes)

print(estudiantes.get("Rivas"))

estudiantes.pop("Alesito")
print(estudiantes)

print(f"¿Existe Anita en estudiantes? {"Anita" in estudiantes}")

print(estudiantes.keys())

print(estudiantes.values())

for nombre, valores in estudiantes.items():
    print(f" Nombre: {nombre}, Edad y Asignaturas: {valores}")
