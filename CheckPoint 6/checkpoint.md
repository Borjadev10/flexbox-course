# Borja Gonzalvo Checkpoint 6

---

* **¿Para qué usamos Clases en Python?**

Las clases en Python nos ayudan a organizar y estructurar el código, de manera que podemos manejarlo mas fácilmente y asi mejorar su comprensión.
De esta manera podemos crear programas más complejos y grandes, ya que los dividimos en partes mas manejables.
Mediante las clases podemos crear *plantillas* y trabajar con ellas de manera más eficiente y organizada.
Las clases nos permiten reutilizar código y manejar diferentes tipos de datos de una manera uniforme, evitando código duplicado.

Ejemplo y lineas de comentarios explicativos:

```python
# Definimos la clase Perro
class Perro:
    def __init__(self, raza, peso, edad):
        self.raza = raza
        self.peso = peso
        self.edad = edad

    def mostrar_info(self):
        print(f"Raza: {self.raza}, Peso: {self.peso}Kg , Edad: {self.edad} años")

# Creamos instancias/objetos de la clase Perro
perro1 = Perro("Beagle", 5, 4)
perro2 = Perro("Caniche", 6, 5)

# Usamos el método mostrar_info para mostrar la información de los perros
perro1.mostrar_info()  # Vemos en pantalla: Raza: Beagle, Peso: 5 kg, Edad: 4 años
perro2.mostrar_info()  # Vemos en pantalla: Raza: Caniche, Peso: 6 kg, Edad: 5 años
```

---

* **¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?**

El método `__init__` se ejecuta automáticamente al crear una instancia de una clase.
Este método nos permite empezar a darle instrucciones a la clase que hemos creado recientemente, para si poder darle las caracteristicas y atributos necesarios.
Nos permite preparar y definir los rasgos mas importantes del objeto que hemos creado.
El método `__init__` es conocido como el constructor.

Siguiendo con el ejemplo del ejercicio anterior:

```python
# Definimos la clase Perro
class Perro:
    def __init__(self, raza, peso, edad):
        self.raza = raza
        self.peso = peso
        self.edad = edad
# Con el método __init__ detallamos que características queremos que tenga la clase perro
# tipo de raza, peso y edad en este caso

```

La sintaxis del método `__init__` es:

```python
class NombreDeLaClase:
    def __init__(self, argumento1, argumento2):
        self.argumento1 = argumento1
```

El self es un parámetro especial , hace referencia a la instancia y sirve para hacer referencia a sí mismo, permitiendonos acceder a sus propios atributos/argumentos, self es en verdad el nombre de una variable, pero su uso se a convertido en una convención en Python.

---

* **¿Cuáles son los tres verbos de API?**

Al hablar de verbos en API, nos referimos a la acción que podemos realizar como cliente,con los recursos que nos ofrece un API, como servidor. Es el método HTTP que utilizamos para realizar esa acción.
Estos verbos HTTP definirán la acción que realizaremos al contactar con los recursos que nos pueda ofrecer la API.
Cada verbo, hay muchos, tienen una labor especifica y dependiendo de la acción que queramos llevar a cabo utilizaremos uno u otro.

Estos verbos HTTP son en su conjunto la base de operaciones CRUD( Crear, Leer, Actualizar, Eliminar), que nos permiten como clientes relacionarnos con los recursos del servidor(API), todo ello de una manera segura.

Los verbos mas utilizados son: *GET, POST, PUT, PATCH y DELETE* y de ellos, los tres mas comunes son:

* **GET**: utilizado para solicitar datos del servidor al que se le manda la solicitud, como por ejemplo lista de usuarios, también al acceder a una dirección url estamos solicitando el servicio para acceder a la dirección web.

```bash
GET /api/users/4445 HTTP/1.1
Host: ej4445
```
>
* **POST**: utilizado para enviar datos al servidor y que este los almacene o los procese,como por ejemplo cuando rellenamos un formulario para registrarnos en una web.
  
```bash
POST /api/users HTTP/1.1
Host: ej445.com
Content-Type: application/json

{
    "nombre": "Borjaejemplo",
    "correo": "borja@ejemplo.com"
}
```

