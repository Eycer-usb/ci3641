###################################################
#   Autor: Eros Cedeño 16-10216
#   Universidad Simon Bolivar
#   Trimestre: Abril-Julio 2022
#   Asignatura: Lenguajes de Programacion CI3641
#   Profesor: Ricardo Monascal
#   Fecha: 2022/06/12 (yyyy/mm/dd)
##################################################
from ast import arg
import sys


def bienvenido():
    print("###################################################\n\
#   Autor: Eros Cedeño 16-10216\n\
#   Universidad Simon Bolivar\n\
#   Trimestre: Abril-Julio 2022\n\
#   Asignatura: Lenguajes de Programacion CI3641\n\
#   Profesor: Ricardo Monascal\n\
#   Fecha: 2022/06/12 (yyyy/mm/dd)\n\
##################################################\n\n\n\n")


def bienvenido():
    print("###################################################\n\
#   Autor: Eros Cedeño 16-10216\n\
#   Universidad Simon Bolivar\n\
#   Trimestre: Abril-Julio 2022\n\
#   Asignatura: Lenguajes de Programacion CI3641\n\
#   Profesor: Ricardo Monascal\n\
#   Fecha: 2022/06/12 (yyyy/mm/dd)\n\
##################################################\n\n\n\n")


# Se procesa la Solicitud del usuario
def ejecutar_solicitud(query, programas, relacion_transitiva, traductores):
    args = query.split(' ')
    instruccion = args[0].lower()
    if(instruccion =="definir"):
        try:
            definir(args, programas, relacion_transitiva, traductores)
        except: print("Error en los argumentos \nSintaxis: DEFINIR <tipo> [<argumentos>]")

    elif(instruccion == "ejecutable"):
        try:
            ejecutable(args, programas, relacion_transitiva, traductores)
        except:
            print("Error en los argumentos \nSintaxis: EJECUTABLE <nombre>")

    elif(instruccion == "salir" ):
        salir()
    else:
        print("Instruccion Invalida")

# Permite Definir un programam un interprete o un traductor
def definir(query, programas, relacion_transitiva, traductores):
    tipo = query[1].lower()
    args = query[2:]
    if(tipo == 'programa'):
        nombre = args[0]
        programas[nombre] = args[1]
        print("Se definió el programa '{}', ejecutable en '{}'"
        .format(nombre, args[1]))
    elif(tipo == 'interprete'):
        if args[0].lower() == 'local': args[0] = 'LOCAL'
        interprete = ( args[1], args[0] ) 
        agregar_interprete(interprete, relacion_transitiva)
        print("Se definió un intérprete para '{}', escrito en '{}'".format(args[1], args[0]))
    elif( tipo == 'traductor' ):
        traductor = ( args[1], args[2], args[0] )
        agregar_traductor(traductor, relacion_transitiva, traductores)
        print("Se definió un traductor de '{}' hacia '{}', escrito en '{}'"
                .format(args[1], args[2], args[0]))
    else:
        print("Error al definir\nRecurde que la sintaxis es: DEFINIR <tipo> [<argumentos>]")

# Determina si un programa es ejecutable
def ejecutable(query, programas, relacion_transitiva, traductores):
    nombre = query[1]
    if( nombre in programas ):
        leng = programas[nombre]
        if( es_interpretable(leng, relacion_transitiva, traductores) ):
            print("Si, es posible ejecutar el programa '{}'".format(nombre))
        else:
            print("No es posible ejecutar el programa '{}'".format(nombre))
    else:
        print("Programa no definido")

# Determina si un lenguaje es interpretable a local
def es_interpretable( lenguaje, relacion_transitiva, traductores ):
    if( lenguaje.lower() == 'local' 
    or (lenguaje,'LOCAL') in relacion_transitiva):
        return True
    else:
        for t in traductores:
            if( t[0] == lenguaje ):
                traductores.discard(t)
                a = es_interpretable(t[2], relacion_transitiva, traductores)
                b = es_interpretable(t[1], relacion_transitiva, traductores)                
                if( a and b):
                    interprete = ( t[1], t[2] )
                    agregar_interprete(interprete, relacion_transitiva)
                    
                    return True
                else:
                    traductores.add(t)


               
        return False

# Recibe un nuevo traductor y lo almacena como es correspondiente
def agregar_traductor(traductor, relacion_transitiva, traductores):
    
    origen = traductor[0]
    destino = traductor[1]
    escrito = traductor[2]

    if( es_interpretable(escrito, relacion_transitiva, traductores) ):
        agregar_interprete( (origen, destino), relacion_transitiva )
    else:
        traductores.add(traductor)


# Guarda un interprete en la relacion transitiva y verifica transitividad
def agregar_interprete( interprete, relacion_transitiva ):
    relacion_transitiva.add(interprete)
    entransitivizacion( relacion_transitiva )

# Entransitiviza la relacion binaria XD :P
def entransitivizacion(relacion_transitiva):
    no_transitiva = True
    while no_transitiva:
        contador = 0
        aux = relacion_transitiva.copy()
        for (a,b) in aux:
            for ( c, d ) in aux:
                if b == c and (a,d) not in aux:
                    relacion_transitiva.add( ( a, d ) )
                    contador += 1
        if contador==0: no_transitiva = False
    
# Permite detener la solicitud de argumentos por consula
def salir():
    sys.exit()

# Programa  Principal
def main():
    bienvenido()
    relacion_transitiva = set()
    traductores = set()
    programas = {}
        
    while True:
        query = input("$ > ")
        ejecutar_solicitud(query, programas, relacion_transitiva, traductores)
        pass

if __name__ == '__main__':
    main()