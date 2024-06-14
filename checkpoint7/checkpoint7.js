function checkpoint(a, b, c, d) {

    let suma1 = a + b;

 
    let suma2 = c + d;

   
    let resultado = suma1 * suma2;

    let mensaje = `En las operaciones con los números ${a}, ${b}, ${c} y ${d}, el resultado es ${resultado}`;


    if (resultado > 50) {
        console.log(mensaje + " ¡El número es mayor que 50!");
        
    } else {
        console.log(mensaje + " ¡El número es menor que 50!");       
    }
}


checkpoint(9, 4, 7, 6); 
checkpoint(1, 1, 2, 4); 