* **DELETE**:utilizado para eliminar un dato o recurso en concreto en el servidor,como por ejemplo cuando eliminamos una publicación en alguna red social.

```bash
DELETE /api/users/123 HTTP/1.1
Host: ej445
```

---

* **¿Es MongoDB una base de datos SQL o NoSQL?**

La diferencia entre base de datos SQL relacionales y NoSQL no relacionales esta en como trabajan, almacenan y modifican los datos de sus bases de datos.
Las principales diferencias entre ellas son:

* Modelo de datos:
  * SQL: modelo de datos basados en tablas con filas y columnas, las relaciones entre las tablas se lleva a cabo por medio de claves primarias u claves externas.
  * NoSQL:en vez de usar tablas, los datos se guardan en estructuras flexibles, como pares clave-valor,documentos JSON.

* Esquema:
  * SQL: antes de empezar a insertar datos hemos de definir el esquema, que sera fijo y definira la estructura y los tipos de datos de cada columna,
  * NoSQL:utilizan un esquema flexible y dinámico, permitiéndonos almacenar datos sin estructura fija, pudiendo añadir según la necesidad nuevos campos.

* Escalabilidad
  * SQL: escala en vertical normalmente, lo que significa que añadimos recursos a un unico servidor.
  * NoSQL:escala en horizontal, lo que nos da la posibilidad de trabajar con un mayor volumen de datos y trafico, ya que esta distribuido en varios servidores,

* Consultas
  * SQL:han de utilizarse con lenguaje estructurado SQL
  * NoSQL:el lenguaje de consulta varia según la base de datos, algunas bases de datos NoSQL utilizan su propio lenguaje, otras son consultas que se centran en operaciones de de búsqueda sencillas,

* Utilización/Aplicación
  * SQL:perfectas para aplicaciones complejas, que requieran consultas complejas,
  * NoSQL:para grandes volúmenes de datos, con escalabilidad horizontal, y que requieran flexibilidad a la hora de insertar datos.

Como regla general a la hora de utilizar una u otra seria ver si tenemos datos que dependan en gran medida en las relaciones, lo mejor seria usar SQL. Mientras que si lo que manejas son datos no estructurados que necesitan flexibilidad, lo mejor es usar NoSQL.

Una vez visto esto, la respuesta a que tipo de base de datos es MongoDB sería que es **NoSQL**.
En MongoDB no se usan tablas y esquemas predefinidos sino que se usan datos flexibles basados en documentos, estos documentos son JSON(JavaScript Object Notation), y a su vez estos documentos se pueden agrupar en colecciones. Cada documento de cada colección puede tener un esquema muy diferente a otro en otra colección. Gracias a esto nos da la opción de almacenar los datos de manera muy flexible.

El lenguaje de consulta utilizado por MongoDB (MongoDB Query Language (MQL)) es muy flexible y amplio lo que permite consultas complejas.

Además, MongoDB utiliza un lenguaje de consulta es rico y flexible llamado MongoDB Query Language (MQL) que permite realizar consultas complejas y poderosas sobre los datos almacenados en la base de datos.

MongoDB es una base de datos NoSQL que ofrece flexibilidad, escalabilidad y rendimiento.

---

* **¿Qué es una API?**

API(Application Programming Interface) podemos definirlo como el intermediario necesario que nos permite que varios programas se conecten y comuniquen entre ellos, compartiendo datos y funciones de manera segura.
Nos ayuda a acceder a las funciones que una aplicación o un servicio puedan ofrecernos.
El cliente es quien envía la solicitud y el servidor es el que recibe la solicitud y nos da la respuesta.
>
* El funcionamiento de una API de forma simplificada es:
  * Solicitud: como cliente enviamos una solicitud a la API como solicitar informacion o envío de datos.
  * Procesamiento: la API, como servidor,recibe la solicitud que le hemos pasado y la procesa.
  * Respuesta:la API nos devuelve una respuesta a nuestra solicitud.

En el desarrollo de software las API son imprescindibles porque nos permiten:

* Que diferentes sistemas,servicios y aplicaciones trabajen juntos, estén escritos o no en el mismo lenguaje de programación.

* Reutilizar funciones que existan en otros sistemas, con la consiguiente mejora de tiempo y esfuerzo  en el desarrollo de software.

* Ayudan en la complejidad interna de un sistema, simplificando en gran medida la forma en que interactuamos con el servidor. Pudiendo usar funciones de un sistema sin conocer todos los detalles internos.

* Aumentar la seguridad, ya que incluyen sistemas de seguridad para proteger los datos que se comparten, como sistemas de autentificación y cifrado de datos.

Resumen de los tipos más utilizados y comunes:

* **APIS de Web**: utilizadas para que distantas aplicaciones web se comuniquen e interactuen entre ellas,
  * REST(Representational State Transfer): Utiliza HTTP, mediante direcciones URL permite acceder y  modificar los recursos que ofrece(usuarios,productos..)
  * SOAP(Simple Object Access Protocol):utiliza XML,utilizadas cuando se requiere alta seguridad y  transacciones complejas,
* **APIS de Sistemas Operativos**:gracias a estas, los programas interactuar con el sistema operativo.
  * Windows API: utilizada en sistema operativo Windows.
  * POSIX: utilizada en sistemas operativos Inux, Linux.
* **APIS de Base da Datos**:utilziadas para que las aplicaciones puedan interactuar con bases de datos.
  * SQL:utilizada en la gestion de bases de datos relacionales.
  * MongoDB API:utilizadas en bases de datos NoSQL, como por ejemplo MongoDB.
* **APIS de Framework**:permiten a los desarrolladores utilizar funciones de frmework.
  * jQuery:
  * Django REST
* **APIS de Hardware**:gracias a ellas el software y el hardware pueden interactuar.
  * DirectX: se utilizan para trabajar con todo lo relacionado con multimedia en Windows.
  * OpenGL:utilizada para renderizar los gráficos 2D/3D.
>
Una parte importante dentro de las APIs son:
**Endpoints**: son los puntos finales a los que va dirigida la solicitud en una consulta a una API, es la dirección URL en la que se define la dirección dentro de la API.
  
---

* **¿Qué es Postman?**  

Podemos definir a Postman como una especie de ayudante que nos asiste  para probar y verificar diferentes servicios que las aplicacions y páginas web utilizan para funcionar correctamente.

Postman es utilizada por muchos desarrolladores, es una plataforma colaborativa. Siendo muy versátil y poderosa, ya que permite a los desarrolladores diseñar,testear, documentar y monitorear APIs y su correcto funcionamiento.

Gracias a Postman los desarrolladores pueden simplificar el desarrollo y prueba de APIs.

* Características de Postman:
  * **Interfaz gráfica**: gracias a su interfaz de usuario intuitivo, ayuda a crear y gestionar solicitudes.
  * **Gran soporte** para métodos HTTP: nos da la posibilidad de usar un variado abanico de métodos(GET,POST,PUT,DELETE..).
  * **Colecciones**: permite agrupar las solicitudes en colecciones, lo que posibilita que estén organizadas,estructuradas y puedan ser exportadas e importadas.
  * **Variables de entorno**:el usuario puede definir variables de entorno y asi cambiar entre diferentes entornos(producción, pruebas,desarrollo)
  * **Automatización**: el desarrollador puede configurar Postaman para que automaticamente se realizen pruebas y ver si todo funciona correctamente.
  * **Colaboración**: Postman facilita compartir con otros desarrolladores pruebas y resultados.
  * **Generación de Documentación**:facilita la creación de documentación para las APIs, que puede ser Integraciones:Postman esta integrada en distintas plataformas y servicios, facilitando la colaboracion y flujo de trabajo.Ej:Github
  * **Generación de Código**:Postman puede generar código en diferentes lenguajes(JavaScript, Python, Ruby, etc.)

---

* **¿Qué es el polimorfismo?**

La palabra Polimorfismo, deriva del griego, significa muchas formas.
De forma sencilla el polimorfismo es la capacidad de un objeto para tomar múltiples formas.

