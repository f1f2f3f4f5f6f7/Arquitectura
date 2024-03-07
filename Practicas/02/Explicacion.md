# Segunda práctica. Segunda parte.


## Preguntas adicionales

### 1. ¿Cuál es el objetivo de cada uno de esos proyectos con sus palabras y describa que debe hacer para desarrollarlo?

#### Tema 1: Aritmetica Booleana

**Objetivo:**
el objetivo de esta parte del laboratorio es construir una serie de chips, con ello culminando con la creación de la Unidad Aritmetico-Lógica de la computadora Hack. La ALU es una parte esencia de la CPU que realiza operaciones aritmeticas y lógicas en los datos que se van procesando en la computadora.

**Desarrollo del Proyecto:**
Primero tendremos que empezar con los chips basicos como medio sumador, sumador completo y incrementador de 16 bits, entre otros, de acuerdo con las especificaciones que nos dan en el capitulo 2, luego, utilizamos los chips construidos para ir ensamblando la ALU de la computadora Hack. Seguimos haciendo unas pruebas de cada chip utilizando los scripts de prueba proporcionados para poder garantizar que nos funciones segun lo planeado. Por ultimo, empezamos a implementar de la ALU, primero empezamos sin manejo de salidas de estado y ya al final si empezamos a incluir estas salidas.

#### Tema 2: Memoria

**Objetivo:** El objetivo en este proyecto es construir una unidad de memoria de acceso aleatorio (RAM) en la arquitectura Hack. La RAM es vital para poder almacenar y recuperar datos de manera rapida y eficiente durante la ejecuccion de los programas.

**Desarrollo del Proyecto:** Empezamos construyendo chips básicos como registros de 1 bit y registros de 16 bits, que formarán parte de la base para construir la memoria RAM, empezamos a utilizar los registros construidos para ir ensamblando las unidades de memoria RAM progresivamente más grande, desde RAM8 hasta una RAM16K, cada una con capacidades de almacenamiento incrementadas. Empezamos a utilizar las compuertas logicas y registros para ir implementando correctamente la funcionalidad de nuestro almacenamiento y dirrecionamiento de la memoria RAM. Para concluir, hacemos pruebas exhaustivas de cada chip construido utilizando los scripts de prueba proporcionados para garantizar el correcto funcioanmiento y cumplimiento de todo lo establecido.

### 2. Explique las principales diferencias entre la lógica aritmética y la lógica secuencial.

| Característica           | Lógica Aritmética                                  | Lógica Secuencial                                |
|--------------------------|----------------------------------------------------|---------------------------------------------------|
| Tipo de Operaciones      | Operaciones aritméticas y lógicas básicas.        | Secuencia de estados y control de flujo.         |
| Procesamiento de Datos   | Realiza cálculos y manipulaciones instantáneas.    | Retiene información a lo largo del tiempo.       |
| Elementos Principales    | Unidades Aritmético-Lógicas (ALU).                | Flip-flops, registros, máquinas de estados finitos.|
| Ejemplo de Aplicaciones  | Suma, resta, multiplicación, división, operaciones lógicas. | Circuitos de control, máquinas de estados finitos. |
| Características Clave    | Operaciones en paralelo.                           | Cambio de estado basado en condiciones o señales de control. |

# Explicación de los chips:

## HalfAdder:
El HalfAdder realiza la suma de dos números binarios de un solo bit y produce dos salidas: una para la suma y otra para el acarreo generado. Esta operación se logra utilizando una compuerta Xor y una compuerta And entre las entradas.

## FullAdder:
El FullAdder es un circuito más avanzado que el HalfAdder y se utiliza para sumar tres números binarios de un solo bit. Produce dos salidas: la suma de los tres bits de entrada y el acarreo resultante. Se construye utilizando múltiples HalfAdders y una compuerta Or para combinar los acarreos.

## Add16:
El chip Add16 suma dos números de 16 bits utilizando múltiples FullAdders conectados en cascada. Cada FullAdder suma un par de bits correspondientes de los dos números y considera el acarreo de la suma anterior.

