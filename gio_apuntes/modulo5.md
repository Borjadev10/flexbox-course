# Modulo 5

## Lodash parte 1 ( times / filter )
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Lodash Demo</title>
    <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.4/lodash.min.js"></script>
  </head>
  <body>
    <!-- http://houston.astros.mlb.com/stats/sortable.jsp?c_id=hou#playerType=ALL&elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type='R'&season=2017&season_type=ANY&league_code='MLB'&sectionType=sp&statType=hitting&page=1&ts=1516406323861&sortColumn=g&sortOrder='desc'&extended=0 -->
  </body>

  <script>
    // times
    randNumber = () => {
      return Math.round(Math.random() * 100);
    }

    const sampleNumbers = _.times(5, randNumber);

    // filter
    const players = [
      { name: 'Bregman, A',  battingAverage: 0.284 },
      { name: 'Altuve, J',   battingAverage: 0.346 },
      { name: 'Springer, G', battingAverage: 0.283 },
      { name: 'Gurriel, Y',  battingAverage: 0.299 },
      { name: 'Gonzalez, M', battingAverage: 0.303 }
    ];

    const over300 = _.filter(players, player => {
      return player.battingAverage > 0.300;
    });
  </script>
</html>
```
## Lodash parte 1 ( KeyBy / reduce / random )

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Lodash Demo</title>
    <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.4/lodash.min.js"></script>
  </head>
  <body>
  </body>

  <script>
    // keyBy
    const roster = [
      { position: '3B', name: 'Bregman, A' },
      { position: '2B', name: 'Altuve, J' },
      { position: 'CF', name: 'Springer, G' },
      { position: '1B', name: 'Gurriel, Y' },
      { position: 'LF', name: 'Gonzalez, M' }
    ]

    const positions = _.keyBy(roster, 'position');

    const secondBase = positions['2B'];

    // reduce
    const sum = _.reduce([1, 2, 3], function(total, num) {
      return total + num;
    }, 0);

    const homerunStats = [
      { name: 'Bregman, A',  hr: 19 },
      { name: 'Altuve, J',   hr: 24 },
      { name: 'Springer, G', hr: 34 },
      { name: 'Gurriel, Y',  hr: 18 },
      { name: 'Gonzalez, M', hr: 23 }
    ];

    const totalHomeruns = _.reduce(homerunStats, function(total, player) {
      return total + player.hr;
    }, 0);

    const links = [
      "https://google.com",
      "https://devcamp.com",
      "https://airbnb.com"
    ];

    const webLinks = _.reduce(links, function(content, link) {
      return `<a href='${link}'>${link}</a><br>`.concat(content);
    }, '');

    // random
    lodashRandNumber = () => {
      return _.random(1, 100);
    }

    const lodashSampleNumbers = _.times(5, lodashRandNumber);

    console.log(lodashSampleNumbers);
  </script>
</html>
```

### ¿Qué es Lodash en JavaScript?

Lodash es una biblioteca de JavaScript que proporciona utilidades para tareas comunes de programación, como manipulación de arrays, objetos, cadenas de texto y otros tipos de datos. Facilita la escritura de código más limpio y eficiente, reduciendo la necesidad de implementar funciones utilitarias desde cero.

### Ventajas de Usar Lodash

1. **Simplicidad**: Proporciona funciones sencillas y consistentes para operaciones comunes.
2. **Compatibilidad**: Funciona bien con todas las versiones de JavaScript y es compatible con navegadores y entornos de servidor.
3. **Rendimiento**: Optimizado para mejorar el rendimiento en muchas operaciones comunes.
4. **Modularidad**: Puedes importar solo las partes de la biblioteca que necesitas, reduciendo el tamaño de tu código.

### Instalación

Para usar Lodash en tu proyecto, puedes instalarlo a través de npm (Node Package Manager):

```bash
npm install lodash
```

O si estás usando una etiqueta de script en un HTML:

```html
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
```

### Ejemplos de Uso

#### 1. Manipulación de Arrays

**_.chunk**: Divide un array en fragmentos más pequeños de un tamaño específico.

```javascript
const _ = require('lodash');
let array = [1, 2, 3, 4, 5, 6];
let chunks = _.chunk(array, 2);
console.log(chunks); // [[1, 2], [3, 4], [5, 6]]
```

**_.difference**: Crea un array con los valores de la primer array que no están presentes en otros arrays.

```javascript
let array1 = [1, 2, 3];
let array2 = [2, 3, 4];
let difference = _.difference(array1, array2);
console.log(difference); // [1]
```

#### 2. Manipulación de Objetos

**_.merge**: Combina propiedades de objetos fuente en un objeto destino.

```javascript
let object1 = { 'a': 1, 'b': 2 };
let object2 = { 'b': 3, 'c': 4 };
let merged = _.merge(object1, object2);
console.log(merged); // { 'a': 1, 'b': 3, 'c': 4 }
```

**_.cloneDeep**: Crea una copia profunda de un objeto.