En la programación, el polimorfismo permite que una función o método pueda procesar datos de diferentes tipos.

El polimorfismo es un principio de la programación orientada a objetos que permite que objetos de diferentes clases sean tratados como objetos de una clase común.

El polimorfismo hace que los sistemas sean más flexibles y fáciles de extender, permitiendo que el mismo método o acción se aplique a diferentes tipos de objetos de manera adecuada.

El polimorfismo en Python permite escribir código más flexible y reutilizable.

Podemos aplicarlo mediante:

* **Funciones**:que pueden aceptar diferentes tipos de objetos.
* **La herencia**: que permite sobrescribir métodos.
* **La sobrecarga de operadores**
* **Funciones incorporadas polimórficas**

Ejemplos:

* **Polimorfismo con Funciones**

Una función en Python puede aceptar diferentes tipos de objetos y comportarse de manera diferente según el tipo del objeto.

```python
class FCBarcelona:
    def __init__(self, goles):
        self.goles = goles

    def goles_totales(self):
        return sum(self.goles)

class RealMadrid:
    def __init__(self, goles):
        self.goles = goles

    def goles_totales(self):
        return len(self.goles)

def calcular_goles_totales(equipo):
    return equipo.goles_totales()

# Crear instancias de FCBarcelona y RealMadrid con una lista de goles de cada partido jugado 
barcelona = FCBarcelona([3, 2, 1, 4])  
madrid = RealMadrid([1, 1, 1, 1, 1])   

# Usar la función polimórfica para calcular los goles totales
print(f"Goles totales del FC Barcelona: {calcular_goles_totales(barcelona)}")  # Salida: Goles totales del FC Barcelona: 10
print(f"Goles totales del Real Madrid: {calcular_goles_totales(madrid)}")      # Salida: Goles totales del Real Madrid: 5

```

La función calcular_goles_totales para calcular los goles totales de ambos equipos. Gracias al **polimorfismo**, la misma función puede trabajar con diferentes tipos de objetos que usen el método goles_totales.

Cuando una clase hija hereda de una clase base y sobrescribe métodos, se puede aprovechar el polimorfismo para tratar a los objetos de las clases hijas como objetos de la clase base.

* **Polimorfismo con Herencia**

```python

class Vehiculo:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def conducir(self):
        print(f"Conduciendo el vehículo {self.marca} de color {self.color}.")

class Coche(Vehiculo):
    def __init__(self, marca, color, modelo):
        super().__init__(marca, color)
        self.modelo = modelo

    def conducir(self):
        print(f"Conduciendo el coche {self.marca} {self.modelo} de color {self.color}.")

class Bicicleta(Vehiculo):
    def __init__(self, marca, color, tipo):
        super().__init__(marca, color)
        self.tipo = tipo

    def conducir(self):
        print(f"Montando la bicicleta {self.marca} de tipo {self.tipo} de color {self.color}.")


# Ejemplo de uso
coche = Coche("Toyota", "rojo", "Corolla")
bicicleta = Bicicleta("Trek", "negro", "de montaña")

coche.conducir()
bicicleta.conducir()

```

En este ejemplo usamos la herencia para evitar la repetición de código al definir atributos y comportamientos comunes (marca, color, conducir()) en la clase base Vehiculo, que luego se comparten con las clases derivadas Coche y Bicicleta.

* **Polimorfismo con sobrecarga de operadores**

```python

class Coche:
    def __init__(self, marca):
        self.marca = marca

    def __str__(self):
        return f"{self.marca}"

    def __add__(self, otro_coche):
        if isinstance(otro_coche, Coche):
            return f"Combinando {self} y {otro_coche}"
        else:
            raise TypeError("No se puede combinar un Coche con un objeto de tipo diferente")


class Audi(Coche):
    def __init__(self):
        super().__init__("Audi")

class BMW(Coche):
    def __init__(self):
        super().__init__("BMW")

# Ejemplo de uso
audi = Audi()
bmw = BMW()

print(audi + bmw)

```

