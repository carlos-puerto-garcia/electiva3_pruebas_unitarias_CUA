import unittest
import Test_Carlos_PuertoG
import Test2_Carlos_PuertoG

class Test_ejemplo(unittest.TestCase):
    def test_suma(self):
        result=Test_Carlos_PuertoG.suma(7,3)
        self.assertEqual(result,10)

#Despues de este mensaje van a integrar sus casos de prueba
        
class Test_multiplicacion(unittest.TestCase):
    def test_multl(self):
        result=Test2_Carlos_PuertoG.multiplicacion(5,3)
        self.assertEqual(result,15)

        


if __name__== '__main__':
    unittest.main()

    
