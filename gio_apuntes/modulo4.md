# Modulo 4

* ## Loops

```python
var players = [
    'Altuve',
    'Bregman',
    'Correa',
    'Springer'
  ];


// for in :metodo mas moderno + sencillo y no hay que poner condiciones ni incrementador
// for: metodo antiguo
// forEach: metodo actual , el mejor  
  
  for (player in players) {
    console.log(players[player]);
  }
  
  for (var i = 0; i < players.length; i++) {
    console.log(players[i]);
  }
  
  players.forEach(function(element) {
    console.log(element);
  });
```

* ## Loops en un obejto

```python

var student = {
    name: 'Kristine',
    age: 12,
    city: 'Scottsdale'
  };
  
  for (var key in student) {
    console.log(key + " => " + student[key]);
  }
 // Bucle en una coleccion

```

* ## While and Do/While Loops

```python
var players = [
    'Altuve',
    'Bregman',
    'Correa',
    'Springer'
  ];
  
  var i = 0;
  while (i < players.length) {
    console.log(players[i]);
    i++;
  }
  
  var i = 21;
  do {
    console.log(players[i]);
    i++;
  } while (i < players.length)

// while hace la comprobacion condicional primero
// do while hace la comprobacion pasada una vez por el programa
```

* ## queryselector

```html
<div class="parent">
    <div class="decoy"></div>
    <div class="decoy"></div>
    <div class="target">You got this!</div>
    <div class="decoy"></div>
</div>
```

```javascript
var query =  document.querySelector(".target");
```

* ## Fundamentos de js moderno

* ### Variables: var / let  y const
  
Durante tiempo usamos **var** para declarar variables, pero eso generaba variabes globales, que se podian sobreescribir o modificar, llevando a errores.

Más tarde llego **let** y estan no contaminaban el espacio global ,pero seguia permitiendose sobreescribir.
ej:

```javascript    
let city ="barcelona";
console.log(city);

city ="Madrid";
console.log(city);

//en este caso se sobreescribe
```

* **const**
  Y por ultimo , llego **const**, esta es la que se usa actualmente. **No permite sobreescribir**

```javascript
const city ="barcelona";
console.log(city);

city ="Madrid";
console.log(city);

//en este caso NO se sobreescribe
```

* ### cadenas interpoladas

Se usan con ${ }, y es como meterle js en su interior. 

```javascript
const nombre = 'Juan';
const edad = 25;

// Usando concatenación de cadenas tradicional
const mensaje1 = 'Hola, mi nombre es ' + nombre + ' y tengo ' + edad + ' años.';
console.log(mensaje1);  // Hola, mi nombre es Juan y tengo 25 años.

// Usando plantillas de cadena para interpolación
const mensaje2 = `Hola, mi nombre es ${nombre} y tengo ${edad} años.`;
console.log(mensaje2);  // Hola, mi nombre es Juan y tengo 25 años.
```

Además de insertar variables, también puedes realizar expresiones dentro de la interpolación:

```javascript

const a = 5;
const b = 10;

const resultado = `La suma de ${a} y ${b} es ${a + b}.`;
console.log(resultado);  // La suma de 5 y 10 es 15.

```

* ### integrar condicionales en cadenas con operadores ternarios

```javascript

const page = 'Home';
console.log(`class=${ page === 'Home' ? 'master-layout' : 'secondary-layout' }`);
```

```javascript
var ship = "hit";

function battleShip() {
  return(ship === "hit" ? " 1 point" : "You lost a point");
}

var ship ="miss";
```

* ### función ARROW (FLECHA)

```javascript
// Same function written as function declaration
function fullName (fName, lName) { 
    console.log(`${lName}, ${fName}`);
  }
  fullName('Tiffany', 'Hudgens');
  
  // Same function written as function expression
  fullName = (fName, lName) => { 
    console.log(`${lName}, ${fName}`);
  }
  fullName('Kristine', 'Hudgens');
  
  // Basic arrow function
  helloWorld = () => { console.log("Hi there"); }
  helloWorld();
  
  // Arrow function with shorthand function argument for single arguments
  firstName = fname => { console.log(fname.toUpperCase()); }
  firstName('Jordan');
  
  // Arrow function with multiple arguments
  fullName = (fName, lName) => { console.log(`${lName}, ${fName}`); }
  fullName('Kristine', 'Hudgens');
```

* ### Deconstruccion de variables

