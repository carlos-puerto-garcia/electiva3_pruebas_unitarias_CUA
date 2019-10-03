import unittest
import Test_Carlos_PuertoG
import Test2_Carlos_PuertoG
import Edwin
import Cardenas
import Ejemplo
import Testni
import Ballesteros
import Comparacion
import Frank
import Yohan

class Test_ejemplo(unittest.TestCase):
    def test_suma(self):
        result=Test_Carlos_PuertoG.suma(7,3)
        self.assertEqual(result,10)

#Despues de este mensaje van a integrar sus casos de prueba
        
class Test_multiplicacion(unittest.TestCase):
    def test_multl(self):
        result=Test2_Carlos_PuertoG.multiplicacion(5,3)
        self.assertEqual(result,15)

class Test_cuadrado(unittest.TestCase):
    def test_cuadrado2(self):
        result=Edwin.cuadrado2(5)
        self.assertEqual(result,25)
        
class Test(unittest.TestCase):
    def test_sumaprogre(self):
        result=Cardenas.sumaprogre(5)
        self.assertEqual(result,15)
       
class Test_operacion (unittest.TestCase):
    def testtype (self):
        result = Ejemplo.hola()
        self.assertIs (result,True)
        
#Trabajo de Larry Alvarez Rodriguez
class PruebasMetodosCadenas(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('casa'.upper(), 'CASA')

    def test_isupper(self):
        self.assertTrue('CASA'.isupper(),print("true"))
#Trabajo de Jhon Darwin Acevedo
class Test_false (unittest.TestCase):
    def testtype (self):
        result = Testni.Verificarnombres()
        self.assertFalse(result, False)
        #Trabajo de Brehider

'''class TestAssertIn (unittest.TestCase):
    def test_verificar_lista(self):
        lista = Ballesteros.IngresarLista()
        numero = input("Ingrese el número para verificar su existencia:")
        self.assertIn(numero, lista)
'''
class PruebasFunciones(unittest.TestCase):
    def test_Comparacion(self):
        result= Comparacion.comparaciontest("Hola_Mundo")
        self.assertIs("Hola_Mundo",result)

class Test_funcion (unittest.TestCase):
    def test_multiplicacion(self):
        result= Frank.multiplicar(3,5)
        self.assertIsNot(result,16)
#Trabajo de Frank Ortiz

def add(x,y):
    return x + y

class Testing(unittest.TestCase):
    def test(self):
        result = Yohan.add(3,8)
        self.assertNotEqual(result, 11)

#Yohan valencia        
if __name__== '__main__':
    unittest.main()

    
