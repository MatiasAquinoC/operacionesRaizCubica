from src.NewtonRaphson import NewtonRaphson

def calcularRaizCubica (numero, valorInicial) :
    solucion = NewtonRaphson ( numero, valorInicial)
    solucion.imprimirSolución ()

if __name__ == '__main__':
    calcularRaizCubica ( 27,3 )
    calcularRaizCubica ( 8,2 )
    calcularRaizCubica ( 15 , 5 )
