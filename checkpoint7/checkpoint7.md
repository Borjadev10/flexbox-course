
# Borja Gonzalvo Checkpoint 7

---

* ## ¿Qué diferencia a Javascript de cualquier otro lenguaje de programación?

* Las diferencia de JavaScript comparadas con otros lenguajes de programación es que se **ejecuta en el navegador.**
* A diferencia de otros lenguajes de programación , JavaScript se ejecuta directamente en los navegadores web, lo que nos permite **crear contenido dinámico y modificar la página web sin tener que recargarla.**
* JavaScript se ejecuta en el navegador del usuario, lo que significa que puedes hacer cosas directamente en la página web sin necesidad de depender de un servidor.
* En otros lenguajes de programación, requiere el uso de un servidor.
* JavaScript nos permite interactuar con el contenido  y el estilo de una página web de manera dinámica.
* JavaScript es un lenguaje interpretado, se ejecuta en tiempo real en el navegador del usuario, lo que permite respuestas rápidas a las acciones del usuario sin necesidad de compilar el código.
* En otros lenguajes(Java y C++) son lenguajes compilados que necesitan ser transformados en código máquina antes de ejecutarse, lo que genera un desarrollo mas lento.
* JavaScript es el único lenguaje de programación que soportado por todos los navegadores web.
* En lenguajes como Python, Ruby, y PHP se usan principalmente en el lado del servidor y requieren diferentes lenguajes (como JavaScript) para la funcionalidad del lado del cliente.
* JavaScript permite trabajar con una amplia gama de frameworks y librerías (React, Angular, Vue.js, jQuery) lo que facilita crear aplicaciones web avanzadas y muy interactivas.
* En otros lenguajes estos frameworks (como Django para Python, Ruby on Rails para Ruby),estan más enfocados en el desarrollo del lado del servidor y no en la manipulación del cliente.

Con **Node.js**, JavaScript se puede usar tanto en el cliente como en el servidor, permitiendo a los desarrolladores trabajar en ambos lados con el mismo lenguaje.

* JavaScript permite modificar elementos HTML y CSS en una página web, haciendo que puedas cambiar el contenido y el estilo de la página en tiempo real.
>
**Ejemplo comparativo entre lenguajes**

En este ejemplo vemos como mostrar un mensaje en respuesta a un clic en un botón.

En JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejemplo de JavaScript</title>
</head>
<body>
    <button onclick="mostrarMensaje()">Haz clic aquí</button>

    <script>
        function mostrarMensaje() {
            alert("¡Hola! Esto es JavaScript en acción.");
        }
    </script>
</body>
</html>
```

 En Python con Flask :

```python
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ejemplo de Flask</title>
        </head>
        <body>
            <button onclick="mostrarMensaje()">Haz clic aquí</button>

            <script>
                function mostrarMensaje() {
                    alert("¡Hola! Esto es JavaScript en acción.");
                }
            </script>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
```

En este ejemplo:
Con JavaScript  la interaccion entre el usuario y la respuesta  se da en el navegador.
Con Python se necesita un servidor web para enviar la página al navegador, donde aún se necesita JavaScript para la interacción del usuario.

---

* ## ¿Cuáles son algunos tipos de datos JS?

JavaScript utiliza varios tipos de datos para almacenar diferentes tipos de información.

Los principales tipos de datos en JavaScript son:

**Números (Number)**
Los utilizamos para trabajar con números, tanto enteros como decimales.

```javascript
    let entero = 52;
    let decimal = 3.14;
```

**Cadenas de texto (String)**
Los utilizamos para representar texto. Las cadenas se pueden definir con comillas simples (`'`), dobles (`"`) o backticks (`` ` ``) para plantillas de cadena.

```javascript
     let saludo = "Hola, mundo!";
     let nombre = 'Borja Gonzalvo';
     let presentacion = `Mi nombre es ${nombre}`;
```

**Booleanos (Boolean)**
Solo pueden ser `true` (verdadero) o `false` (falso).

