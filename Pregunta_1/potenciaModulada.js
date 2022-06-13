/////////////////////////////////////////////////////
//    Autor: Eros Cedeño 16-10216
//    Universidad Simon Bolivar
//    Trimestre: Abril-Julio 2022
//    Asignatura: Lenguajes de Programacion CI3641
//    Profesor: Ricardo Monascal
//    Fecha: 2022/06/12 (yyyy/mm/dd)
/////////////////////////////////////////////////////


// Se define la estructura para interactuar por la consola
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// Solicitamos los argumentos
console.log("\nCalculadora de Potencia Modulada de la forma a^b mod c")
const solicitud = "\nIntroduzca a, b y c\nEjemplo: > 1 2 3\n\n> "

readline.question(solicitud, args => {

    args = args.split(" ");
    // Invocamos la Funcion recursiva Potencia Modulada
    console.log( `a^b mod c: ${potenciaModulada( args[0], args[1], args[2] )}` )
    readline.close();
});

// Definicion de Potencia Modulada
function potenciaModulada( a, b, c){
    if (b == 0) {
        return 1
    } else {
        return ( (a % c) * potenciaModulada( a, b-1, c ) ) % c 
    }
}