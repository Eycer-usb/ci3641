###################################################
#   Autor: Eros Cedeño 16-10216
#   Universidad Simon Bolivar
#   Trimestre: Abril-Julio 2022
#   Asignatura: Lenguajes de Programacion CI3641
#   Profesor: Ricardo Monascal
#   Fecha: 2022/06/12 (yyyy/mm/dd)
##################################################
import sys
from math import log2 as log, ceil as techo

def bienvenido():
    print("###################################################\n\
#   Autor: Eros Cedeño 16-10216\n\
#   Universidad Simon Bolivar\n\
#   Trimestre: Abril-Julio 2022\n\
#   Asignatura: Lenguajes de Programacion CI3641\n\
#   Profesor: Ricardo Monascal\n\
#   Fecha: 2022/06/12 (yyyy/mm/dd)\n\
##################################################\n\n\n\n")

    print("------------BUDDY SYSTEM------------")

def iniciar():
    cantidad_bloques = int(input("Ingrese la cantidad de bloques \
de memoria que se manejará:\n> "))
    potencia = log(cantidad_bloques)//1
    tamanios_disponibles = {}
    tamanios_disponibles[int(2**potencia)] = [ 0 ]
    # Establecemos la memoria para mostrarla luego
    # si la celda esta vacia tiene None si no tiene el nombre asociado
    memoria = [ None  for i in range(0,int(2**potencia)) ]
    print("\nMemoria Establecida a {} bloques\n".format(int(2**potencia)))
    #mostrar(memoria, tamanios_disponibles, )
    return [ memoria, tamanios_disponibles, potencia ]

# Procesa la query recibida segun su tipo
def ejecutar_solicitud(query, memoria, tamanios_disponibles, potencia, diccionario_nombres):
    args = query.split(' ')
    instruccion = args[0]
    if(instruccion == "RESERVAR" or instruccion == "reservar"):
        try:
            reservar(args[1], int(args[2]), memoria, tamanios_disponibles, potencia, diccionario_nombres)
        except: print("Error en los argumentos \nSintaxis: RESERVAR <nombre> <cantidad>")

    elif(instruccion == 'LIBERAR' or instruccion == "liberar"):
        try:
            liberar(args[1], diccionario_nombres, memoria, tamanios_disponibles, total = 2**potencia)
        except:
            print("Error en los argumentos \nSintaxis: LIBERAR <nombre>")
    elif(instruccion == "MOSTRAR" or instruccion == "mostrar"):
        try:
            mostrar(memoria, tamanios_disponibles)
        except:
            print("Error en los argumentos \nSintaxis: MOSTRAR")
    elif(instruccion == 'SALIR' or instruccion == "salir" ):
        salir()
    else:
        print("Instruccion Invalida")


#   Marca en el Arreglo de memoria el nombre dado en las posiciones
#   Correspondientes
def etiquetar_memoria(memoria, indice, nombre, cantidad, total_reservar):
    for i in range(indice, indice+cantidad):
        memoria[i] = nombre

    for i in range(indice+cantidad, indice+total_reservar):
        memoria[i] = -1

#   Elimina los nombres del Arreglo de Memoria
def desetiquetar_memoria( memoria, indice ):
    nombre = memoria[indice]
    c = 0
    i = indice
    while  i < len(memoria) and (memoria[i] == nombre or memoria[i] == -1):
        memoria[i] = None
        c += 1
        i += 1
    return  c

#   Elimina del diccionario que contiene los tamanos disponibles
#   un tamano dado
def eliminar_tamanio_disponible(tamanios_disponibles, tamanio_a_reservar):

    if( tamanio_a_reservar in tamanios_disponibles and \
        len(tamanios_disponibles[tamanio_a_reservar]) > 1):
        return tamanios_disponibles[tamanio_a_reservar].pop(0)
    elif( tamanio_a_reservar in tamanios_disponibles and \
        len(tamanios_disponibles[tamanio_a_reservar]) == 1 ):
        ans = tamanios_disponibles[tamanio_a_reservar].pop(0)
        tamanios_disponibles.pop(tamanio_a_reservar)
        return ans
    else:
        print("El espacio no esta disponible")
        return -1

#   Inserta en el diccionario de tamanos disponibles un nuevo tamano
def agregar_tamanio_disponible( tamanios_disponibles, tamanio_a_reservar, indice ):
    if (tamanio_a_reservar in tamanios_disponibles):
        tamanios_disponibles[tamanio_a_reservar].append(indice)
    else:
        tamanios_disponibles[tamanio_a_reservar] = [ indice ]

