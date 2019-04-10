import unittest
import Test_Carlos_PuertoG

class Test_ejemplo(unittest.TestCase):
    def test_suma(self):
        result=Test_Carlos_PuertoG.suma(7,3)
        self.assertEqual(result,10)

#Despues de este mensaje van a integrar sus casos de prueba

        


if __name__== '__main__':
    unittest.main()

    