```javascript
    let esVerdad = true;
    let esFalso = false;
```

**Objetos (Object)**
Colecciones de pares clave-valor. Los objetos se usan para almacenar colecciones de datos y entidades más complejas.

```javascript
    let persona = {
         nombre: "Borja",
         edad: 43,
         esconductor: true
         };
```

**Arreglos (Array)**
Listas ordenadas de elementos. Los arreglos son un tipo especial de objeto.
  
```javascript
     let colores = ["rojo", "verde", "azul"];
```

**Nulo (Null)**
Es la ausencia de cualquier valor. Es un valor asignable.

```javascript
    let sinValor = null;
```

**Indefinido (Undefined)**
   Indica que una variable ha sido declarada pero aún no tiene un valor asignado.

```javascript
    let valorIndefinido;
 ```

**Símbolos (Symbol)**
Representa un valor único y inmutable, principalmente usado como identificadores únicos para las propiedades de los objetos.
  
```javascript
    let id = Symbol('id');
```

**BigInt**
Representa números enteros de gran tamaño que exceden el rango de los números `Number` normales.

```javascript
    let numeroGrande = BigInt(98785123456789012345678901234567890);
```

Ejemplo con varios de estos tipos utilizandose :

```javascript

// Números
let edad = 43;

// Cadenas de texto
let nombre = "Borja";

// Booleanos
let esconductor = true;

// Objetos
let persona = {
    nombre: "Borja",
    edad: 43,
    esconductor: true
};

// Arreglos
let ciudadesFavoritas = ["Barcelona", "Madrid", "Bilbao"];

// Nulo
let sinValor = null;

// Indefinido
let valorIndefinido;

// Símbolos
let id = Symbol('id');

// BigInt
let numeroGrande = BigInt(999998765432101234567890);

```

---

* ## ¿Cuáles son las tres funciones de String en JS?

En JavaScript existen muchas de funciones para manipular y trabajar con cadenas de texto (strings).
Algunas de las funciones más comunes son:

#### Funciones para Manipulación y Búsqueda

**`length`**
La propiedad `length` te permite obtener la longitud de una cadena, es decir, cuántos caracteres contiene.

```javascript
let mensaje = "Hola, mundo!";
console.log(mensaje.length);
```

**`charAt(index)`**
Devuelve el carácter en la posición especificada (índice) de una cadena,los índices comienzan desde 0.

```javascript
let mensaje = "Hola, mundo!";
console.log(mensaje.charAt(0)); // Muestra "H"
console.log(mensaje.charAt(7)); // Muestra "m"
```

**`substring(startIndex, endIndex)`**
El método `substring()` devuelve una parte de la cadena entre los índices `startIndex` (inclusive) y `endIndex` (exclusivo). Si solo se proporciona `startIndex`, devuelve la cadena desde ese índice hasta el final.

```javascript
let mensaje = "Hola, mundo!";
console.log(mensaje.substring(0, 4)); // Muestra "Hola"
console.log(mensaje.substring(5)); // Muestra "mundo!"
```

**`slice(startIndex, endIndex)`**
Devuelve una parte de la cadena entre `startIndex` (inclusive) y `endIndex` (exclusivo). Permite índices negativos para contar desde el final de la cadena.

```javascript
let mensaje = "Hola, mundo!";
console.log(mensaje.slice(0, 4)); // Muestra "Hola"
console.log(mensaje.slice(-6)); // Muestra "mundo!"
```

#### Funciones para Búsqueda y Verificación

**`indexOf(substring)`**
El método `indexOf()` devuelve el índice de la primera aparicion de `substring` dentro de la cadena, o `-1` si no se encuentra.

```javascript
let mensaje = "Hola, mundo!";
console.log(mensaje.indexOf("mundo")); // Muestra 6
console.log(mensaje.indexOf("amigo")); // Muestra -1 (no encontrado)
```

**`lastIndexOf(substring)`**
Parecido a `indexOf()`, pero devuelve el índice de la última ocurrencia de `substring` dentro de la cadena, o `-1` si no se encuentra.