```javascript
let playerOne = 'Tiffany';
let playerTwo = 'Kristine';

//let tempPlayerOne = playerOne;
//let tempPlayerTwo = playerTwo;

//playerOne = tempPlayerTwo;
//playerTwo = tempPlayerOne;

[playerOne, playerTwo] = [playerTwo, playerOne];

console.log(`
Player One: ${playerOne}
Player Two: ${playerTwo}
`);
```

* ### Deconstruccion de arrays 

```javascript
const apiList = [
  'https://api.dailysmarty.com/posts',
  'https://api.github.com/users/jordanhudgens/repos',
  'https://api.github.com/users/jordanhudgens'
]

const [posts, repos, profile] = apiList;

console.log(posts);
console.log(repos);
console.log(profile);
```

* ### Deconstruccion usando funciones

```javascript
const user = {
  name: 'Kristine',
  email: 'kristine@devcamp.com'
}

const renderUser = ({ name, email }) => {
  console.log(`${name}: ${email}`);
}

renderUser(user);
```

* ### Agregar valores de objetos predeterminados a argumentos de funciones

```javascript
const blog = {
  title: 'My great post',
  summary: 'Summary of my post'
}

const openGraphMetadata = ({ title, summary = 'A DailySmarty Post' }) => {
  console.log(`
    og-title=${title}
    og-description=${summary}
  `);
}

openGraphMetadata(blog);
```

* ### Operador de extensión (...)

```javascript

// Combining Arrays
let shoppingCart = [345, 375, 765, 123];
let newItems = [98, 123];

shoppingCart.push(...newItems);
console.log(shoppingCart); // [345, 375, 765, 123, 98, 123]

// Copying Arrays
const shoppingCart = [345, 375, 765, 123];
const updatedCart = [...shoppingCart];
updatedCart.push(5);
console.log(updatedCart);
console.log(shoppingCart);

const orderTotals = [1, 5, 1, 10, 2, 3];
console.log(Math.max(...orderTotals));

// [1, 5, 1, 10, 2, 3]
// ...[1, 5, 1, 10, 2, 3]
// 1, 5, 1, 10, 2, 3

const { starter, closer, ...relievers } = {
  starter: 'Verlander',
  closer: 'Giles',
  relief_1: 'Morton',
  relief_2: 'Gregerson'
}

console.log(starter);
console.log(closer);
console.log(relievers);
```

* ### Bind

```javascript
const userOne = {
  firstName: "Kristine",
  lastName: "Hudgens"
};

const userTwo = {
  firstName: "Tiffany",
  lastName: "Hudgens"
};

// Function expression
const fullName = function() {
  return `${this.lastName}, ${this.firstName}`;
};

// Nope!
// const fullName = () => {
//   return `${this.lastName}, ${this.firstName}`;
// };

const kristine = fullName.bind(userOne);
const tiffany = fullName.bind(userTwo);

kristine();
tiffany();
```

* ### Crear una funcion para comparar los valores de dos objetos

```javascript
const isEqual = (obj1, obj2) => {
  const obj1Keys = Object.keys(obj1);
  const obj2Keys = Object.keys(obj2);

  if (obj1Keys.length !== obj2Keys.length) {
    return false;
  }

  for (let objKey of obj1Keys) {
    if (obj1[objKey] !== obj2[objKey]) {
      return false;
    }
  }

  return true;
};

const obj1 = {
  name: "Kristine",
  age: 13,
  favorites: {
    food: "Pizza",
    vacation: "Disneyland"
  }
};

const obj2 = {
  name: "Kristine",
  age: 13,
  favorites: {
    food: "Pizza",
    vacation: "Disneyland"
  }
};

obj1 == obj2;
isEqual(obj1, obj2);
```
Esto funciona con objetos superficiales, que no tienen anidado nada, para esos casos hay que usar la libreria lodash library.

* ### Programacion orientada a objetos  OOP
  
* **Crear una clase e instanciarla**

```javascript
class Instructor {
  constructor({ name }) {
    this.name = name;
  }
}

const jon = new Instructor({ name: 'Jon Snow' });
console.log(jon.name); //imprime "Jon Snow"
console.log(jon.); //imprime  object { name="Jon Snow"}

```

* **Agregar métodos de instacia a una clase**

```javascript
class Instructor {
  constructor({ name, role = 'assistant' }) {
    this.name = name;
    this.role = role;
  }

  renderDetails() {
    console.log(`${this.name}: ${this.role}`);
  }
}

const jon = new Instructor({name: 'Jon Snow'});
const brayden = new Instructor({name: 'Brayden', role: 'teacher'});
jon.renderDetails();
brayden.renderDetails();
```

