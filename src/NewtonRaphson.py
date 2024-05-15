import math

class NewtonRaphson( ):

    def __init__(self,numero, valorInicial):
        self.terminoIndependiente = numero
        self.valorInicial = valorInicial

    def funcionNR ( self, x, variableIndependiente ) :
        resultado = x * x * x - variableIndependiente
        return resultado

    def derivadaFuncionNR ( self, x ) :
        resultado = 3 * x * x
        return resultado

    def raizNewtonRapshon(self):
        x = self.valorInicial
        while (abs( self.funcionNR ( x , self.terminoIndependiente ) ) >= 0.001):
            x = x - self.funcionNR ( x , self.terminoIndependiente ) / self.derivadaFuncionNR ( x )
        return x

    def imprimirSolución(self):
        print("\nRaíz cúbica")
        print ( "X^3 = {0:.2f}".format(self.terminoIndependiente) )
        print ( "\nSolución:" )
        x = self.raizNewtonRapshon()
        print (f"X = {x}")
