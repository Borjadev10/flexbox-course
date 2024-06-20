// Lista de nombres
const miLista = ["velma", "exploradora", "jane", "john", "harry"];

// Bucle for que imprime cada nombre en la lista
for (let i = 0; i < miLista.length; i++) {
    console.log(miLista[i]);
}

// Bucle while que recorre la misma lista e imprime los nombres
let contador = 0;
while (contador < miLista.length) {
    console.log(miLista[contador]);
    contador++;
}

// Función de flecha que devuelve "Hola mundo"
const holaMundo = () => "Hola mundo";
console.log(holaMundo());