```javascript

class Car {
    constructor({ year, brand, poweredBy = 'gas' }) {
    this.year = year;
    this.brand = brand;
    this.poweredBy = poweredBy;
    }
    carSpecs() {
    return(`The ${this.year} ${this.brand} runs on ${this.poweredBy}`)
    }
}

const model3 = new Car({year: 1970, brand: "Tesla", poweredBy: "electricity"});//Write your code here
```

* **Métodos estaticos**

```javascript
class Instructor {
  constructor({ name, role = "assistant" }) {
    this.role = role;
    this.name = name;
  }

  // Instance method
  renderDetails() {
    console.log(`${this.name} - ${this.role}`);
  }

  // Base case static method
  static helloWorld() {
    console.log('Hi there');
  }

  // Static method
  static canTeach(instructor) {
    return (instructor.role === 'classroom');
  }
}

let juniorInstructor = new Instructor({ 'name' : 'Brian' });
let seniorInstructor = new Instructor({ 'name' : 'Alice', "role" : "classroom" });

juniorInstructor.renderDetails(); // "Brian - assistant"
seniorInstructor.renderDetails(); // "Alice - classroom"

Instructor.helloWorld(); // "Hi there"

// "Brian can teach: false"
console.log(
  `${juniorInstructor.name} can teach: ${Instructor.canTeach(juniorInstructor)}`
);

// "Alice can teach: true"
console.log(
  `${seniorInstructor.name} can teach: ${Instructor.canTeach(seniorInstructor)}`
);
```

* ## JSON

* Fue creado para ser un formato de datros universal, para usarse en todos los lenguajes y marcos.
* Es una forma de formatear datos en pares de atributos y valores.

¡Claro! JSON es una manera de organizar y compartir datos que es fácil de entender tanto para las personas como para las computadoras. Aquí tienes una explicación sencilla:

### ¿Qué es JSON?
- **JSON** significa **JavaScript Object Notation**.
- Es un formato de texto que se utiliza para almacenar y transferir datos.

### ¿Cómo se ve JSON?
JSON se parece mucho a una lista de cosas o a un diccionario de palabras y definiciones. Aquí hay un ejemplo sencillo de JSON que describe a una persona:

```json
{
  "nombre": "Juan",
  "edad": 30,
  "casado": true,
  "hijos": ["Ana", "Luis"],
  "direccion": {
    "calle": "Calle Falsa 123",
    "ciudad": "Madrid",
    "codigo_postal": "28013"
  }
}
```

### Elementos Básicos de JSON
1. **Llaves `{}`**: Se utilizan para agrupar datos en un objeto.
   - En el ejemplo, todo lo que está entre las llaves representa a una persona.
2. **Pares clave-valor**: Dentro de las llaves, los datos se organizan en pares.
   - `"nombre": "Juan"` es un par clave-valor. La clave es `"nombre"` y el valor es `"Juan"`.
3. **Comas `,`**: Separan los diferentes pares clave-valor.
   - `"edad": 30, "casado": true` separa la edad y el estado civil.
4. **Corchetes `[]`**: Se utilizan para listas de elementos.
   - `"hijos": ["Ana", "Luis"]` es una lista de hijos.

### Tipos de Datos en JSON
- **Cadenas de texto**: `"nombre": "Juan"`
- **Números**: `"edad": 30`
- **Booleanos** (verdadero o falso): `"casado": true`
- **Listas**: `"hijos": ["Ana", "Luis"]`
- **Objetos**: `"direccion": {"calle": "Calle Falsa 123", "ciudad": "Madrid", "codigo_postal": "28013"}`

### ¿Por qué es útil JSON?
- **Simplicidad**: Es fácil de leer y escribir tanto para humanos como para computadoras.
- **Interoperabilidad**: Diferentes sistemas y lenguajes de programación pueden utilizar JSON para comunicarse entre sí.
- **Estandarización**: Es un formato estándar ampliamente aceptado en la industria tecnológica.

### Un Ejemplo Real
Supongamos que tienes una aplicación de contactos en tu teléfono. La información de cada contacto puede estar almacenada en formato JSON. Así, cuando tu aplicación necesita mostrar tus contactos, lee el archivo JSON y muestra la información.

