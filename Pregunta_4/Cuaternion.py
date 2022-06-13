###################################################
#   Autor: Eros Cedeño 16-10216
#   Universidad Simon Bolivar
#   Trimestre: Abril-Julio 2022
#   Asignatura: Lenguajes de Programacion CI3641
#   Profesor: Ricardo Monascal
#   Fecha: 2022/06/12 (yyyy/mm/dd)
##################################################




"""
Clase de datos que implementa los cuaterniones

Se cobrecargaron los operadores de la siguiente forma:

- ( + ) : asociativa, conmutativa y permite operar entero y flotante con cuaternion 
        o dos cuaterniones

- ( * ) : asociativa, permite la multiplicacion de dos cuaterniones o de escalar por 
        cuaternion y de Cuaternion por escalar

- ( ~ ) : Conjugada de cuaternion, prefijo.

- ( + ) : Cuando se usa como prefijo con un cuaternion retorna su modulo euclediano


"""

from math import sqrt

class Cuaternion:
    # Contructor de la clase
    def __init__(self, real, i_coeficient, j_coeficient, k_coeficient) -> None:
        self.real = real
        self.i = i_coeficient
        self.j = j_coeficient
        self.k = k_coeficient
    
    # Se define la suma biadica, sobrecargando el operador +
    def __add__(self, other):

        # En caso se que sumen dos cuaterniones
        if isinstance(other, Cuaternion):
            r = self.real + other.real
            i = self.i + other.i
            j = self.j + other.j
            k = self.k + other.k
            return Cuaternion( r, i, j, k )

        # Si el otro elemento es entero o flotante 
        elif isinstance(other, int)  or isinstance(other, float):
            return Cuaternion( self.real + other, self.i, self.j, self.k )

    # Definimos la reflexividad de la suma
    __radd__ = __add__

    # Sobrecargamos el operador *
    def __mul__(self, other):

        # Si es un escalar se tiene que λ*(a + bi + cj + dk) = λa + λbi + λcj + λdk
        if isinstance(other, int) or isinstance(other, float):
            return Cuaternion( self.real*other,\
                self.i*other, self.j*other, self.k*other )

        # En caso que sea el producto de cuaterniones se aplica la definicion del producto
        # de cuaterniones
        elif( isinstance(other,Cuaternion) ):

            a1, b1, c1, d1 = self.real, self.i, self.j, self.k
            a2, b2, c2, d2 = other.real, other.i, other.j, other.k
            
            r = a1*a2 - b1*b2 - c1*c2 - d1*d2
            i = a1*b2 + b1*a2 + c1*d2 - d1*c2 
            j = a1*c2 - b1*d2 + c1*a2 + d1*b2
            k = a1*d2 + b1*c2 - c1*b2 + d1*a2
            return Cuaternion( r, i, j, k )

    # Permitimos la reflexividad del producto
    __rmul__ = __mul__

    def __invert__(self):
        i = -self.i        
        j = -self.j        
        k = -self.k        
        return Cuaternion(self.real, i, j, k)

    # Se define el modulo euclediano sobrecargando una vez mas el operador +
    # en este caso como operador unario. Por lo que el modulo del cuaternion
    # 'a' se puede calcular con '+a'
    def __pos__(self):
        r = self.real**2
        i = self.i**2
        j = self.j**2
        k = self.k**2
        return sqrt(r+i+j+k)

    # Definimos la igualdad de cuaterniones
    def __eq__(self, other: object) -> bool:
        return (abs(self.real - other.real) < 0.00000001) and (abs(self.i - other.i) < 0.00000001) and \
            (abs(self.j - other.j) < 0.00000001) and (abs(self.k - other.k) < 0.00000001) 

    # Establecemos la representacion del cuaternion en forma de String para
    # facilitar su impresion 
    def __repr__(self) -> str:
        return "{} + {}i + {}j + {}k".format( self.real, self.i, self.j, self.k )
    
if __name__ == '__main__':
    print("###################################################\n\
#   Autor: Eros Cedeño 16-10216\n\
#   Universidad Simon Bolivar\n\
#   Trimestre: Abril-Julio 2022\n\
#   Asignatura: Lenguajes de Programacion CI3641\n\
#   Profesor: Ricardo Monascal\n\
#   Fecha: 2022/06/12 (yyyy/mm/dd)\n\
##################################################")
    print("\nClase que implementa los Cuaterniones como tipo abstracto de Datos\n")