```javascript
let mensaje = "Hola, mundo! Hola!";
console.log(mensaje.lastIndexOf("Hola")); // Muestra 12
console.log(mensaje.lastIndexOf("amigo")); // Muestra -1 (no encontrado)
```

**`includes(substring)`**
El método `includes()` verifica si la cadena contiene `substring` y devuelve `true` o `false`.

```javascript
let mensaje = "Hola, mundo!";
console.log(mensaje.includes("mundo")); // true
console.log(mensaje.includes("amigo")); // false
```

#### Funciones para Transformación y Modificación

**`toUpperCase()`**
Convierte todos los caracteres de la cadena a mayúsculas.

```javascript
let minusculas = "hola";
let mayusculas = minusculas.toUpperCase();
console.log(mayusculas); // Muestra "HOLA"
```

**`toLowerCase()`**
Convierte todos los caracteres de la cadena a minúsculas.

```javascript
let mayusculas = "HOLA";
let minusculas = mayusculas.toLowerCase();
console.log(minusculas); // Muestra "hola"
```

**`trim()`**
Elimina los espacios en blanco al inicio y al final de la cadena.

```javascript
let espacio = "   Hola, mundo!   ";
let sinEspacio = espacio.trim();
console.log(sinEspacio); // Muestra "Hola, mundo!"
```

#### Funciones para Sustitución y Separación

**`replace(searchValue, newValue)`**
El método `replace()` busca `searchValue` en la cadena y lo reemplaza por `newValue`.

```javascript
let mensaje = "Hola, amigo!";
let nuevoMensaje = mensaje.replace("amigo", "mundo");
console.log(nuevoMensaje); // Muestra "Hola, mundo!"
```

**`split(delimiter)`**
El método `split()` divide la cadena en un array de subcadenas utilizando `delimiter` como separador.

```javascript
let lista = "manzana,naranja,uva";
let frutas = lista.split(",");
console.log(frutas); // Muestra ["manzana", "naranja", "uva"]
```

---

* ## ¿Qué es un condicional?

Para que un lenguaje de programación como JavaScript,pueda, en su código tomar decisiones, utilizamos un condicional.

Es como cuando en la vida real decidimos hacer o no hacer algo dependiendo de una condición.
Por ejemplo, si está lloviendo, vamos en coche; si no está lloviendo, vamos a pie.

En JavaScript, un condicional es una estructura de control que permite ejecutar diferentes bloques de código dependiendo de si una condición se evalúa como verdadera o falsa.
Los condicionales son fundamentales para tomar decisiones en el flujo de un programa.

### Tipos de Condicionales en JavaScript

#### **`if` (Si)**
`if` es como decir "si algo es verdadero, haz esto". 

```javascript
let haceFrio = true; // Imagina que esto es como una declaración que dice que hace frío.

if (haceFrio) { // Aquí estamos diciendo: "si hace frío es verdadero, haz lo siguiente".
    console.log("Ponte una chaqueta"); // Este es el mensaje que verás si haceFrio es verdadero.
}
```

En este ejemplo, `haceFrio` es verdadero, por lo que el mensaje "Ponte una chaqueta" aparecerá.

#### **`if...else` (Si...si no)**
`if...else` es como decir "si algo es verdadero, haz esto; si no, haz otra cosa".

```javascript
let esDeDia = false; // Aquí decimos que no es de día.

if (esDeDia) { // "si es de día es verdadero"
    console.log("Buenos días");
} else { // "si no"
    console.log("Buenas noches");
}
```
En este ejemplo, como `esDeDia` es falso, verás el mensaje "Buenas noches".

#### **`if...else if...else` (Si...si no, si...si no)**
A veces, tienes varias condiciones para verificar. Esto es como decir "si algo es verdadero, haz esto; si no, si otra cosa es verdadera, haz eso; si no, haz otra cosa".

