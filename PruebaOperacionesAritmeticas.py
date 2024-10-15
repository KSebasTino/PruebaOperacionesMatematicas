import unittest
from OperacionesAritmeticas import OperacionesAritmeticas


class PruebaOperacionesAritmeticas(unittest.TestCase):

    def setUp(self):
        self.operacion = OperacionesAritmeticas()

    def tearDown(self):
        self.operacion = None

    def test_suma_dosEnteros_retornaSuma(self):

        sumando1 = 10
        sumando2 = 20
        resultadoEsperado = 30

        resultadoActual = self.operacion.suma(sumando1, sumando2)

        self.assertEqual(resultadoEsperado, resultadoActual)

def mcd(dato1, dato2):
    while dato2:
        dato1, dato2 = dato2, dato1 % dato2
    return dato1

def mcm(dato1, dato2):
    return abs(dato1 * dato2) // mcd(dato1, dato2)

class PruebaOperacionesAitmeticas(unittest.TestCase):
    def setUp(self):
        self.dato1 = 10
        self.dato2 = 15

    def tearDown(self):
        self.dato1 = None
        self.dato2 = None

    def test_mcd_dosEnteros_retornaMCD(self):
        resultadoEsperado = 5
        resultadoActual = mcd(self.dato1 , self.dato2)
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_mcm_dosEnteros_retornaMCM(self):
        resultadoEsperado = 30
        resultadoActual = mcm(self.dato1, self.dato2)
        self.assertEqual(resultadoEsperado, resultadoActual)

if __name__ == '__main__':
    unittest.main()
