class OperacionesAritmeticas:
    def suma(self, sumando1, sumando2):
        return sumando1 + sumando2

    def mcm(self, dato1, dato2):
        try:
            return dato1 * dato2
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero"
