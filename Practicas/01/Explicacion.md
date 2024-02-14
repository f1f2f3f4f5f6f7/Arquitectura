# Primera práctica. Segunda parte.

# NOT

| in  | out |
|:---:|:---:|
| 0   | 1   |
| 1   | 0   |

Esta representa la compuerta más básica que podemos crear. Comenzando desde la compuerta NAND, con la siguiente configuración:
| a   | b   | out |
|:---:|:---:|:---:|
| 0   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |

En este momento, como podemos observar, todas las situaciones nos conducen al resultado 1, excepto cuando ambos valores son 0. Podemos aprovechar esto a nuestro favor. Si establecemos que el caso $(1,1)$ produce 0, considerándolo como nuestro "1", y el resto como "0", podemos construir una compuerta NOT muy simple. Esto se logra haciendo que la entrada de nuestra compuerta NOT, llamada "in", sea la entrada de la compuerta NAND, lo que resulta en solo dos casos posibles:

1. Ambas entradas del nand son 0
2. Ambas entradas del nand son 1

En todos los escenarios, la salida será opuesta a las entradas, lo que nos garantiza el comportamiento deseado de obtener una función NOT.

| a   | b   | out |
|:---:|:---:|:---:|
| 0   | 0   | 1   |
| 1   | 1   | 0   |

# AND

| a   | b   | out |
|:---:|:---:|:---:|
| 0   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

Para la compuerta AND, podemos notar que es el inverso de la compuerta NAND (obviamente). Por lo tanto, la creación de esta compuerta es sencilla: simplemente negamos la salida de la compuerta NAND con una compuerta NOT al final, y pasamos las entradas de nuestra compuerta AND a las entradas de la NAND, obteniendo así nuestra compuerta AND.

| a   | b   | out | not out |
|:---:|:---:|:---:|:-------:|
| 0   | 0   | 1   | 0       |
| 0   | 1   | 1   | 0       |
| 1   | 0   | 1   | 0       |
| 1   | 1   | 0   | 1       |

# OR

| a   | b   | out |
|:---:|:---:|:---:|
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 1   |

Como podemos observar en la tabla de verdad, la compuerta OR es muy parecida a la compuerta NAND, excepto que los valores de salida para $(0,0)$ y $(1,1)$ están "intercambiados". Nuestra solución es tan simple como negar las entradas de la compuerta NAND, de modo que la entrada $(0,0)$ se comporte como la entrada $(1,1)$ y la entrada $(1,1)$ como la $(0,0)$. Es importante notar que las demás combinaciones no se ven afectadas, ya que solo intercambian valor, pero el resultado de salida ya era el mismo en ambos casos.

# XOR

Para la compuerta XOR, inicialmente observamos que es el resultado de una operación AND entre la compuerta NAND y la compuerta OR, manteniendo únicamente las entradas donde hay valores comunes, como por ejemplo $(1,0)$ y $(0,1)$, para así obtener la compuerta XOR deseada.

| a   | b   | or  | nand | out |
|:---:|:---:|:---:| ---- | --- |
| 0   | 0   | 0   | 1    | 0   |
| 0   | 1   | 1   | 1    | 1   |
| 1   | 0   | 1   | 1    | 1   |
| 1   | 1   | 1   | 0    | 0   |

# MUX

El funcionamiento del multiplexor (MUX) permite seleccionar cuál de las entradas, "a" o "b", se reflejará en la salida, utilizando un selector al que en este caso llamamos "sel".

| a | b | sel | out |
|:-:|:-:|:---:|:---:|
| 0 | 0 | 0   | 0   |
| 0 | 0 | 1   | 0   |
| 0 | 1 | 0   | 0   |
| 0 | 1 | 1   | 1   |
| 1 | 0 | 0   | 1   |
| 1 | 0 | 1   | 0   |
| 1 | 1 | 0   | 1   |
| 1 | 1 | 1   | 1   |

