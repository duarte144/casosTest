import unittest #--------> para ejecutar pruebas unitarias
from vocales import contar_vocales   #------>  Importamos la función que queremos probar desde el archivo vocales.py

class TestContarVocales(unittest.TestCase):   #-----> lo que nos permite escribir y ejecutar pruebas con unittest

    def test_texto_con_vocales_normales(self): #------------> Verifica que la función devuelva 4 las vocales 
        self.assertEqual(contar_vocales("Hola Mundo"), 4)
        self.assertEqual(contar_vocales("Python es genial"), 6)
        self.assertEqual(contar_vocales("Unittest"), 3)

    def test_texto_vacio_y_sin_vocales(self): #--------> Se prueban casos donde no hay vocales o el texto está vacío
        self.assertEqual(contar_vocales(""), 0)
        self.assertEqual(contar_vocales("rhythm"), 0)
        self.assertEqual(contar_vocales("bcdfghjklmnpqrstvwxyz"), 0)

    def test_mayusculas_y_minusculas(self): #--------> Verifica que la función cuente correctamente vocales en mayúsculas y minúsculas
        self.assertEqual(contar_vocales("AEIOU aeiou"), 10)
        self.assertEqual(contar_vocales("Hola Qué Tal"), 5)
        self.assertEqual(contar_vocales("PyThOn UnItEsT"), 5)

    def test_vocales_con_tildes_y_caracteres_especiales(self): #-----------> Se prueba que la función reconozca vocales con tildes
        self.assertEqual(contar_vocales("áéíóú ÁÉÍÓÚ"), 10)
        self.assertEqual(contar_vocales("Canción, emoción, avión"), 9)
        self.assertEqual(contar_vocales("Público único"), 7)

    def test_texto_con_numeros_y_simbolos(self):  #-----------> Se verifica que los números y símbolos no sean contados como vocales
        self.assertEqual(contar_vocales("H0l@, ¿cóm0 estás?"), 6)
        self.assertEqual(contar_vocales("1234567890"), 0)
        self.assertEqual(contar_vocales("!@#$%^&*()"), 0)

    def test_texto_con_espacios_y_tabulaciones(self): #------> Se evalúan espacios en blanco, tabulaciones y saltos de línea
        self.assertEqual(contar_vocales("     "), 0)
        self.assertEqual(contar_vocales("a e i o u"), 5)
        self.assertEqual(contar_vocales("\n\t a b c d e"), 2)

    def test_textos_largos_y_repeticiones(self): #-------------> Se prueban textos con miles de repeticiones de vocales
        self.assertEqual(contar_vocales("A" * 1000), 1000)
        self.assertEqual(contar_vocales("E" * 500 + "I" * 500), 1000)
        self.assertEqual(contar_vocales("O" * 300 + "U" * 200), 500)

    def test_mezcla_vocales_y_consonantes(self): #----------> Se mezclan vocales y consonantes para comprobar la precisión del conteo
        self.assertEqual(contar_vocales("AbCdEfGhIjKlMnOpQrStUvWxYz"), 5)
        self.assertEqual(contar_vocales("Supercalifragilisticoespialidoso"), 20)
        self.assertEqual(contar_vocales("Murciélago"), 6)

    def test_entradas_invalidas(self): #------------> Se prueban entradas no textuales
        self.assertEqual(contar_vocales(str(None)), 0)
        self.assertEqual(contar_vocales(str(12345)), 0)
        self.assertEqual(contar_vocales(str([])), 0)

    def test_caracteres_unicode_y_emojis(self): #-----------> Se verifica que los emojis y caracteres Unicode no afecten el conteo
        self.assertEqual(contar_vocales("🌟 a e i o u 🎉"), 5)
        self.assertEqual(contar_vocales("🔥🚀💡AEIOU💖"), 5)
        self.assertEqual(contar_vocales("😀😃😄😁"), 0)