```javascript
let temperatura = 25;

if (temperatura > 30) { // "si la temperatura es mayor que 30"
    console.log("Hace mucho calor");
} else if (temperatura > 20) { // "si no, si la temperatura es mayor que 20"
    console.log("El clima es agradable");
} else { // "si no"
    console.log("Hace frío");
}
```

En este ejemplo, como la temperatura es 25, verás el mensaje "El clima es agradable" porque está entre 21 y 30 grados.

#### **`switch` (Cambiar)**
El `switch` es como elegir entre varias opciones específicas. Es útil cuando tienes muchos casos posibles.

```javascript
let diaDeLaSemana = 3;
let nombreDelDia;

switch (diaDeLaSemana) {
    case 1: // Si es 1
        nombreDelDia = "Lunes";
        break; // Detén aquí y no sigas con los otros casos
    case 2: // Si es 2
        nombreDelDia = "Martes";
        break;
    case 3: // Si es 3
        nombreDelDia = "Miércoles";
        break;
    case 4: // Si es 4
        nombreDelDia = "Jueves";
        break;
    case 5: // Si es 5
        nombreDelDia = "Viernes";
        break;
    case 6: // Si es 6
        nombreDelDia = "Sábado";
        break;
    case 7: // Si es 7
        nombreDelDia = "Domingo";
        break;
    default: // Si no es ninguno de los anteriores
        nombreDelDia = "Día inválido";
}

console.log(nombreDelDia); // Muestra el nombre del día
```

En este ejemplo, como `diaDeLaSemana` es 3, verás "Miércoles".

Estos condicionales ayudan al programa a decidir qué hacer en diferentes situaciones.

Los condicionales en JavaScript permiten tomar decisiones en el flujo del programa.

Estas estructuras permiten que tu programa tome diferentes caminos de ejecución basados en los valores de las variables y las condiciones que definas.

---

* ## ¿Qué es un operador ternario?

Un operador ternario es:

* Una forma compacta y clara de escribir una estructura condicional `if...else` en una sola línea.
* Una herramienta poderosa para simplificar y hacer más expresivas las estructuras condicionales, ideal para situaciones donde se necesita tomar decisiones simples basadas en una condición booleana.
  
Se le llama ternario porque implica tres partes principales:una expresión condicional seguida de dos expresiones posibles separadas por un signo de interrogación (`?`) y un colon (`:`).
Sintaxis:

```python

condicion ? valorSiVerdadero : valorSiFalso

```

### Componentes del Operador Ternario:

- **Condición**: Es una expresión que se evalúa como verdadera (`true`) o falsa (`false`).
  
- **valorSiVerdadero**: Es el valor que se retorna si la condición es verdadera.

- **valorSiFalso**: Es el valor que se retorna si la condición es falsa.

**Ejemplo:**

```javascript
let edad = 20;
let mensaje = edad >= 18 ? "Eres mayor de edad" : "Eres menor de edad";

console.log(mensaje); // Muestra "Eres mayor de edad"
```

En este ejemplo:
- La condición `edad >= 18` se evalúa como verdadera porque la edad es 20.
- Si la condición es verdadera, se retorna el primer valor después del `?`, que es `"Eres mayor de edad"`.
- Si la condición es falsa, se retorna el segundo valor después del `:`, que es `"Eres menor de edad"` (aunque en este caso no es necesario porque la condición es verdadera).

### Ventajas del Operador Ternario:

- **Concisión**: Permite escribir estructuras condicionales de forma más compacta y legible, especialmente para casos simples.
  
- **Legibilidad**: Mejora la legibilidad del código al reducir la cantidad de líneas y al ser fácil de entender para desarrolladores familiarizados con el operador ternario.

### Consideraciones:

- **Uso Adecuado**: Aunque es útil y mejora la legibilidad en casos sencillos, el uso excesivo de operadores ternarios puede hacer que el código sea más difícil de mantener y entender, especialmente cuando las condiciones y los valores son complejos.

Ejemplo que muestra cómo podrías usar tanto un operador ternario como una estructura condicional `if...else` para determinar si una persona puede votar en función de su edad en JavaScript:

**Ejemplo con Operador Ternario:**

```javascript
let edad = 20;
let puedeVotar = edad >= 18 ? "Puede votar" : "No puede votar";

console.log(puedeVotar); // Muestra "Puede votar"
```

En este ejemplo con operador ternario:
La condición `edad >= 18` se evalúa como verdadera porque la edad es 20.
Como la condición es verdadera, se asigna el valor `"Puede votar"` a la variable `puedeVotar`.

**Ejemplo con Estructura Condicional `if...else`:**

```javascript
let edad = 15;
let puedeVotar;

if (edad >= 18) {
    puedeVotar = "Puede votar";
} else {
    puedeVotar = "No puede votar";
}

console.log(puedeVotar); // Muestra "No puede votar"
```

En este ejemplo con estructura condicional `if...else`:
La condición `edad >= 18` se evalúa como falsa porque la edad es 15.
Por lo tanto, se ejecuta el bloque de código dentro del `else`, y se asigna el valor `"No puede votar"` a la variable `puedeVotar`.

En los dos ejemplos logramos el mismo resultado, que es determinar si una persona puede votar basado en su edad. La elección entre usar un operador ternario o una estructura `if...else` en este caso depende de la preferencia del desarrollador y de la complejidad de la lógica que se quiera expresar. 

**Operador Ternario**: Es útil para expresiones simples y directas, donde se desea asignar un valor basado en una condición de forma concisa.
  
**Estructura `if...else`**: Es más adecuada cuando se necesita realizar múltiples comprobaciones o cuando la lógica condicional es más compleja y necesita más líneas de código.

En general, el operador ternario es especialmente útil cuando se desea asignar un valor a una variable en función de una condición simple y clara, mientras que la estructura `if...else` es más versátil para manejar lógicas condicionales más complejas y extensas.

---

* ## ¿Cuál es la diferencia entre una declaración de función y una expresión de función?

### Declaración de Función:
Imagina que quieres hacer una lista de tareas para un día ocupado. Decidiste escribir una lista en una hoja de papel antes de empezar tu día.
**Ejemplo:**

```javascript
function hacerTareas() {
    console.log("1. Limpia la habitación.");
    console.log("2. Haz la cama.");
    console.log("3. Lava los platos.");
}

// Llamada a la función
hacerTareas();
```

En este caso:
La declaración de función es como escribir una lista de tareas en una hoja de papel antes de hacerlas.
`hacerTareas` es el nombre que le das a tu lista de tareas. Puedes llamarla en cualquier momento para realizar esas acciones específicas que escribiste.

### Expresión de Función:

Ahora, imagina que no estás seguro de qué tareas necesitas hacer hasta que comienzas tu día. Decides escribir las tareas en una nota adhesiva que puedes pegar en tu escritorio para recordarlas más tarde.
**Ejemplo:**

```javascript
const prepararDesayuno = function() {
    console.log("1. Haz café.");
    console.log("2. Prepara tostadas.");
    console.log("3. Corta fruta.");
};

// Llamada a la función
prepararDesayuno();
```

En este caso:

* La expresión de función es como escribir una lista de tareas en una nota adhesiva que puedes colocar en tu escritorio cuando las necesites.
* `prepararDesayuno` es una nota adhesiva con las acciones que necesitas hacer para preparar el desayuno. Puedes llamarla para realizar esas acciones específicas cuando lo desees.

#### Diferencias:

* **Declaración de Función:** Escribes una lista de tareas específicas con un nombre claro desde el principio, como una lista de tareas en una hoja de papel.
* **Expresión de Función:** Creas una nota adhesiva con tareas específicas que puedes usar más tarde, como escribir tareas en una nota adhesiva antes de empezar tu día.

Las dos formas te permiten organizar y realizar tareas de manera efectiva, pero cual elegir utilizar depende de cómo prefieres estructurar y utilizar tus acciones (funciones) en JavaScript.