#   Funcion recursiva para dividir espacios de memoria (potencias de 2)
#  en particiones iguales hasta alcanzar el tamano mas ajustado para la 
# informacion a asignar
def particionar( tamanios_disponibles, tamanio_particionar, tamanio_objetivo ):
    if tamanio_particionar != tamanio_objetivo:
        indice = eliminar_tamanio_disponible(tamanios_disponibles, tamanio_particionar)
        agregar_tamanio_disponible(tamanios_disponibles, tamanio_particionar//2, indice)
        agregar_tamanio_disponible(tamanios_disponibles, tamanio_particionar//2, \
            indice+tamanio_particionar//2)
        particionar(tamanios_disponibles, tamanio_particionar//2, tamanio_objetivo)

#   Procesa la solicitud de reservar un espacio en la memoria
def reservar(nombre, cantidad, memoria, tamanios_disponibles, potencia, diccionario_nombres):
    
    if nombre in diccionario_nombres:
        print("Error: Ese nombre ya pertenece a una asociacion intente con otro nombre")
        return
    
    total = 2**potencia
    tamanio_a_reservar = 2**techo(log(cantidad))
    
    if tamanio_a_reservar > total:
        print( "Memoria total menor a la memoria a asignar" )
        return
    elif tamanio_a_reservar in tamanios_disponibles:
        indice = eliminar_tamanio_disponible(tamanios_disponibles, tamanio_a_reservar)
        diccionario_nombres[nombre] = indice
        etiquetar_memoria(memoria, indice, nombre, cantidad, tamanio_a_reservar)
    else:
        i = tamanio_a_reservar
        
        while( i < total and i not in tamanios_disponibles):
            i*= 2
        if( i in tamanios_disponibles ):
            particionar( tamanios_disponibles, i, tamanio_a_reservar )
            reservar(nombre, cantidad, memoria, tamanios_disponibles, potencia, diccionario_nombres)
        else:
            print("No hay suficiente espacio en memoria")

#   Realiza un merge de particiones iguales adyacentes y las convierte 
#   en una particion del doble de su tamano
def unir_particiones_adyacentes(tamanios_disponibles, tamanio, indice, total):

    # Considerando las particiones como un arbol binario
    # calculamos si la particion dada tiene un nodo
    # con el mismo padre y si es asi los une
    clust = indice // tamanio
    bro = None
    #Hijo izquierdo
    if clust % 2 == 0:
        bro = indice + tamanio
    #Hijo derecho
    else:
        bro = indice - tamanio
        
    # Recorremos recursivamente uniendo las particiones adyacentes
    # subiendo en el arbol
    if bro > 0 and bro in tamanios_disponibles[tamanio]:
        i = indice
        if (bro < i): i, bro = bro, i
        print(i, bro)
        tamanios_disponibles[tamanio].remove(bro)
        tamanios_disponibles[tamanio].remove(i)
        if( len(tamanios_disponibles[tamanio]) == 0 ): tamanios_disponibles.pop(tamanio)
        agregar_tamanio_disponible(tamanios_disponibles, tamanio*2, i)
        unir_particiones_adyacentes(tamanios_disponibles, tamanio*2, i, total)
    else:
        pass

#   Maneja la instruccion para liberar la memoria principal
#   dado el nombre de un programa en memoria
def liberar(nombre, diccionario_de_nombres, memoria, tamanios_disponibles, total):
    if nombre in diccionario_de_nombres:
        indice = diccionario_de_nombres[nombre]
        nuevo_tamanio_disponible = desetiquetar_memoria(memoria, indice)
        agregar_tamanio_disponible(tamanios_disponibles, nuevo_tamanio_disponible, indice)
        unir_particiones_adyacentes( tamanios_disponibles, nuevo_tamanio_disponible, indice, total )
        diccionario_de_nombres.pop(nombre)

    else:
        print("No hay memoria reservada a ese nombre")


#   Pos Muestra el estado de la memoria en la pantalla
#   Subrutina manejadora de la instruccion MOSTRAR
def mostrar(memoria, tamanios_disponibles):
    print("\nEstado de Memoria")
    print(memoria)

    print("\nBloques Libres:")
    print( "Tamaño del Bloque -> Indices en Memoria" )
    for tamanio, indice in tamanios_disponibles.items():
        print("{} -> {}".format(tamanio, indice ))
    print('\n')

# Finaliza la ejecucion del programa
def salir():
    sys.exit()

#Funcion Principal
def main():
    bienvenido()
    memoria, tamanios_disponibles, potencia = iniciar()
    diccionario_nombres = {}

    while True:
        query = input("> ")
        ejecutar_solicitud(query, memoria, tamanios_disponibles, potencia, diccionario_nombres)


if __name__ == '__main__':
    main()



    


