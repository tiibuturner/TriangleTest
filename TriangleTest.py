
## Tiina Ylimäki

import unittest
import TriangleEngine

class TriangleTest(unittest.TestCase):
    def test_TasasivuinenKolmio(self):
        a = int(6)
        b = int(6)
        c = int(6)
        expectResult = 'Kolomio o tasasivune'
        result = TriangleEngine.typeTriangle(a, b, c)
        self.assertEqual(result, expectResult)
    
    def test_TasakylkinenKolmio1(self):
        a = int(4)
        b = int(12)
        c = int(12)
        expectResult = 'Kolomio o tasakylykine'
        result = TriangleEngine.typeTriangle(a, b, c)
        self.assertEqual(result, expectResult)

    def test_TasakylkinenKolmio2(self):
        a = int(9)
        b = int(6)
        c = int(9)
        expectResult = 'Kolomio o tasakylykine'
        result = TriangleEngine.typeTriangle(a, b, c)
        self.assertEqual(result, expectResult)

    def test_TasakylkinenKolmio3(self):
        a = int(1)
        b = int(4)
        c = int(4)
        expectResult = 'Kolomio o tasakylykine'
        result = TriangleEngine.typeTriangle(a, b, c)
        self.assertEqual(result, expectResult)

    def test_EpasaannollinenKolmio(self):
        a = int(4)
        b = int(5)
        c = int(6)
        expectResult = 'Kolomio o epäsäännölline'
        result = TriangleEngine.typeTriangle(a, b, c)
        self.assertEqual(result, expectResult)
    
    def test_NegatiivinenKolmio(self):
        a = int(6)
        b = int(-5)
        c = int(5)
        expectResult = 'Annoit negatiivisia numeroota, ei oo kolomio'
        result = TriangleEngine.typeTriangle(a, b, c)
        self.assertEqual(result, expectResult)

    def test_EiValidiKolmio1(self):
        a = int(8)
        b = int(1)
        c = int(9)
        expectResult = 'Ei oo validi kolomio'
        result = TriangleEngine.typeTriangle(a, b, c)
        self.assertEqual(result, expectResult)

    def test_EiValidiKolmio2(self):
        a = int(4)
        b = int(4)
        c = int(45)
        expectResult = 'Ei oo validi kolomio'
        result = TriangleEngine.typeTriangle(a, b, c)
        self.assertEqual(result, expectResult)

    def test_EiValidiKolmio3(self):
        a = int(8)
        b = int(3)
        c = int(13)
        expectResult = 'Ei oo validi kolomio'
        result = TriangleEngine.typeTriangle(a, b, c)
        self.assertEqual(result, expectResult)

if (__name__ == "__main__"):
    unittest.main()