## Inc16:
El chip Inc16 suma 1 al número binario de 16 bits de entrada utilizando una serie de sumadores de un solo bit conectados en cascada.

## ALU:
La ALU realiza operaciones aritméticas y lógicas en datos binarios. Utiliza compuertas lógicas y sumadores para ejecutar operaciones como suma, resta, AND, OR, y NOT.

## Bit:
El chip Bit selecciona entre la salida anterior y la entrada actual mediante un multiplexor y luego guarda la selección utilizando un Data Flip Flop.

## Register:
El Register almacena 16 bits en la memoria utilizando 16 bits construidos anteriormente.

## RAM8:
La RAM8 es una memoria de 8x16 que utiliza 8 registros de 16 bits cada uno, construidos con chips Register.

## RAM64:
La RAM64 es una memoria de 64 registros de 16 bits, construida utilizando 8 chips RAM8.

## RAM512:
La RAM512 es una memoria de 512 registros de 16 bits, construida utilizando 8 chips RAM64.

## RAM4k:
La RAM4k es una memoria de 4000 registros de 16 bits, construida utilizando 8 chips RAM512.

## RAM16k:
La RAM16k es una memoria de 16k registros de 16 bits, construida utilizando 4 chips RAM4k.

## PC:
El PC (Contador de Programa) primero incrementa la salida mediante un chip Inc16, luego selecciona entre las posibles entradas utilizando un multiplexor y finalmente guarda la selección utilizando un Register.

# BONUS

## ¿Qué tipo de unidades aritmético lógicas existen?

# Tipos de Unidades Aritmético Lógicas (ALU)

Las Unidades Aritmético Lógicas (ALU) son componentes fundamentales de las CPU (Unidades de Procesamiento Central) de las computadoras. Varían en complejidad y características según el diseño de la CPU y su aplicación. A continuación, se describen algunos tipos comunes de ALU:

- **ALU de 4 bits**: Es uno de los tipos más simples de ALU y puede realizar operaciones en datos de hasta 4 bits de longitud.

- **ALU de 8 bits**: Similar al ALU de 4 bits, pero puede manejar datos de hasta 8 bits de longitud, lo que lo hace más versátil y capaz de realizar operaciones más complejas.

- **ALU de 16 bits**: Diseñado para manejar datos de 16 bits, este tipo de ALU se encuentra comúnmente en procesadores más antiguos y en sistemas embebidos de baja potencia.

- **ALU de 32 bits y 64 bits**: Son los tipos de ALU más comunes en las CPU modernas para computadoras de propósito general. Pueden manejar datos de 32 o 64 bits de longitud, lo que les permite realizar operaciones más complejas y manejar una mayor cantidad de datos en paralelo.

- **ALU con soporte SIMD**: SIMD (Single Instruction, Multiple Data) es una técnica de procesamiento que permite realizar una operación en múltiples datos simultáneamente. Las ALU con soporte SIMD están diseñadas para manejar este tipo de operaciones y son comunes en CPUs utilizadas en tareas intensivas en computación, como gráficos, procesamiento de señales y procesamiento de imágenes.

- **ALU especializadas**: Algunas CPU pueden incluir ALU especializadas para tareas específicas, como el procesamiento de punto flotante o el cifrado/descifrado de datos.


la cantidad exacta de unidades aritmético lógicas (ALU) que existen depende de la diversidad de diseños de procesadores y circuitos integrados que se han desarrollado a lo largo del tiempo. Cada fabricante de CPU puede implementar su propia versión de la ALU, adaptándola a sus necesidades específicas y a las demandas del mercado.

Por ejemplo, en la actualidad, los principales fabricantes de CPU como Intel, AMD, ARM y otros, desarrollan sus propias ALU para sus respectivas líneas de procesadores, y dentro de cada empresa, puede haber múltiples diseños de ALU para diferentes modelos de procesadores.

Además, con los avances en la tecnología y la investigación en arquitectura de computadoras, se han propuesto y desarrollado varios diseños de ALU especializadas para aplicaciones específicas, como el procesamiento de gráficos, la inteligencia artificial, el procesamiento de señales, entre otros.



