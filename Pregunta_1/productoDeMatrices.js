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
console.log("\nMultiplicadora de Matrices")
const solicitud = "Introduzca Matriz separando elementos \
de la misma fila con espacios y separando las filas con ','\nsin espacios alrededor\
 Ejemplo > 1 2,3 4\n> "

readline.question(solicitud, args => {
    //Obtenemos Matriz A
    A = args.split(",")
    for( let i = 0; i < A.length; i++){
        A[i] = A[i].split(" ");
    }
    console.log(`Matriz A: `);
    console.log(A)

    // Obtenemos Matriz B
    readline.question( solicitud, args2 => {
        
        B = args2.split(",")
        for( let i = 0; i < B.length; i++){
            B[i] = B[i].split(" ");
        }
        console.log(`Matriz B: `);
        console.log(B)

        // Hallamos el Producto
        C = multiplicar(A,B);

        //Mostramos el Resultado
        console.log( "Resultado: " )
        console.log(C)
        readline.close();
    });
});

// Funcion multiplicar Dos Matrices A y B

function multiplicar(A, B){
    let n = A.length;
    let m = B.length;
    let p = B[0].length;
    let C = []

    for(let i = 0; i < n; i++){
        C[i] = new Array(p);
    }

    for( let i = 0; i < n; i++) {
        for(let j = 0; j < p; j++) {
            C[i][j] = 0
            for( let k = 0; k < m; k++ ){
                C[i][j] += A[i][k]*B[k][j];
            }
        }
    }
    
    return C;
}