#### ¿Cuándo usar cada una?

* **Declaración de Función:** Es útil cuando quieres tener una función disponible desde el principio de tu código o cuando prefieres organizar tus funciones al comienzo de un archivo para mayor claridad. El hoisting puede ser conveniente en ciertos casos.

* **Expresión de Función:** Es más flexible y útil cuando necesitas asignar una función a una variable o pasarla como argumento a otra función. También es común en patrones de programación avanzados como funciones de orden superior.

La declaración de función es como construir una máquina con un nombre específico desde el principio, mientras que la expresión de función es como crear una máquina cuando la necesitas y guardarla en una caja para usarla más tarde.

Las dos formas te permiten realizar tareas repetitivas en JavaScript, pero con diferencias  que las hacen útiles en diferentes situaciones de programación.

La diferencia principal entre una declaración de función y una expresión de función en JavaScript esta en cómo y cuándo se declaran y se comportan en relación con el flujo en el que se ejecuta el código.

### Declaración de Función:

Una declaración de función es aquella en la que se utiliza la palabra clave `function` seguida de un nombre de función y un bloque de código que define las instrucciones que la función ejecutará.

```javascript
function suma(a, b) {
    return a + b;
}
```

**Características:**

* **Hoisting:** Las declaraciones de funciones son elevadas (hoisted) al principio de su contexto de ejecución. Esto significa que pueden ser utilizadas antes de su declaración en el código.

**Uso:**

* Son útiles cuando se quiere tener la flexibilidad de llamar a la función antes de su declaración en el código, debido al hoisting.

### Expresión de Función:

Una expresión de función es aquella en la que se define una función como parte de una expresión más grande, como asignar la función a una variable, pasarlo como argumento a otra función, o declararlo dentro de otra función.

```javascript
const suma = function(a, b) {
    return a + b;
};
```

**Características:**

* **No hay hoisting:** Las expresiones de función no son elevadas (hoisted) al principio del contexto de ejecución. Deben ser declaradas antes de ser utilizadas en el código.

**Uso:**

* Son útiles cuando se desea asignar una función a una variable, o utilizarla en contextos donde se requiere una expresión.

### Diferencias Clave:

* **Hoisting:** Las declaraciones de funciones son elevadas (hoisted), lo que significa que pueden ser utilizadas antes de su declaración en el código. En cambio, las expresiones de función no son hoisted y deben ser declaradas antes de su uso en el código.
>

* **Asignación y Flexibilidad:** Las expresiones de función permiten asignar funciones a variables y pasarlas como argumentos a otras funciones, lo cual es útil en patrones como funciones de orden superior. Las declaraciones de funciones tienen un uso más general y pueden ser más convenientes cuando se necesita hoisting.

**La diferencia clave entre una declaración de función y una expresión de función es cómo y cuándo están disponibles para su uso**

* **Declaración de Función:**
  * Puede ser llamada antes de su declaración debido al hoisting.
  * Se define con la palabra clave `function` seguida del nombre de la función.

* **Expresión de Función:**
  * Se define asignando una función anónima a una variable u otro tipo de estructura.
  * No puede ser llamada antes de su declaración debido a que no hay hoisting.

### Ejemplo Comparativo

```javascript
// Declaración de función
console.log(saludar("Juan")); // "Hola, Juan!"

function saludar(nombre) {
    return `Hola, ${nombre}!`;
}

// Expresión de función
console.log(sumar(3, 5)); // 8

let sumar = function(a, b) {
    return a + b;
};
```

En este ejemplo:

* La función `saludar` es una declaración de función y puede ser llamada antes de su declaración debido al hoisting.
* La función `sumar` es una expresión de función y no puede ser llamada antes de su asignación, ya que no hay hoisting.

### Declaración de Función

Una declaración de función es cuando defines una función utilizando la palabra clave `function`, seguida de un nombre y un cuerpo de función entre llaves `{}`.

**Ejemplo:**

```javascript
// Declaración de función
function saludar(nombre) {
    return `Hola, ${nombre}!`;
}
```