Cuando "sel" es cero, la entrada reflejada es "a", mientras que si es uno, la entrada reflejada es "b". Para lograr esta funcionalidad, primero se niega la entrada "sel" para determinar cuándo es cero. Luego, se utilizan dos compuertas AND que tienen como entradas "a" y "notSel" para la primera, y "b" y "sel" para la segunda. Finalmente, se utiliza una compuerta OR para verificar si alguna de las dos compuertas AND ha reflejado un 1.

# DMUX

La compuerta Mux tiene como entradas "in" y "sel" y se encarga de decidir que salida será activada de esta forma:

| in | sel | out1 | out2 |
|:--:|:---:|:----:|:----:|
| 0  | 0   | 0    | 0    |
| 0  | 1   | 0    | 0    |
| 1  | 0   | 1    | 0    |
| 1  | 1   | 0    | 1    |

Para conseguir esta funcionalidad se hizo un procedimiento muy parecido al Mux, sin embargo en este caso las compuertas And comparan "a","sel" y "a","notSel" respectivamente, y la salida de cada And son "Out1" y "Out2" respectivamente.

# OR16

Después de haber creado previamente la compuerta OR, esta resulta ser particularmente simple y directa. Sus entradas consisten en un vector "a" de tamaño 16 y un vector "b" del mismo tamaño. Luego, se comparan una por una las posiciones de los vectores, por ejemplo: "Or(a=a[0], b=b[0], out=out[0])". Finalmente, como se mostró en el ejemplo anterior, la salida, denominada "out", es un vector de 16 valores.

# AND16

Esta situación es muy parecida a la anterior, con las mismas entradas y salidas. La única diferencia radica en que en lugar de tratarse de una serie de 16 compuertas OR, ahora tenemos una serie de 16 compuertas AND que comparan cada posición de los dos vectores de entrada. Por ejemplo: "And(a=a[0], b=b[0], out=out[0])".

# MUX16

En esta situación, una vez más, necesitamos replicar la compuerta original 16 veces, en este caso, la compuerta Mux. Las entradas consisten en dos vectores de 16 valores, "a" y "b", y un selector "sel". Luego, se repetirá la compuerta Mux 16 veces para cada una de las entradas de los vectores. Por ejemplo: "Mux(a=a[0], b=b[0], sel=sel, out=out[0])".

# MUX4WAY16

Para realizar el MUX4W16, primero observamos la tabla de verdad de la compuerta:


# DMUX4WAY


Para realizar el DMux4Way, primero observamos la tabla de verdad de la compuerta:

|sel\[1\]|sel\[0\]|out|
|:------:|:------:|:-:|
|    0   |    0   | a |
|    0   |    1   | b |
|    1   |    0   | c |
|    1   |    1   | d |

Siendo la entrada in $0$ o $1$. Ahora, como podemos observar, las salida $(a,b)$ y las salidas $(c,d)$ tienen el mismo bit en el selector $sel[1]$, por lo que podríamos gruparlas, obteniendo:



|sel\[1\]|  out  |
|:------:|:-----:|
|    0   |$(a,b)$|
|    1   |$(c,d)$|

Que es precisamente un demultiplexor sencillo. Al aplicarlo, aún requerimos los valores de $a$, $b$, $c$ y $d$ por separado, pero si nos fijamos bien, estos a su vez, generan un demultiplexor por cada par:

> Dmux $(a,b)$

|sel\[0\]|out|
|:------:|:-:|
|    0   |$a$|
|    1   |$b$|


> Dmux $(c,d)$

|sel\[0\]|out|
|:------:|:-:|
|    0   |$c$|
|    1   |$d$|


Teniendo así, nuestro demultiplexor.

# DMUX8WAY

Primero, observemos la tabla de verdad de nuestro demultiplexor.

| sel\[2\] | sel\[1\] | sel\[0\] | out |
|:--------:|:--------:|:--------:|:---:|
|     0    |     0    |     0    |  a  |
|     0    |     0    |     1    |  b  |
|     0    |     1    |     0    |  c  |
|     0    |     1    |     1    |  d  |
|     1    |     0    |     0    |  e  |
|     1    |     0    |     1    |  f  |
|     1    |     1    |     0    |  g  |
|     1    |     1    |     1    |  h  |

