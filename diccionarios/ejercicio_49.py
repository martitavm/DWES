#Agregar un nuevo producto al inventario.
#Actualizar el precio y la cantidad de un producto.
#Consultar la información de un producto específico.
#Eliminar un producto del inventario.
#Comprobar si un producto está en el inventario.
#Obtener todas las claves (nombres de los productos).
#Obtener todos los valores (información de los productos).
#Recorrer el inventario y mostrar la información de cada producto.

inventario_tienda = {
    "Ordenador": {
        "precio": 2599.99,
        "cantidad": 10,
        "puntuaciones": [4.5, 5.0, 4.0]
    },
    "Móvil": {
        "precio": 699.99,
        "cantidad": 25,
        "puntuaciones": [4.0, 4.5, 3.5]
    },
    "Ratón": {
        "precio": 59.99,
        "cantidad": 15,
        "puntuaciones": [4.8, 4.6, 4.9]
    },
    "Monitor": {
        "precio": 189.99,
        "cantidad": 50,
        "puntuaciones": [4.3, 4.1, 4.4]
    }
}
print(inventario_tienda)

inventario_tienda.update({ "Cascos": { "precio": 69.99, "cantidad": 40, "puntuaciones": [3.3, 4.0, 4.6]}})
print(inventario_tienda)

inventario_tienda["Monitor"].update({"precio": 289.99, "cantidad": 45})
print(inventario_tienda)

print(inventario_tienda.get("Ratón"))

inventario_tienda.pop("Móvil")
print(inventario_tienda)

print(f"¿Existe Ordenador en inventario_tienda? {"Ordenador" in inventario_tienda}")

print(inventario_tienda.keys())

print(inventario_tienda.values())

for nombre_producto, valores in inventario_tienda.items():
    print(f" Nombre_producto: {nombre_producto}, {valores}")