En este ejemplo:

Tenemos una clase Coche que define la sobrecarga de los operadores str()para proporcionar una representación de string y add() para combinar dos objetos Coche.

* **Funciones incorporadas polimórficas**

```python

# Suma de una lista
lista = [1, 2, 3, 4, 5]
print("Suma de los elementos de la lista:", sum(lista))

# Suma de una tupla
tupla = (1, 2, 3)
print("Suma de los elementos de la tupla:", sum(tupla))

# Suma de un conjunto
conjunto = {1, 2, 3, 4, 5}
print("Suma de los elementos del conjunto:", sum(conjunto))

```

En este ejemplo, sum() se utiliza para sumar los elementos de una lista, una tupla y un conjunto, y en cada caso devuelve la suma de los elementos. Esto demuestra cómo las funciones incorporadas en Python pueden trabajar de forma polimórfica con diferentes tipos de datos.

---

* **¿Qué es un método dunder?**
  
El método dunder es una forma de referirse a los métodos especiales en Python que tienen nombres que empiezan y terminan con dos guiones bajos (`__`).

Los métodos dunder son utilizados por Python para realizar diversas operaciones internas:la inicialización de objetos,la representación de objetos en forma de cadena,la sobrecarga de operadores …

Por ejemplo, cuando defines una clase en Python, puedes agregar métodos especiales dunder para que los objetos de esa clase puedan trabajar de manera especial cuando interactúan con operadores integrados de Python.

Ejemplos:

* `__init__`: Este método lo usamos una vez creado un nuevo objeto de la clase y se utiliza para inicializar los atributos de ese objeto.

```python
 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona = Persona("Borja", 43)

```
  
* `__str__`: Este método lo usamos para representar el objeto como una cadena utilizando la función str()

```python

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}"

persona = Persona("Borja", 43)
print(str(persona))  # Salida: Persona: Borja, Edad: 43

```

* `__add__`: Este método lo usamos para llamar al operador `+` con dos objetos.

```python

class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def __add__(self, otro):
        return self.valor + otro.valor


num1 = Numero(55)
num2 = Numero(10)

# Sumar las instancias usando el método __add__
resultado = num1 + num2

# Mostrar el resultado
print("Resultado de la suma:", resultado)

```

* `__len__`: Este método lo usamos cuando se utiliza la función `len()` en un objeto. Se utiliza para definir la longitud de un objeto.

```python

class Contenedor:
    def __len__(self):
        return 3

# Crear una instancia de la clase Contenedor
contenedor = Contenedor()

# Obtener la longitud del contenedor usando el método __len__
print("Longitud del contenedor:", len(contenedor))

```


---

* **¿Qué es un decorador de python?**

Un decorador es como una capa extra, como un envoltorio, que le añade mas extras a una función, pero sin modificar el código de la función.
Nos permite añadir mas características sin tener que repetir el código.

En programación es una forma de añadir funcionalidades extras a un método o función que ya tenemos creado sin modificarle el código. Envolvemos,decoramos esa función con funciones extras.

Para utilizar un decorador, escribimos **@ y el nombre del decorador** que queramos ponerle antes de la función que queramos decorar o añadirle funciones, ejemplo:**@decorador**

**Ejemplos y usos**

```python
# Definimos el decorador
def agregar_color(funcion):
    def coche_con_color():
        return funcion() + " de color rojo"
    return coche_con_color

# Aplicamos el decorador a la función coche
@agregar_color
def coche():
    return "Coche"

# Probamos la función decorada
print(coche())

```

* En este ejemplo con el decorador le hemos añadido color(funcionalidad) a la función original sin modificar nada del original.


```python

# Definimos el decorador
def agregar_caracteristica(funcion):
    def animal_con_caracteristica():
        return funcion() + " que puede volar"
    return animal_con_caracteristica

# Aplicamos el decorador a la función animal
@agregar_caracteristica
def animal():
    return "Animal"

# Probamos la función decorada
print(animal())

```

* En este ejemplo con el decorador le hemos añadido características( que puede volar) a la función original sin modificar nada del original
