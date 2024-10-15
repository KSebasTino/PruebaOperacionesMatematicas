class OperacionesAritmeticas:
    def suma(self, sumando1, sumando2):
        return sumando1 + sumando2

    def division(self, dividendo, divisor):
        try:
            return dividendo / divisor
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero"
