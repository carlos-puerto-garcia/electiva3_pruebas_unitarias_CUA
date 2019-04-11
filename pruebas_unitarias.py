import unittest
import Test_Carlos_PuertoG
import Test2_Carlos_PuertoG
import Edwin
import Cardenas

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
       


if __name__== '__main__':
    unittest.main()

    