Sin embargo, al igual que con el DMux4Way, podemos notar que se puede dividir en dos grupos. Uno donde el bit sel 2 2 es igual a 0 con $abcd$, y otro donde sel 2 2 es igual a 1 con $efgh$. Ahora, podemos obtener la siguiente tabla.

| sel\[2\] |   out  |
|:--------:|:------:|
|     0    | $abcd$ |
|     1    | $efgh$ |

Como podemos observar, esto corresponde a un demultiplexor básico. Para obtener cada una de las salidas por separado, dirigimos cada salida de nuestro demultiplexor aplicado a través de dos demultiplexores de 4 entradas.

>Dmux4Way $(abcd)$

| sel\[1\] | sel\[0\] | out |
|:--------:|:--------:|:---:|
|     0    |     0    |  a  |
|     0    |     1    |  b  |
|     1    |     0    |  c  |
|     1    |     1    |  d  |

>Dmux4Way $(efgh)$

| sel\[1\] | sel\[0\] | out |
|:--------:|:--------:|:---:|
|     0    |     0    |  e  |
|     0    |     1    |  f  |
|     1    |     0    |  g  |
|     1    |     1    |  h  |

Obteniendo así, nuestro Dmux8Way.

# MUX4W16

Primero, haciendo la tabla de verdad del circuito, tenemos

|   A |  B |  C |  D |   sel[1] |   sel[0]  |   out |
|:---:|:--:|:--:|:--:|:--------:|:---------:|:-----:|
|   a |  b |  c |  d |     0    |      0    |    a  |
|   a |  b |  c |  d |     0    |      1    |    b  |
|   a |  b |  c |  d |     1    |      0    |    c  |
|   a |  b |  c |  d |     1    |      1    |    d  |

Observamos que podemos dividir esto en 2 grupos: el grupo $ab$ y el grupo $cd$. Sabemos que el bit $sel[0]$ nos dará $0$ o $1$, determinando qué valor se transmite. En el caso del grupo $ab$, $a$ correspondería a $0$ y $b$ a $1$. Lo mismo ocurre para el grupo $cd$, por lo que podemos tratarlos como dos multiplexores simples. Entonces tendríamos:

| A | B |   sel[0]  |   out |
|:-:|:-:|:---------:|:-----:|
| a | b |      0    |   a   |
| a | b |      1    |   b   |

y la tabla

| C | D |   sel[0]  |   out |
|:-:|:-:|:---------:|:-----:|
| c | d |      0    |   c   |
| c | d |      1    |   d   |

Al finalizar este proceso, obtendríamos la salida $a$ o $b$ y la salida $c$ o $d$. Por lo tanto, podríamos dirigir estas salidas a otro multiplexor que lea el bit $sel[1]$ para determinar cuál de los grupos se transmite. De esta manera, tendríamos:


| A/B |  C/D  |   sel[0]  |   out |
|:---:|:-----:|:---------:|:-----:|
| a/b |   c/d |      0    |  a/b  |
| a/b |   c/d |      1    |   c/d |

Por lo que nuesto multiplexor de 4ways estaría hecho. Para poderlo hacerlo con 16 entradas, simplemente aplicamos esto en Mux16 en vez de usar Mux.

# MUX8W16

Para este, podemos observar la tabla de datos

| A  | B  | C | D | E | F | G | H |   sel\[2\] | sel\[1\] |  sel\[0\] | out |
|----|----|---|---|---|---|---|---|------------|----------|-----------|-----|
| a  | b  | c | d | e | f | g | h | 0          | 0        | 0         | a   |
|  a |  b | c | d | e | f | g | h | 0          | 0        | 1         | b   |
| a  |  b | c | d | e | f | g | h | 0          | 1        | 0         | c   |
| a  |  b | c | d | e | f | g | h | 0          | 1        | 1         | d   |
| a  |  b | c | d | e | f | g | h | 1          |  0       |  0        | e   |
| a  |  b | c | d | e | f | g | h | 1          |  0       |  1        | f   |
| a  |  b | c | d | e | f | g | h | 1          |  1       |  0        | g   |
| a  |  b | c | d | e | f | g | h | 1          |  1       |  1        | h   |