```javascript
let obj = { 'a': 1, 'b': { 'c': 2 } };
let clone = _.cloneDeep(obj);
console.log(clone); // { 'a': 1, 'b': { 'c': 2 } }
```

#### 3. Manipulación de Cadenas

**_.camelCase**: Convierte una cadena de texto a formato camel case.

```javascript
let text = 'hello world';
let camelCaseText = _.camelCase(text);
console.log(camelCaseText); // 'helloWorld'
```

**_.capitalize**: Capitaliza la primera letra de una cadena de texto.

```javascript
let text = 'hello world';
let capitalizedText = _.capitalize(text);
console.log(capitalizedText); // 'Hello world'
```

#### 4. Utilidades Variadas

**_.debounce**: Crea una función que retrasa la ejecución de la función original hasta que haya pasado un tiempo determinado desde la última vez que se invocó.

```javascript
const debouncedFunc = _.debounce(() => {
  console.log('Executed after 1 second of inactivity');
}, 1000);

// Ejecuta varias veces
debouncedFunc();
debouncedFunc();
debouncedFunc();
// Solo se ejecutará una vez, 1 segundo después de la última llamada
```

**_.throttle**: Crea una función que solo permite ejecutar la función original una vez cada intervalo de tiempo especificado.

```javascript
const throttledFunc = _.throttle(() => {
  console.log('Executed once every 2 seconds');
}, 2000);

// Ejecuta varias veces
throttledFunc();
throttledFunc();
throttledFunc();
// Solo se ejecutará una vez cada 2 segundos
```

### Uso Modular

Para optimizar el tamaño de tu paquete, puedes importar solo las funciones que necesitas:

```javascript
const chunk = require('lodash/chunk');
const merge = require('lodash/merge');

let array = [1, 2, 3, 4];
let chunks = chunk(array, 2);
console.log(chunks); // [[1, 2], [3, 4]]
```

Claro, aquí tienes ejemplos de cómo usar las funciones `_.reduce`, `_.keyBy`, `_.random`, `_.times` y `_.filter` de Lodash en JavaScript.

### 1. `_.reduce`

`_.reduce` aplica una función a un acumulador y a cada elemento de un array (de izquierda a derecha) para reducirlo a un solo valor.

```javascript
const _ = require('lodash');

let numbers = [1, 2, 3, 4, 5];

let sum = _.reduce(numbers, (accumulator, value) => {
  return accumulator + value;
}, 0);

console.log(sum); // 15
```

### 2. `_.keyBy`

`_.keyBy` crea un objeto compuesto de claves generadas a partir de las propiedades de cada elemento de la colección.

```javascript
const _ = require('lodash');

let users = [
  { 'id': '1', 'name': 'John' },
  { 'id': '2', 'name': 'Jane' },
  { 'id': '3', 'name': 'Jack' }
];

let usersById = _.keyBy(users, 'id');

console.log(usersById);
/*
{
  '1': { 'id': '1', 'name': 'John' },
  '2': { 'id': '2', 'name': 'Jane' },
  '3': { 'id': '3', 'name': 'Jack' }
}
*/
```

### 3. `_.random`

`_.random` genera un número aleatorio entre los valores inferior y superior dados, ambos inclusive.

```javascript
const _ = require('lodash');

let randomNumber = _.random(1, 10);

console.log(randomNumber); // Un número aleatorio entre 1 y 10
```

### 4. `_.times`

`_.times` invoca la función dada n veces, devolviendo un array de los resultados de cada invocación.

```javascript
const _ = require('lodash');

let result = _.times(5, String);

console.log(result); // ['0', '1', '2', '3', '4']
```

### 5. `_.filter`

`_.filter` crea un array con todos los elementos que pasan la prueba implementada por la función dada.

```javascript
const _ = require('lodash');

let users = [
  { 'name': 'John', 'active': true },
  { 'name': 'Jane', 'active': false },
  { 'name': 'Jack', 'active': true }
];

let activeUsers = _.filter(users, (user) => user.active);

console.log(activeUsers); 
/*
[
  { 'name': 'John', 'active': true },
  { 'name': 'Jack', 'active': true }
]
*/
```

### Resumen de las Funciones

- **`_.reduce`**: Reduce un array a un único valor aplicando una función a un acumulador y cada elemento del array.
- **`_.keyBy`**: Crea un objeto compuesto de claves generadas a partir de las propiedades de cada elemento de la colección.
- **`_.random`**: Genera un número aleatorio entre dos valores dados.
- **`_.times`**: Invoca una función dada un número específico de veces, devolviendo un array de los resultados.
- **`_.filter`**: Crea un array con todos los elementos que pasan la prueba implementada por una función dada.


### Resumen

Lodash es una biblioteca poderosa y flexible para JavaScript que facilita la manipulación de arrays, objetos, cadenas de texto y más. Al proporcionar funciones utilitarias comunes y optimizadas, ayuda a escribir código más limpio, legible y eficiente.
