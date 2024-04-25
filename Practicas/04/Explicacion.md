# Cuarta práctica. Cuarta parte

## Teniendo en cuenta las características del ensamblador, ¿Cuál es la principal limitante que observan? Justifique su respuesta.

La principal limitante que se observa en el ensamblador es su dependencia en la codificación a nivel de bajo nivel. Aunque el ensamblador permite a los programadores escribir programas en un lenguaje más simbólico y legible en comparación con el código binario directo, todavía requiere un conocimiento detallado de la arquitectura y la codificación específica de la máquina objetivo. Esto significa que los programadores deben ser conscientes de las instrucciones específicas de la máquina y sus formatos de codificación, lo que puede resultar en un código difícil de escribir y mantener.

Justificación:
1. **Complejidad de codificación**: Escribir en lenguaje ensamblador requiere un conocimiento profundo de la arquitectura subyacente del hardware. Esto incluye entender las instrucciones de la CPU, el diseño de la memoria y otros aspectos técnicos. Los programadores deben ser capaces de traducir sus algoritmos y lógica de manera precisa y eficiente en instrucciones de bajo nivel.

2. **Falta de abstracción**: El ensamblador carece de abstracciones significativas que faciliten la escritura de programas complejos. Los programadores deben lidiar con detalles a nivel de registro, memoria y operaciones aritméticas, lo que puede resultar en un código más propenso a errores y difícil de entender.

# Bonus: 
## El ensamblador es importante por varias razones:

1. **Control preciso del hardware**: Permite un control preciso sobre el hardware subyacente al escribir programas directamente en un nivel más bajo que el código de alto nivel. Esto puede ser necesario para optimizar el rendimiento o acceder a características específicas del hardware que no están disponibles a través de lenguajes de alto nivel.

2. **Entender el funcionamiento interno de la computadora**: Escribir en ensamblador puede proporcionar una comprensión más profunda de cómo funciona una computadora a nivel de bajo nivel. Esto es útil para los desarrolladores que necesitan entender el comportamiento exacto de sus programas y optimizarlos para un rendimiento óptimo.

3. **Conocimiento de la informática básica**: El ensamblador enseña conceptos fundamentales de informática, como la aritmética de bits, el funcionamiento de la memoria y la ejecución de instrucciones. Estos conocimientos pueden ser valiosos incluso para programadores que trabajan en niveles más altos de abstracción.



# Proyecto 6: El Ensamblador
A continuación se presenta una breve explicación del proceso de construcción del programa del proyecto 6 de nand2tetris, describiendo de manera concisa su funcionamiento básico.

- El proceso general de convertir código de ensamblador a código de máquina incluye los siguientes pasos:

## Configuración inicial:
Se establece un diccionario que asigna nombres simbólicos (como 'SCREEN', 'KBD', 'SP', 'LCL', etc.) a direcciones de memoria predefinidas. Además, se asignan direcciones a las localidades de memoria de tipo 'R' (R0, R1, ..., R15), inicializando los registros generales con valores del 0 al 15.
En este caso específico, el código en Python incluye la creación de un diccionario que asigna ciertos nombres simbólicos a direcciones de memoria predefinidas. Este diccionario se emplea posteriormente para asignar direcciones de memoria específicas a símbolos presentes en el código de ensamblador.

## Ensamblador:
Este proceso implica analizar el código de ensamblador, principalmente mediante el uso del módulo de análisis sintáctico. Aquí se detallan los aspectos clave de este proceso:

### Inicialización del análisis sintáctico: 
Se inicializa un objeto de análisis sintáctico para cada línea del archivo de código de ensamblador. El constructor de la clase elimina los espacios en blanco y otros caracteres innecesarios, y establece el tipo de instrucción como nulo inicialmente.

### Identificación del tipo de instrucción: 
A través del método de verificación, se determina el tipo de instrucción según su estructura. Se verifica si la línea es un comentario, una instrucción A (que comienza con "@"), una etiqueta (que comienza con "("), o una instrucción C. El resultado se guarda en el atributo tipo del objeto.

### Limpieza de la línea: 
El método de limpieza elimina los comentarios y espacios en blanco de la línea para facilitar el análisis posterior. Esto implica encontrar la posición del comentario (si existe) y truncar la línea en consecuencia.

### Métodos para obtener componentes específicos de instrucciones: 
Se utilizan métodos como get_valor, get_destino, get_operacion, get_salto y get_etiqueta para extraer componentes específicos de la instrucción, como el valor, el destino, la operación, el salto y la etiqueta respectivamente. Estos métodos operan según el tipo de instrucción y devuelven los valores correspondientes según la lógica definida.

## Generación de código de máquina:
El módulo codificador traduce los componentes de la instrucción ensambladora a código binario. Se obtiene el código de destino, el código de operación y el código de salto correspondientes para las instrucciones de tipo C. Para las instrucciones de tipo A, se traduce el valor a su representación binaria de 15 bits. A continuación se detallan las funciones de los métodos de manera más exhaustiva:
- código_destino: Este método toma el destino de una instrucción de tipo C y devuelve su representación en código binario, según el diccionario de destinos predefinidos.
- código_operacion: Toma la operación de una instrucción de tipo C y la convierte en su representación en código binario correspondiente, según el diccionario de operaciones predefinidas. Se eliminan los espacios en blanco de la operación antes de buscarla en el diccionario.
- código_salto: Similar a código_destino y código_operacion, este método toma el salto de una instrucción de tipo C y lo convierte en su representación en código binario correspondiente, según el diccionario de saltos predefinidos.
- código_valor: Utilizado para convertir un valor, ya sea un número o una variable, en su representación binaria de 15 bits. Si la variable no está en el diccionario, se le asigna un valor y se agrega al diccionario.
- agregar_al_diccionario: Añade las etiquetas y sus direcciones correspondientes al diccionario.
  
## Actualización del diccionario:
Este paso implica actualizar el diccionario con la información de las etiquetas y sus respectivas direcciones. El método agregar_al_diccionario recorre cada línea previamente procesada y analizada para determinar si es una etiqueta. Si no es una etiqueta, se incrementa un contador para rastrear las instrucciones no relacionadas con etiquetas.
Si se encuentra una línea que es una etiqueta, se agrega al diccionario la información de la etiqueta y su dirección correspondiente, la cual se establece según el contador de instrucciones.

## Escritura del archivo de salida:
Se genera el nombre del archivo de salida basado en el nombre del archivo de entrada proporcionado, reemplazando la extensión ".asm" por ".hack".
Según el tipo de instrucción (A o C), se escribe la cadena de código de máquina correspondiente en el archivo de salida, junto con un carácter de nueva línea para cada línea de código de máquina. Una vez que el código está en la memoria, el procesador o CPU lo lee e interpreta como instrucciones de bajo nivel. La CPU ejecuta estas instrucciones una por una, realizando las operaciones especificadas en el código.



