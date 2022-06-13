"""
Pruebas unitarias
"""

from Cuaternion import Cuaternion
import unittest

class TestCuternion( unittest.TestCase ):
    def test_suma_y_resta_por_escalar(self):
        entero = -5
        flotante = -2.510
        cuater = Cuaternion( 2, 2, 3, 5 )
        self.assertTrue( entero*cuater == cuater*entero )
        self.assertTrue( entero*cuater == Cuaternion(-10,-10,-15,-25) )
        self.assertTrue( flotante*cuater == cuater*flotante )
        self.assertTrue( flotante*cuater == Cuaternion(-5.02,-5.02,-7.53,-12.55) )
    


    def test_producto_por_escalar( self ):
        entero = -15
        flotante = -102.123
        a = Cuaternion( -3, 6, 7, -8)
        b = Cuaternion( 1, 12, -7, -11)
        respuesta = Cuaternion(-114, -163, -2, -101)
        self.assertEqual( a*b , respuesta )
        self.assertTrue(b*entero == Cuaternion(-15, -180, 105, 165))
        self.assertTrue(entero*b == Cuaternion(-15, -180, 105, 165))
        self.assertTrue(b*flotante == Cuaternion(-102.123, -1225.476, 714.861, 1123.353))
        self.assertTrue(flotante*b == Cuaternion(-102.123, -1225.476, 714.861, 1123.353))

    def test_conjugada(self):
        a = Cuaternion( 2, 8.0, -3, 5)
        conjugada = Cuaternion( 2, -8.0, 3, -5)
        self.assertTrue(~a==conjugada)
    
    def test_modulo(self):
        a = Cuaternion( -2, 2, 2, 2)
        modulo = 4
        self.assertTrue(+a==modulo)
        

if __name__ == '__main__':
    unittest.main()