### Expresión de Función

Una expresión de función es cuando defines una función como parte de una expresión más grande, como asignarla a una variable o pasarla como argumento a otra función.

**Ejemplo:**

```javascript
// Expresión de función
let sumar = function(a, b) {
    return a + b;
};
```

* **Características:**
  * Se define asignando una función anónima (sin nombre) a una variable (`sumar` en este caso), o como argumento en una función de orden superior
  * No se beneficia del hoisting, lo que significa que debe ser declarada antes de su uso en el código.

**Ejemplo sin Hoisting:**

```javascript
console.log(sumar(3, 5)); // Error: sumar is not a function

let sumar = function(a, b) {
    return a + b;
};
```

### Contexto de Ejecución y Cierre (Scope)

* **Declaración de Función:**
  * Tiene un ámbito propio, lo que significa que las variables definidas dentro de la función solo son visibles dentro de ella misma, a menos que se declare en un ámbito superior (como `var`).

* **Expresión de Función:**
  * También tiene un ámbito, pero su visibilidad depende de cómo y dónde se asigna (por ejemplo, si se asigna a una variable local o global).

### Consideraciones Finales

* **Hoisting:** la forma en que Javascript lee las variables, en las declaraciones de funciones son elevadas al inicio, hacia arriba, mientras que las expresiones de función no.
* **Flexibilidad:** Las expresiones de función ofrecen más flexibilidad al permitir asignar funciones a variables y utilizarlas en contextos dinámicos.
* **Usos Comunes:** Ambas formas tienen usos específicos dependiendo de la situación y del estilo de codificación preferido.

En conclusión, tanto las declaraciones de función como las expresiones de función son fundamentales en JavaScript y se utilizan según las necesidades específicas del desarrollo de software y la organización del código.

---

* ## ¿Qué es la palabra clave "this" en JS?

**"this"** es como un pronombre en lenguaje natural que se refiere a algo específico en una situación particular.

 En JavaScript, "this" se usa principalmente para acceder y manipular datos dentro de un objeto.

**Ejemplo**
Imagina que tienes un objeto llamado `persona` con algunas propiedades y métodos. Cuando usas "this" dentro de un método de ese objeto, te estás refiriendo al propio objeto `persona`.

```javascript
let persona = {
    nombre: "Borja",
    edad: 43,
    saludar: function() {
        return "Hola, soy " + this.nombre + " y tengo " + this.edad + " años.";
    }
};

console.log(persona.saludar()); // Imprime: "Hola, soy Borja y tengo 43 años."
```

**Explicación del Ejemplo**
* En este ejemplo, `this.nombre` se refiere a la propiedad `nombre` del objeto `persona`, que es "Borja".
*- `this.edad` se refiere a la propiedad `edad` del objeto `persona`, que es 43.

### ¿Cómo Cambia "this"?

La forma en que "this" se comporta puede cambiar dependiendo de cómo se llame una función o método:

1. **En el contexto global**: "this" se refiere al objeto global (`window` en un navegador o `global` en Node.js).

```javascript
   console.log(this === window); // En un navegador, esto sería verdadero
   ```

1. **En el contexto de un método de objeto**: "this" se refiere al objeto al que pertenece el método.

2. **En funciones y eventos**: "this" puede ser explícitamente definido mediante técnicas como `bind`, `call` o `apply`.

**"this"** en JavaScript es una palabra clave que se refiere dinámicamente al objeto actual en el contexto de ejecución. Es útil para acceder y manipular datos dentro de objetos y varía según el contexto donde se utiliza. Entender cómo funciona "this" es fundamental para desarrollar aplicaciones web interactivas y dinámicas con JavaScript.

Entendamos "this" en JavaScript de manera más profunda, considerando sus diversos comportamientos y cómo se maneja en diferentes contextos de ejecución.

### Comportamiento Dinámico de "this"

