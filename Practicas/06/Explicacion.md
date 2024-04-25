# Sexto práctica. Sexta parte
## Lenguaje de alto nivel

Un lenguaje de programación de alto nivel está creado para ser fácilmente entendido por los humanos y para expresar la lógica de programación de una forma que se asemeje más al lenguaje humano. A medida que nos desplazamos hacia abajo en la escala de abstracción, desde "alto nivel" hacia "bajo nivel", la conexión con la arquitectura y el hardware de la computadora se vuelve más directa, reduciendo la abstracción.

## Características de los Lenguajes de Alto Nivel:

- Abstracción: Los lenguajes de programación de alto nivel permiten a los desarrolladores escribir instrucciones sin tener que preocuparse excesivamente por la complejidad interna de la máquina.

- Portabilidad: Los programas creados en un lenguaje de alto nivel son más fáciles de trasladar, ya que pueden ejecutarse en distintas plataformas con pocos o ningún cambio necesario.

- Sintaxis más clara: Los lenguajes de alto nivel suelen tener una estructura y sintaxis más fácil de entender, lo que facilita tanto la lectura como la escritura del código.

- Gestión automática de memoria: Muchos lenguajes de alto nivel incluyen características que gestionan automáticamente la asignación y liberación de memoria, lo que libera a los desarrolladores de esta tarea.

## Bonus: ¿Qué se debe considerar para proponer un nuevo y buen lenguaje de programación, teniendo en cuenta la arquitectura de computador completa? Justifique su respuesta.

Eficiencia: El nuevo lenguaje debe ser eficiente en la ejecución del código, ya que la optimización del rendimiento es esencial para su viabilidad en aplicaciones del mundo real.

Abstracción: Debe ofrecer un equilibrio adecuado entre abstracción y control. Una abstracción demasiado baja puede dificultar la expresión clara de ideas para los programadores, mientras que una abstracción demasiado alta puede afectar el rendimiento.

Portabilidad: La capacidad de ejecutar programas escritos en el lenguaje eficientemente en diversas arquitecturas de computadoras es fundamental para su diseño.

Seguridad: La seguridad debe ser una preocupación principal para evitar vulnerabilidades y ataques. La gestión segura de la memoria y la prevención de errores comunes son aspectos críticos a considerar.

Herramientas y Ecosistema: Es importante que el lenguaje disponga de un sólido conjunto de herramientas de desarrollo y un ecosistema activo de bibliotecas y frameworks para facilitar la implementación de aplicaciones.

Comunidad: La formación de una comunidad activa y comprometida alrededor del lenguaje es esencial, ya que puede contribuir significativamente al crecimiento y la mejora continua del mismo.

## ¿Cuál es el objetivo del proyecto?

En este proyecto, se buscó adoptar o idear una idea de aplicación en forma de un juego de computadora simple. Se implementaron ejemplos como Snake y Square, utilizando Jack, los cuales representan versiones básicas o partes de juegos simples o interacciones interesantes. Para llevar a cabo este desarrollo, se utilizó un editor de texto para escribir los programas Jack, el JackCompiler para compilarlos y el emulador VM ya existente.



## Snake

# Main

En el archivo Main.jack se define la clase principal (Main), que contiene el método main(). Aquí se crea una instancia de la clase SnakeGame llamada game, y luego se invoca el método run() de la instancia game para ejecutar el juego. Una vez completada la ejecución del juego, se llama al método dispose() para llevar a cabo cualquier limpieza o liberación de recursos necesaria, devolviendo el control.

# RandSeed

El archivo RandSeed.jack define la clase RandSeed que contiene el método getSeed() para obtener una semilla aleatoria. Además, muestra un mensaje al usuario indicando que presione una tecla para comenzar, y luego utiliza un bucle para esperar a que el usuario realice dicha acción. La semilla se incrementa cada vez que se ejecuta el bucle y se reinicia cuando alcanza un valor límite, seguido de la limpieza de la pantalla y la devolución de la semilla.

# Random

La clase Random, definida en el archivo Random.jack, tiene un campo estático seed y métodos para manipular y generar números aleatorios. Incluye el método setSeed(), que establece la semilla para la generación de números aleatorios. El método rand() genera un número aleatorio en el rango de 0 a 32767 utilizando una fórmula específica, mientras que el método randRange() genera un número aleatorio en un rango específico utilizando la semilla y operaciones de bits.

# Snake

El archivo Snake.jack define la clase Snake, que representa la serpiente en el juego. Sus atributos incluyen referencias al juego (SnakeGame), la posición de la cabeza, longitud, dirección y un historial de movimientos. El constructor inicializa la serpiente y dibuja su posición inicial. Sus métodos incluyen funciones para gestionar el movimiento, crecimiento, dibujo y verificación de colisiones.

# SnakeGame

La clase SnakeGame, representada en el archivo SnakeGame.jack, es responsable de manejar el juego. Contiene instancias de Snake y SnakeGrid. El método run() maneja el bucle principal del juego, procesa la entrada del teclado, mueve la serpiente y actualiza el estado del juego. Además, gestiona niveles, dibuja y actualiza la interfaz de usuario, y maneja eventos de pausa o finalización del juego.

# SnakeGrid

El archivo SnakeGrid.jack define la clase SnakeGrid, que representa la cuadrícula del juego. Se utiliza para gestionar la posición de la serpiente y la ubicación de la comida. Sus métodos incluyen funciones para colocar y dibujar la comida, inicializar y gestionar la cuadrícula, y verificar ocupación y colisiones. También proporciona métodos para dibujar la interfaz de usuario, como puntuación, nivel y mensajes de estado.

## Square


- Main.jack: Este archivo actúa como el punto de entrada del juego. En su función main(), se crea una instancia de SquareGame, se inicia el juego con el método run(), y luego se liberan los recursos con dispose().

- Square.jack: Esta clase define un cuadrado gráfico en la pantalla. Al ser instanciado, el constructor establece la posición y tamaño del cuadrado, además de dibujarlo en la pantalla. Métodos adicionales permiten borrar el cuadrado, así como aumentar o disminuir su tamaño, y moverlo en diferentes direcciones (arriba, abajo, izquierda, derecha).

- SquareGame.jack: Esta clase implementa el juego "Square Dance". La instancia de Square es controlada por el usuario para moverse y cambiar su tamaño. El método run() maneja la entrada del usuario, moviendo el cuadrado en la dirección actual y ajustando su tamaño según las teclas presionadas. El juego continúa ejecutándose hasta que el usuario presiona la tecla 'q'.