```json
[
  {
    "nombre": "Juan",
    "telefono": "123456789"
  },
  {
    "nombre": "María",
    "telefono": "987654321"
  }
]
```

En este ejemplo, hay una lista de contactos, cada uno con su nombre y número de teléfono.

**En Resumen**
JSON es simplemente una forma ordenada y fácil de leer para guardar y compartir datos. Es como un libro de registros que una computadora puede leer y escribir sin confundirse, y que a nosotros también nos resulta fácil de entender.

* ### Cree una función de exponente manual

```javascript
const toThePowerOf = (num, exp) => {
  const items = Array(exp).fill(num);
  const reducer = (accumulator, currentValue) => accumulator * currentValue;
  return items.reduce(reducer);
};

toThePowerOf(2, 3); //?
toThePowerOf(3, 3); //?
toThePowerOf(4, 2); //?
toThePowerOf(10, 10); //?
10 ** 10; //?
```

* ### Promises

Una promesa es un objeto que representa la eventual finalización (o fracaso) de una operación asincrónica y su valor resultante. Piensa en una promesa como en una promesa en la vida real: es algo que se hará en el futuro.

### Estados de una Promesa
Una promesa puede estar en uno de los tres estados siguientes:
1. **Pendiente (Pending)**: La operación aún no ha terminado.
2. **Cumplida (Fulfilled)**: La operación terminó con éxito.
3. **Rechazada (Rejected)**: La operación terminó con un error.

### Creando una Promesa

Para crear una promesa, se utiliza el constructor `Promise`, que toma una función con dos argumentos: `resolve` y `reject`. Aquí hay un ejemplo simple:

```javascript
let promesa = new Promise((resolve, reject) => {
  let exito = true; // Puedes cambiar esto a false para ver cómo funciona el rechazo.
  
  if (exito) {
    resolve("¡La operación fue exitosa!");
  } else {
    reject("Hubo un error en la operación.");
  }
});
```

### Usando una Promesa

Para manejar el resultado de una promesa, utilizamos los métodos `then` y `catch`.

- **`then`**: Se ejecuta cuando la promesa se cumple (es exitosa).
- **`catch`**: Se ejecuta cuando la promesa es rechazada (ocurre un error).

```javascript
promesa
  .then((mensaje) => {
    console.log(mensaje); // Esto se ejecuta si la promesa se resuelve.
  })
  .catch((error) => {
    console.error(error); // Esto se ejecuta si la promesa es rechazada.
  });
```

### Ejemplo de Uso Real

Imagina que quieres obtener datos de un servidor. Esto puede tomar tiempo, así que utilizamos una promesa para manejar la operación asincrónica:

```javascript
function obtenerDatos() {
  return new Promise((resolve, reject) => {
    setTimeout(() => { // Simula una operación asincrónica como una llamada a un servidor.
      let exito = true; // Cambia esto para simular éxito o fracaso.
      
      if (exito) {
        resolve("Datos obtenidos con éxito");
      } else {
        reject("Error al obtener datos");
      }
    }, 2000); // La operación tarda 2 segundos.
  });
}

obtenerDatos()
  .then((datos) => {
    console.log(datos); // Se ejecuta si la promesa se resuelve.
  })
  .catch((error) => {
    console.error(error); // Se ejecuta si la promesa es rechazada.
  });
```

### Promesas Encadenadas

Puedes encadenar varias promesas utilizando `then`. Cada `then` recibe el resultado del anterior:

```javascript
obtenerDatos()
  .then((datos) => {
    console.log(datos);
    return "Proceso los datos";
  })
  .then((resultado) => {
    console.log(resultado);
    return "Más procesamiento";
  })
  .then((final) => {
    console.log(final);
  })
  .catch((error) => {
    console.error(error); // Esto captura cualquier error en la cadena de promesas.
  });
```

### Resumen
Las promesas son una manera de manejar operaciones asincrónicas en JavaScript. Te permiten ejecutar código cuando una operación ha completado (con éxito o con error) y manejar esos resultados de manera estructurada y limpia.

```javascript
let sleepyGreeting = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Hello....')
  }, 2000);

  setTimeout(() => {
    reject(Error('Too sleepy...'))
  }, 2000);
});

sleepyGreeting
  .then(data => {
    console.log(data);
  })
  .catch(err => {
    console.error(err);
  });
```

* ## Promesas con un API
Ejemplo de cómo puedes crear una promesa en JavaScript para conectar con una API real. En este caso, usaré la API pública de JSONPlaceholder, que es un servicio gratuito que provee datos de prueba.