En JavaScript, la palabra clave "this" se refiere dinámicamente al objeto al que pertenece en el momento de la ejecución. Su valor puede cambiar dependiendo de cómo se llame una función o método. Aquí están los principales comportamientos de "this":

* **En el contexto global:**
* Fuera de cualquier función, "this" se refiere al objeto global (`window` en navegadores o `global` en Node.js).

   ```javascript
   console.log(this === window); // true en un navegador
   ```

* **En el contexto de una función regular:**
* Dentro de una función regular que no es un método de objeto, "this" también se refiere al objeto global.

```javascript
   function ejemplo() {
       console.log(this === window);
   }
   ejemplo(); // true en un navegador
   ```

* **En el contexto de un método de objeto:**
* Cuando "this" se usa dentro de un método de un objeto, se refiere al propio objeto al que pertenece el método.

   ```javascript
   let persona = {
       nombre: "Juan",
       saludar: function() {
           return "Hola, soy " + this.nombre;
       }
   };
   console.log(persona.saludar()); // "Hola, soy Juan"
   ```

* **En funciones anidadas:**
* "this" puede cambiar en funciones anidadas; en este caso, no se refiere al objeto exterior, sino que puede necesitar ser capturado mediante técnicas como `bind`, `call`, o `apply`.

   ```javascript
   let obj = {
       contador: 0,
       incrementar: function() {
           function incrementoInterior() {
               this.contador++;
           }
           incrementoInterior(); // this.contador no funcionará aquí
           return this.contador;
       }
   };
   console.log(obj.incrementar()); // 0, porque incrementoInterior() no actualizó this.contador
   ```

### Cambio de "this" con `bind`, `call`, y `apply`

Para controlar explícitamente qué objeto "this" debería referenciar dentro de una función, puedes usar métodos como `bind`, `call`, y `apply`:

* **`bind`**: Crea una nueva función que, cuando sea llamada, tiene "this" establecido al primer argumento que se le pasa.

  ```javascript
  let persona = {
      nombre: "Ana"
  };

  function saludar() {
      return "Hola, soy " + this.nombre;
  }

  let funcionSaludo = saludar.bind(persona);
  console.log(funcionSaludo()); // "Hola, soy Ana"
  ```

* **`call` y `apply`**: Invocan la función inmediatamente y permiten pasar argumentos a la función. La diferencia principal entre `call` y `apply` es la forma en que se pasan los argumentos: `call` acepta una lista de argumentos separados por coma, mientras que `apply` acepta un array de argumentos.

  ```javascript
  function saludar(mensaje1, mensaje2) {
      return `${mensaje1}, soy ${this.nombre}. ${mensaje2}`;
  }

  let persona = {
      nombre: "Carlos"
  };

  console.log(saludar.call(persona, "Hola", "¿Cómo estás?")); // "Hola, soy Carlos. ¿Cómo estás?"
  console.log(saludar.apply(persona, ["Hola", "¿Cómo estás?"])); // "Hola, soy Carlos. ¿Cómo estás?"
  ```

### Uso Avanzado de "this"

* **Funciones Flecha (Arrow Functions)**: Las funciones flecha no tienen su propio "this". En su lugar, "this" se toma del contexto léxico más cercano.

  ```javascript
  let objeto = {
      contador: 0,
      incrementar: function() {
          setInterval(() => {
              this.contador++;
              console.log(this.contador);
          }, 1000);
      }
  };
  objeto.incrementar(); // Incrementa el contador cada segundo
  ```

* **Eventos en HTML y JavaScript**: En los manejadores de eventos como `onclick`, `onmouseover`, etc., "this" hace referencia al elemento HTML que desencadenó el evento.

  ```html
  <button onclick="console.log(this.textContent)">Haz clic</button>
  ```

**"this"** en JavaScript es una característica poderosa pero a veces puede ser confusa debido a su naturaleza dinámica. Es importante comprender cómo cambia "this" según el contexto de ejecución para evitar errores y aprovechar su flexibilidad en el desarrollo de aplicaciones web y otras aplicaciones basadas en JavaScript.
