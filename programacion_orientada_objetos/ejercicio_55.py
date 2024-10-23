# Ejercicio 54: Sistema de Gestión de Empleados
#
# En esta actividad se desarrollará un sistema simple de gestión de empleados de una empresa.
#
# Requisitos:
#
# Crea una clase Empleado que contenga:
#
# Atributos privados nombre y salario.
#
# Métodos getters y setters para ambos atributos.
# Un método de instancia detalles() que muestre la información del empleado.
# Un método destructor que muestre un mensaje al eliminar el objeto.
#
# Crea una subclase Gerente que herede de la clase Empleado.
#
# Esta clase debe tener un atributo adicional privado llamado departamento.
#
# Sobrescribe el método detalles() para que también muestre el departamento del gerente.
# Utiliza el método super() para acceder al constructor de la clase Empleado.
#
# Agrega un método de clase llamadodescuento_sueldo() que calcule un descuento del 10% al salario y devuelva el salario modificado.
#
# Agrega un método estático impuesto() que acepte un salario y devuelva el impuesto (21% del salario).


class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre  # Atributo 'privado'
        self.__salario = salario  # Atributo 'privado'
