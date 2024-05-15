import unittest
from src.NewtonRaphson import NewtonRaphson

class TestNewtonRaphson ( unittest.TestCase ) :
    def test_NewtonRaphson_ingresarNumero_retornaRaizCubica ( self ) :
        newtonRaphson=NewtonRaphson()
        self.assertEqual ( 2 , newtonRaphson.raizCubica(8) )