Este ejemplo realizará una solicitud para obtener una lista de publicaciones (posts):

```javascript
// Función para hacer una solicitud a la API
function fetchPosts() {
    // Crear una nueva promesa
    return new Promise((resolve, reject) => {
        // Usar fetch para hacer la solicitud GET a la API
        fetch('https://jsonplaceholder.typicode.com/posts')
            .then(response => {
                // Verificar si la respuesta es exitosa
                if (response.ok) {
                    return response.json();
                } else {
                    reject('Error en la solicitud');
                }
            })
            .then(data => {
                // Resolver la promesa con los datos obtenidos
                resolve(data);
            })
            .catch(error => {
                // Rechazar la promesa en caso de un error en la solicitud
                reject(error);
            });
    });
}

// Usar la función y manejar la promesa resultante
fetchPosts()
    .then(posts => {
        console.log('Lista de publicaciones:', posts);
    })
    .catch(error => {
        console.error('Hubo un problema con la solicitud:', error);
    });
```

### Explicación del código:

1. **Función `fetchPosts`**:
   * Esta función retorna una nueva promesa.
   * Dentro de la promesa, se utiliza `fetch` para realizar una solicitud HTTP GET a la URL `https://jsonplaceholder.typicode.com/posts`.

2. **Manejo de la respuesta**:
   * Si la respuesta es exitosa (`response.ok`), se convierte a formato JSON.
   * Si hay un error en la solicitud, la promesa se rechaza con un mensaje de error.

3. **Manejo de datos**:
   * Si la conversión a JSON es exitosa, la promesa se resuelve con los datos obtenidos.
   * Si hay un error durante el proceso de solicitud o conversión, la promesa se rechaza.

4. **Uso de la función**:
   * Se llama a `fetchPosts` y se maneja la promesa resultante con `.then` para procesar los datos y `.catch` para manejar cualquier error.

Este ejemplo te permite ver cómo trabajar con promesas y manejar solicitudes a una API en JavaScript de manera asíncrona.

* ## Agrupar Promesas (Promise all)

```javascript
const greeting = new Promise((resolve, reject) =>{
  resolve('Hi there');
  reject('Oops, bad greeting');
});

const updateAccount = new Promise((resolve, reject) => {
  resolve('Updating last login...');
  reject('Error updating account with login.');
});

const loginActivities = Promise.all([greeting, updateAccount]);

loginActivities.then(res => {
  res.forEach(activity => {
    console.log(activity);
  })
})
```

* ## Async and Await
  
En las versiones modernas de Js se soluciono el problema con la devolucion de llamada:
El problema principal con las devoluciones de llamada (callbacks) en JavaScript, especialmente antes de la introducción de las promesas y `async/await`, se conoce comúnmente como "callback hell" o "pyramid of doom". Aquí hay una breve explicación de estos problemas:

### 1. **Anidamiento Extremo (Callback Hell)**:

   * Cuando se tienen múltiples operaciones asíncronas que dependen unas de otras, las devoluciones de llamada se anidan profundamente.
   * Este anidamiento hace que el código sea difícil de leer y mantener.
     
   ```javascript
   doSomething(function(result1) {
       doSomethingElse(result1, function(result2) {
           doAnotherThing(result2, function(result3) {
               doSomethingMore(result3, function(result4) {
                   // ...
               });
           });
       });
   });
   ```

### 2. **Dificultad para Manejar Errores**:
   * Manejar errores en un flujo de devoluciones de llamada puede ser complicado.
   * Cada nivel de anidamiento necesita su propio manejo de errores, lo cual incrementa la complejidad del código.

   ```javascript
   doSomething(function(err, result1) {
       if (err) {
           // manejar error
       } else {
           doSomethingElse(result1, function(err, result2) {
               if (err) {
                   // manejar error
               } else {
                   doAnotherThing(result2, function(err, result3) {
                       if (err) {
                           // manejar error
                       } else {
                           // ...
                       }
                   });
               }
           });
       }
   });
   ```

### 3. **Código Difícil de Leer y Mantener**:
   * Con callbacks profundamente anidados, el código se vuelve difícil de leer y seguir.
   *-* La estructura anidada crea una "pirámide de la perdición" que complica la comprensión del flujo lógico del programa.

### Soluciones con Promesas y `async/await`:

- **Promesas**:
  - Las promesas ayudan a aplanar el código y manejar errores de manera más sencilla usando `.then` y `.catch`.

  ```javascript
  doSomething()
      .then(result1 => doSomethingElse(result1))
      .then(result2 => doAnotherThing(result2))
      .then(result3 => doSomethingMore(result3))
      .catch(err => {
          // manejar error
      });
  ```

- **`async/await`**:
  - La sintaxis `async/await` permite escribir código asíncrono que se ve y se comporta como código síncrono, haciendo el código más limpio y fácil de seguir.

  ```javascript
  async function doAll() {
      try {
          const result1 = await doSomething();
          const result2 = await doSomethingElse(result1);
          const result3 = await doAnotherThing(result2);
          const result4 = await doSomethingMore(result3);
          // ...
      } catch (err) {
          // manejar error
      }
  }

  doAll();
  ```

### Conclusión

Las devoluciones de llamada eran una forma fundamental de manejar operaciones asíncronas en JavaScript, pero traían consigo problemas de legibilidad y mantenibilidad. Las promesas y `async/await` fueron introducidos para resolver estos problemas, proporcionando una forma más estructurada y comprensible de manejar la asincronía en JavaScript.

ejemplo Devcamp:

```javascript
const login = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('User logged in...');
    }, 2000);
  });
}

const updateAccount = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Updating last login...');
    }, 2000);
  });
}

async function loginActivities() {
  const returnedLogin = await login();
  console.log(returnedLogin);

  const returnedUpdateAccount = await updateAccount();
  console.log(returnedUpdateAccount);
}

loginActivities();
```

* ## Clausuras
Claro, los closures (o cierres) son una característica fundamental y poderosa de JavaScript. Para entender los closures, es importante tener una comprensión básica de las funciones y el alcance (scope) en JavaScript.

### ¿Qué es un Closure?

Un closure es una función que recuerda el estado de las variables de su entorno léxico (scope) incluso después de que el entorno en el que fue creada haya terminado su ejecución.

En otras palabras, un closure permite que una función acceda a variables fuera de su propio ámbito (scope), pero dentro del ámbito en el que fue definida, incluso después de que dicho ámbito haya dejado de existir.

### Ejemplo Básico de Closure

```javascript
function createCounter() {
    let count = 0; // Variable dentro del alcance de createCounter

    return function() {
        count += 1;
        return count;
    };
}

const counter = createCounter();
console.log(counter()); // Output: 1
console.log(counter()); // Output: 2
console.log(counter()); // Output: 3
```

### Explicación del Ejemplo

1. **Función `createCounter`**:
   - Declara una variable `count` inicializada en 0.
   - Retorna una función anónima.

2. **Función Anónima Retornada**:
   - Incrementa el valor de `count` y retorna el nuevo valor.
   - Esta función tiene acceso a la variable `count` debido al closure.

3. **Uso del Closure**:
   - Cuando `createCounter` es llamada, retorna la función anónima.
   - Esta función anónima recuerda el valor de `count` y puede modificarlo, aunque el contexto de `createCounter` haya terminado.

### Más Ejemplos de Closures

#### Ejemplo con Múltiples Closures

```javascript
function createCounter() {
    let count = 0;

    return {
        increment: function() {
            count += 1;
            return count;
        },
        decrement: function() {
            count -= 1;
            return count;
        },
        getCount: function() {
            return count;
        }
    };
}

const counter = createCounter();
console.log(counter.increment()); // Output: 1
console.log(counter.increment()); // Output: 2
console.log(counter.decrement()); // Output: 1
console.log(counter.getCount());  // Output: 1
```

#### Ejemplo con Funciones que Crean Funciones

```javascript
function makeMultiplier(multiplier) {
    return function(number) {
        return number * multiplier;
    };
}

const double = makeMultiplier(2);
const triple = makeMultiplier(3);

console.log(double(5)); // Output: 10
console.log(triple(5)); // Output: 15
```

### Beneficios y Usos Comunes de los Closures

1. **Encapsulación**:
   - Permiten encapsular datos y lógica, evitando la exposición de variables internas.

2. **Manejo de Estado**:
   - Utilizados para crear funciones que mantienen su propio estado interno sin depender de variables globales.

3. **Callbacks y Asincronía**:
   - Muy útiles en patrones de programación asíncrona y en el uso de callbacks, ya que permiten que una función acceda al estado de su entorno incluso después de que el entorno haya finalizado.