Podemos notar la similitud con el Mux4W16, así que intentamos aplicar el mismo enfoque, dividiendo en dos grupos y luego aplicando un multiplexor a la salida. Al dividir en 2 grupos, obtenemos grupos de 4 elementos, por lo que utilizamos un Mux4W16 en cada uno de los grupos, $abcd$ y $efgh$. Al hacerlo, obtenemos dos salidas, v1 y v2, que podemos dirigir a través de un multiplexor normal de 16 entradas. El resultado es la salida del Mux7W16.


Preguntas Adicionales 

1-¿qué consideraciones importantes debe tener en cuenta para trabajar con Nand2Tetris?

Tenemos que tener compromiso con nuestro tiempo ya que es un curso completo 
que abarca desde la construcción de una computadora básica hasta la creación de 
un lenguaje de programación de alto nivel, por esto es importante dedicar tiempo 
suficiente para completar las tareas. 

Tenemos que seguir con el enfoque que tiene Nand2Tetris que se enfoca en paso a 
paso, desde la construcción de puertas lógicas hasta la implementación de un compilador. 
Es importante seguir este enfoque secuencial para comprender completamente cada etapa del proceso.

se tiene que llevar una práctica regular para mejorar en el diseño de hardware y software. 
Trabajar en los proyectos de Nand2Tetris regularmente ayudará a reforzar los conceptos y mejorar las habilidades.

Tenemos que tener en cuenta todos los recursos disponibles que nos ofrece Nand2Tetris proporciona 
una amplia gama de recursos, incluidos videos de conferencias, materiales de lectura y un foro de 
discusión en línea. con esto aprovechar al máximo todos estos recursos para profundizar en los conceptos. 

Aunque el proyecto se puede realizar de forma individual, también es beneficioso colaborar con otros 
estudiantes. La colaboración puede proporcionar diferentes perspectivas y ayudar a resolver problemas 
de manera más efectiva.

2- ¿qué otras herramientas similares a Nand2Tetris existen?

Digital Logic Design Courses (Cursos de Diseño Lógico Digital): Muchas universidades y plataformas 
educativas ofrecen cursos de diseño lógico digital que cubren desde conceptos básicos hasta diseño 
avanzado de circuitos digitales. Estos cursos a menudo incluyen proyectos prácticos que permiten a 
los estudiantes implementar y simular circuitos utilizando software especializado.

Proyectos de Verilog y VHDL: Verilog y VHDL son lenguajes de descripción de hardware (HDL) ampliamente 
utilizados en el diseño de circuitos integrados digitales. Los proyectos que involucran la escritura 
de código en Verilog o VHDL y su posterior síntesis y simulación son una excelente manera de aprender 
sobre diseño de hardware a nivel de registro.

Cursos de Arquitectura de Computadoras: Los cursos de arquitectura de computadoras a menudo incluyen 
proyectos prácticos que van desde la construcción de una unidad de procesamiento básica hasta la implementación 
de un conjunto de instrucciones y la creación de un simulador de CPU.

Simuladores de Circuitos Digitales: Hay varios simuladores de circuitos digitales disponibles que permiten 
a los estudiantes diseñar, simular y depurar circuitos digitales. Estos simuladores proporcionan una forma 
interactiva de aprender sobre la lógica digital y el diseño de circuitos.

Plataformas de Programación de FPGA (Field-Programmable Gate Array): Las plataformas de programación de FPGA, 
como Altera (ahora parte de Intel) y Xilinx, proporcionan herramientas y recursos para diseñar y programar 
circuitos digitales en hardware reconfigurable. Estas plataformas ofrecen una excelente oportunidad para 
aprender sobre diseño de hardware a nivel de sistema.
