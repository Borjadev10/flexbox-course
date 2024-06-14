function checkpoint(a, b, c, d) {

    let suma1 = a + b;

 
    let suma2 = c + d;

   
    let resultado = suma1 * suma2;


    if (resultado > 50) {
        console.log("¡El número es mayor que 50!");
    } else {
        console.log("¡El número es menor que 50!");
    }
}

// Ejemplo 
checkpoint(9, 4, 7, 6); // Salida: ¡El número es mayor que 50!
checkpoint(1, 1, 2, 4); // Salida: ¡El número es menor que 50!