4. **Módulos**:
   - Ayudan en la creación de módulos en JavaScript, proporcionando una manera de crear funciones y variables privadas.

### Conclusión

Los closures son una característica poderosa en JavaScript que permite a las funciones recordar y acceder a su contexto léxico, lo que habilita una variedad de patrones de diseño y facilita la programación asíncrona y modular. Entender los closures es crucial para escribir código JavaScript más efectivo y eficiente.

ejemplo Devcamp

```javascript
const login = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('User logged in...');
    }, 4000);
  });
}

const updateAccount = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Updating last login...');
    }, 2000);
  });
}

async function loginActivities(login, updateAccount) {
  const returnedLogin = await login;
  console.log(returnedLogin);

  const returnedUpdateAccount = await updateAccount;
  console.log(returnedUpdateAccount);
}

loginActivities(login(), updateAccount());
```

(https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/combining-async-await-closures-ensure-all-processes-run)


* ## Usar Async/Awaiy para cominicar con APIS externos

(https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/using-async-await-communicating-outside-apis-javascript)

```javascript
async function queryApis() {
  const postsPromise = fetch('https://api.dailysmarty.com/posts');
  const posts = await postsPromise.then(res => res.json());
  console.log(posts);

  const reposPromise = fetch('https://api.github.com/users/jordanhudgens/repos');
  const repos = await reposPromise.then(res => res.json());
  console.log(repos);
}

queryApis();
```

Ejemplo de cómo usar `async` y `await` para comunicarte con dos APIs diferentes en JavaScript. En este caso, usaré la API de JSONPlaceholder para obtener una lista de publicaciones y luego obtener los detalles de un usuario basándome en el ID del primer autor de esas publicaciones.

### Paso a Paso:

1. **Primero**, obtener una lista de publicaciones de la API de JSONPlaceholder.
2. **Segundo**, usar el ID del autor de la primera publicación para obtener los detalles del usuario de otra llamada a la API.

### Código de Ejemplo:

```javascript
// Función asíncrona para obtener publicaciones
async function fetchPosts() {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts');
        if (!response.ok) {
            throw new Error('Error al obtener las publicaciones');
        }
        const posts = await response.json();
        return posts;
    } catch (error) {
        console.error('Hubo un problema con la solicitud de publicaciones:', error);
    }
}

// Función asíncrona para obtener detalles del usuario
async function fetchUser(userId) {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
        if (!response.ok) {
            throw new Error('Error al obtener los detalles del usuario');
        }
        const user = await response.json();
        return user;
    } catch (error) {
        console.error('Hubo un problema con la solicitud de detalles del usuario:', error);
    }
}

// Función principal para coordinar las solicitudes a las APIs
async function main() {
    try {
        // Obtener publicaciones
        const posts = await fetchPosts();
        if (!posts || posts.length === 0) {
            throw new Error('No se encontraron publicaciones');
        }

        // Obtener el ID del autor de la primera publicación
        const firstPost = posts[0];
        const userId = firstPost.userId;

        // Obtener detalles del usuario
        const user = await fetchUser(userId);

        // Mostrar los resultados
        console.log('Primera publicación:', firstPost);
        console.log('Detalles del autor:', user);
    } catch (error) {
        console.error('Hubo un problema en el flujo principal:', error);
    }
}

// Llamar a la función principal
main();
```

### Explicación del Código:

1. **Funciones Asíncronas `fetchPosts` y `fetchUser`**:
   - **`fetchPosts`**: Realiza una solicitud `fetch` para obtener las publicaciones. Si la respuesta es exitosa, convierte la respuesta a JSON y la retorna. Si hay un error, lo maneja y muestra en la consola.
   - **`fetchUser`**: Similar a `fetchPosts`, pero realiza la solicitud para obtener los detalles de un usuario específico basándose en el `userId`.

2. **Función `main`**:
   - **Obtener Publicaciones**: Llama a `fetchPosts` y obtiene la lista de publicaciones. Si no hay publicaciones, lanza un error.
   - **Obtener ID del Usuario**: Toma el ID del autor de la primera publicación.
   - **Obtener Detalles del Usuario**: Usa el ID del usuario para llamar a `fetchUser` y obtener los detalles del autor.
   - **Mostrar Resultados**: Imprime la primera publicación y los detalles del usuario en la consola.

3. **Llamada a la Función `main`**:
   - Se llama a `main` para ejecutar el flujo completo.

### Notas:

- **Manejo de Errores**: Cada función `async` usa `try...catch` para manejar posibles errores durante las solicitudes.
- **Legibilidad**: El uso de `async` y `await` hace que el código sea más legible y se asemeje a un código síncrono, a pesar de ser asíncrono.

Este patrón es muy útil para coordinar múltiples llamadas a APIs y manejar sus resultados de manera ordenada y comprensible.

* ## Implementación del manejo de errores en una función Async/Await

(https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/implementing-error-handling-javascript-async-await-function)

```javascript
async function queryApis() {
  try {
    const postsPromise = fetch('http://api.dailysmarty.com/posts');
    const posts = await postsPromise.then(res => res.json());
    console.log(posts);
  } catch(err) {
    console.log(err);
    console.log('There was an error with the DailySmarty API');
  }

  try {
    const reposPromise = fetch('https://api.github.com/users/jordanhudgens/repos');
    const repos = await reposPromise.then(res => res.json());
    console.log(repos);
  } catch(err) {
    console.log(err);
    console.log('There was an error with the GitHub API');
  }
}

queryApis();
```

---
El manejo de errores es crucial cuando se trabaja con funciones asíncronas en JavaScript usando `async` y `await`. Aquí te muestro cómo implementar el manejo de errores en una función `async/await`.

### Ejemplo de Implementación de Manejo de Errores

Vamos a implementar una función que realiza una solicitud a una API y maneja posibles errores utilizando `try...catch`.

#### Función para Obtener Datos de una API con Manejo de Errores

```javascript
async function fetchData(url) {
    try {
        const response = await fetch(url);
        // Verificar si la respuesta es exitosa
        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        // Manejo de errores
        console.error('Hubo un problema con la solicitud:', error.message);
        // Puedes decidir cómo manejar el error: lanzar el error, retornar un valor por defecto, etc.
        throw error; // Re-lanzar el error para que sea manejado en otra parte si es necesario
    }
}

// Uso de la función con manejo de errores
async function main() {
    const url = 'https://jsonplaceholder.typicode.com/posts/1';

    try {
        const postData = await fetchData(url);
        console.log('Datos obtenidos:', postData);
    } catch (error) {
        console.error('Error al obtener los datos en la función principal:', error.message);
    }
}

main();
```

### Explicación del Código

1. **Función `fetchData`**:
   - **`try` Bloque**:
     - Intenta ejecutar la solicitud `fetch` a la URL proporcionada.
     - Verifica si la respuesta es exitosa (`response.ok`).
     - Si no es exitosa, lanza un error con un mensaje que incluye el código de estado y el texto de estado.
     - Si la respuesta es exitosa, convierte la respuesta a JSON y la retorna.
   - **`catch` Bloque**:
     - Captura cualquier error que ocurra durante la solicitud o la conversión a JSON.
     - Imprime un mensaje de error en la consola.
     - Lanza el error nuevamente si es necesario manejarlo en otro lugar.

2. **Función `main`**:
   - Llama a `fetchData` y maneja posibles errores.
   - Si `fetchData` lanza un error, `main` lo captura y muestra un mensaje de error en la consola.

### Notas Adicionales

- **Re-Lanzamiento de Errores**: En el bloque `catch` de `fetchData`, el error se lanza nuevamente (`throw error`) para permitir que el error sea manejado por el llamador de `fetchData`, en este caso, la función `main`.
- **Manejo de Errores Centralizado**: Este enfoque permite un manejo de errores centralizado y específico para cada operación asíncrona. Puedes decidir cómo manejar los errores en diferentes niveles de tu aplicación.
- **Mensajes de Error Informativos**: Incluir información específica en los mensajes de error (como el código de estado de la respuesta) ayuda a diagnosticar y solucionar problemas más fácilmente.

Este patrón de manejo de errores usando `try...catch` en funciones `async/await` es esencial para construir aplicaciones robustas y mantener un flujo de control claro y manejable en operaciones asíncronas.

* ## Construir una función de lotería ponderada 

(https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/build-weighted-lottery-function-javascript)

```javascript
const weightedLottery = weights => {
  let containerArray = [];

  Object.keys(weights).forEach(key => {
    for (let i = 0; i < weights[key]; i++) {
      containerArray.push(key);
    }
  });

  return containerArray[(Math.random() * containerArray.length) | 0];
};

const weights = {
  green: 1,
  yellow: 2,
  red: 3
};

weightedLottery(weights);
```
--- 