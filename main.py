class Asiento:

    def _init_(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):

        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]

        if color in colores:
            self.color = color
        
class Auto:

    cantidadCreados = 0
    def _init_(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):

        asientos = 0

        for asiento in self.asientos:
            if asiento is not None:
                asientos += 1

        return asientos


    def verificarIntegridad(self):

        asientosOriginales = True

        for asiento in self.asientos:
            if asiento is not None:
                if asiento.registro != self.motor.registro:
                    asientosOriginales = False
                    break

        if asientosOriginales and self.registro == self.motor.registro:
            return "Auto original"
        else:
            return "Las piezas no son originales"

class Motor:

    def _init_(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):

        if (tipo == "electrico" or tipo == "gasolina"):
            self.tipo = tipo