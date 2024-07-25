import unittest
from clasePalindromo import Palindromo

class testPalindromo(unittest.TestCase):
    __Palindromo = None
    __NoPalindromo = None

    def setUp(self):
        self.__Palindromo = Palindromo("menem")
        self.__NoPalindromo = Palindromo("juan")
        self.__PalindromoComparable = Palindromo("aibofobia")
    
    def testUnPalindromo(self):
        self.assertTrue(self.__Palindromo.esPalindromo())
        self.assertTrue(self.__PalindromoComparable.esPalindromo())
    
    def testUnNoPalindromo(self):
        self.assertFalse(self.__NoPalindromo.esPalindromo())
    
    def testcompararPalindromos(self):
        self.assertNotEqual(self.__Palindromo,self.__PalindromoComparable)
    
    def testLongitudPalabra(self):
        self.assertEqual(self.__Palindromo.getLongitud(),5)
        self.assertEqual(self.__PalindromoComparable.getLongitud(),9)
        self.assertNotEqual(self.__NoPalindromo.getLongitud(),20)
    
    def testParidad(self):
        self.assertTrue(self.__NoPalindromo.parImpar())
        self.assertFalse(self.__Palindromo.parImpar())
        self.assertFalse(self.__PalindromoComparable.parImpar())

if __name__ == "__main__":

    unittest.main()

    
