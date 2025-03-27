import unittest    #--------> para ejecutar pruebas unitarias
from fibonacci import fibonacci  #------>  Importamos la función que queremos probar desde el archivo fibonacci.py

class TestFibonacci(unittest.TestCase): #-----> lo que nos permite escribir y ejecutar pruebas con unittest

    def test_numeros_positivos(self):  #---------> Prueba de números positivos
        self.assertEqual(fibonacci(2, 3), 5)
        self.assertEqual(fibonacci(10, 20), 30)
        self.assertEqual(fibonacci(100, 200), 300)

    def test_numeros_negativos(self): #-------> Prueba con números negativos
        self.assertEqual(fibonacci(-1, -1), -2)
        self.assertEqual(fibonacci(-5, -10), -15)
        self.assertEqual(fibonacci(-100, -200), -300)

    def test_mixto_positivo_negativo(self): #-------> Se verifica que la suma de positivos y negativos sea la correcta
        self.assertEqual(fibonacci(-10, 10), 0)
        self.assertEqual(fibonacci(5, -3), 2)
        self.assertEqual(fibonacci(-7, 14), 7)

    def test_ceros(self): #--------> Verifica que la función maneja correctamente el 0 en diferentes escenarios
        self.assertEqual(fibonacci(0, 0), 0)
        self.assertEqual(fibonacci(0, 5), 5)
        self.assertEqual(fibonacci(10, 0), 10)

    def test_numeros_decimales(self): #--------> Se verifica que la función maneje correctamente los decimalles (float)
        self.assertEqual(fibonacci(1.5, 2.5), 4.0)
        self.assertEqual(fibonacci(10.1, 5.2), 15.3)
        self.assertEqual(fibonacci(100.75, 200.25), 301.0)

    def test_numeros_grandes(self): #-------> Se verifica que la función puede manejar enteros muy grandes sin errores
        self.assertEqual(fibonacci(10**6, 10**6), 2 * 10**6)
        self.assertEqual(fibonacci(10**9, 10**9), 2 * 10**9)
        self.assertEqual(fibonacci(10**12, 10**12), 2 * 10**12)

    def test_valores_invalidos(self): #------> Espera que la función genere un error si se ingresan strings
        self.assertRaises(TypeError, fibonacci, "a", "b")
        self.assertRaises(TypeError, fibonacci, [1, 2], [3, 4])
        self.assertRaises(TypeError, fibonacci, {"x": 1}, {"y": 2})

    def test_booleanos(self): #-----> True y False no son números válidos así que se espera que la función genere un TypeError
        self.assertRaises(TypeError, fibonacci, True, False)
        self.assertRaises(TypeError, fibonacci, True, 10)
        self.assertRaises(TypeError, fibonacci, 10, False)

    def test_tipos_estructurados(self): #------>  Se espera que la función falle cuando recibe tuplas
        self.assertRaises(TypeError, fibonacci, (1, 2), (3, 4))
        self.assertRaises(TypeError, fibonacci, None, 5)
        self.assertRaises(TypeError, fibonacci, {"a": 1}, {"b": 2})

    def test_extremos(self):#------>maneja correctamente números enormes sin errores de desbordamiento
        self.assertEqual(fibonacci(10**100, 10**100), 2 * 10**100)
        self.assertEqual(fibonacci(-10**100, -10**100), -2 * 10**100)
        self.assertEqual(fibonacci(0, 10**100), 10**100)

