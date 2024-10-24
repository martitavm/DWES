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
        self._nombre = nombre  # Atributo 'privado'
        self._salario = salario  # Atributo 'privado'

    @property
    def nombre(self):  # Getter
        return self._nombre

    @nombre.setter
    def nombre(self, valor):  # Setter
        if isinstance(valor, str):
            self._nombre = valor
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres.")

    @property
    def salario(self):  # Getter
        return self.salario

    @salario.setter
    def salario(self, valor):  # Setter
        if isinstance(valor, float):
            self._salario = valor
        else:
            raise ValueError("El salario tiene que ser un número con decimales")

    def detalles(self):
        return f"Nombre: {self._nombre}, Salario: {self._salario}"

    def __del__(self):
        print(
            f"El objeto del empleado {self._nombre} con salario {self._salario} ha sido eliminado."
        )


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self._departamento = departamento

    @property
    def departamento(self):  # Getter
        return self._departamento

    @departamento.setter
    def departamento(self, valor):  # Setter
        if isinstance(valor, str):
            self._departamento = valor
        else:
            raise ValueError("El departamento debe ser una cadena de caracteres.")

    def detalles(self):
        return f"Nombre: {self._nombre}, Salario: {self._salario}, Departamento: {self._departamento}"

    @classmethod
    def descuento_sueldo(cls, salario):
        return salario * 0.90

    @staticmethod
    def impuesto(salario):
        return salario * 0.21
