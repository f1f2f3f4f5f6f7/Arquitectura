# Tercer práctica. Tercera parte.

El laboratorio número 3 se enfoca en llevar a cabo y ejecutar los proyectos 4 y 5 de nand2tetris, los cuales están ubicados en la carpeta de proyectos de la aplicación. Estos proyectos requieren el uso del lenguaje de máquina en una forma comprensible para la programación, así como también hacen uso de la plataforma Hack y su lenguaje ensamblador.

## ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?

El lenguaje de máquina es fundamental para definir la arquitectura computacional por varias razones:

1. **Interacción directa con el hardware**: El lenguaje de máquina es el único lenguaje que el hardware de la computadora puede entender directamente. Define las instrucciones básicas que la CPU puede ejecutar, como sumar dos números, mover datos de un lugar a otro en la memoria, etc.

2. **Estándares de la arquitectura**: El lenguaje de máquina establece el conjunto de instrucciones y operaciones que una arquitectura computacional particular puede realizar. Esto permite la interoperabilidad y la compatibilidad entre diferentes sistemas y programas que se ejecutan en la misma arquitectura.

3. **Eficiencia y optimización**: Al compilar programas en lenguaje de máquina específico para una arquitectura computacional particular, los desarrolladores pueden optimizar el rendimiento de sus aplicaciones, aprovechando las características específicas del hardware subyacente.


## ¿Qué diferencia ven entre arquitectura computacional, arquitectura de software y arquitectura del sistema?

| Aspecto                | Arquitectura Computacional                      | Arquitectura de Software                        | Arquitectura del Sistema                        |
|------------------------|--------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| Enfoque                | Hardware                                         | Software                                        | Hardware y Software                             |
| Definición             | Estructura y diseño del hardware de la computadora | Estructura y diseño del software               | Combinación de hardware y software              |
| Componentes            | CPU, memoria, buses de datos, periféricos, etc. | Algoritmos, estructuras de datos, módulos, etc. | Hardware, sistema operativo, servicios, etc.    |
| Interacción            | Instrucciones y operaciones de bajo nivel        | Funciones, objetos, APIs, interfaces, etc.     | Interacción entre hardware y software           |
| Optimización           | Rendimiento, eficiencia, consumo de energía      | Funcionalidad, modularidad, mantenibilidad     | Integración, rendimiento, compatibilidad, etc.  |
| Ejemplos               | Arquitectura x86, ARM, RISC-V, etc.              | Arquitectura de software de una aplicación     | Arquitectura de un sistema operativo, aplicaciones, etc. |

## BONUS

## Como informático o computista: ¿La arquitectura computacional o la arquitectura del sistema no tiene en cuenta igualmente la arquitectura de software?

Como informático o computista, es importante comprender que la arquitectura computacional, la arquitectura del sistema y la arquitectura de software son conceptos interrelacionados pero distintos en el ámbito de la informática.

cada uno se enfoca en aspectos diferentes de un sistema computacional. La arquitectura computacional y la arquitectura del sistema se ocupan principalmente del hardware y del software de bajo nivel, mientras que la arquitectura de software se centra en los aspectos de alto nivel del diseño y la implementación del software.

Es crucial tener en cuenta la arquitectura de software al diseñar sistemas computacionales, ya que influye en la eficiencia, la mantenibilidad, la escalabilidad y otras características importantes del sistema. Por lo tanto, aunque la arquitectura computacional y la arquitectura del sistema son fundamentales, no se puede ignorar la importancia de la arquitectura de software en el desarrollo de sistemas informáticos robustos y eficientes.


## Proyecto 4: 
# Descripción de los programas
Se presenta una breve explicación sobre la construcción y el funcionamiento básico de los programas del proyecto 4 de nand2tetris.

# Mult:
Este programa utiliza las 16 palabras principales de la RAM (RAM[0]...RAM[15]) para calcular R0*R1 y almacenar el resultado en R2. El cálculo se realiza mediante una secuencia de instrucciones que multiplican los valores contenidos en R0 y R1, guardando el resultado en R2. Esta operación es esencial en la computadora Hack y se emplea para diversas tareas como cálculos matemáticos y manipulación de datos.

# Fill:
Este programa demuestra cómo manipular los dispositivos de pantalla y teclado a nivel básico. Monitoriza constantemente la entrada del teclado y oscurece la pantalla (poniendo cada píxel en negro) mientras una tecla está siendo presionada.

## Proyecto 5: 
# Descripción de los chips
Se proporciona una breve explicación sobre la construcción y el funcionamiento de los chips del proyecto 5 de nand2tetris.

# Memory:
Este chip facilita las operaciones básicas de lectura y escritura en la memoria de la computadora Hack. Selecciona la ubicación de memoria donde cargar la orden (RAM16K, pantalla o teclado) utilizando un DMux4Way. Luego, utiliza un Ram16k para almacenar la entrada y dirigirla a la pantalla y al teclado, y finalmente, emplea un Mux4Way16 para enviar la salida adecuada.

# CPU:
La CPU de Hack consta de una ALU, registros A y D, y un contador de programa PC. Ejecuta las instrucciones del lenguaje de máquina Hack, refiriéndose a los registros integrados en la CPU y la posición de memoria externa apuntada por A.

# Computer:
La computadora HACK se compone de la CPU, la ROM y la RAM. Al reiniciar, ejecuta el programa almacenado en la memoria ROM. Si se activa el reset, se reinicia la ejecución del programa actual. Para iniciar un programa, el usuario debe presionar el botón de reset, lo que permite la interacción con la computadora a través del teclado y la visualización de resultados en la pantalla.





