# Quinta práctica. Quinta parte

## Explicación

**1. Introducción al proyecto:**

El proyecto de laboratorio se desarrolla en el contexto de la construcción de un traductor de máquina virtual (VM), una parte esencial en el proceso de desarrollo de software. Este traductor convierte programas escritos en el lenguaje de la VM en programas escritos en el lenguaje de ensamblaje de Hack, lo que permite ejecutar programas de nivel más alto en una arquitectura de hardware específica.

**2. Objetivo:**

- **Proyecto 7:** El objetivo principal de esta fase es construir un traductor de VM básico que se enfoque en la implementación de los comandos de aritmética de pila y acceso a memoria del lenguaje VM. Esto sienta las bases para proyectos posteriores al proporcionar una comprensión fundamental de la traducción entre diferentes niveles de abstracción en la computación.

- **Proyecto 8 :** En esta etapa, la meta es extender el traductor básico construido en el Proyecto 7 en un traductor de VM a gran escala. Aquí, nos centramos en manejar los comandos de control de programa de la VM, como las ramificaciones y las llamadas de funciones. Esta ampliación permite una traducción más completa y precisa de los programas de VM a programas de ensamblaje de Hack.

**3. Implementación propuesta:**

- **Proyecto 7:** Para cumplir con el objetivo del proyecto 7, se propone implementar el traductor de VM básico en dos etapas distintas. En la primera etapa, se manejan los comandos de aritmética de pila, mientras que en la segunda etapa, se abordan los comandos de acceso a memoria, como la manipulación de diferentes segmentos de memoria.

- **Proyecto 8:** La fase de extensión del proyecto 8 sigue una estructura similar, pero se enfoca en la traducción de comandos de control de programa. En la primera etapa, se implementa y prueba la traducción de comandos de ramificación, mientras que en la segunda etapa, se abordan los comandos de llamada y retorno de funciones, completando así la traducción de programas de VM a programas de ensamblaje de Hack.

**4. Contracto y recursos:**

Se proporcionan especificaciones detalladas sobre el contrato del proyecto, incluyendo lecturas relevantes del material del curso y herramientas necesarias para el desarrollo, como el emulador de CPU y el emulador de VM. Estos recursos son fundamentales para comprender y ejecutar con éxito los programas de prueba suministrados.

**5. Testing:**

La fase de prueba juega un papel crucial en la verificación del correcto funcionamiento del traductor de VM en cada etapa del proyecto. Se describen los programas de prueba suministrados y se detallan los pasos para ejecutar y verificar la implementación del traductor en diferentes escenarios, lo que garantiza la precisión y la robustez del traductor desarrollado.

**6. Conclusiones y recomendaciones:**

Se enfatiza la importancia de seguir el orden de implementación propuesto y se sugiere guardar copias de seguridad del traductor de VM en cada etapa del proyecto para futuras modificaciones. Además, se destaca la necesidad de comprender a fondo las especificaciones del proyecto y utilizar los recursos proporcionados de manera efectiva para lograr resultados exitosos.






## Preguntas

### 1- Teniendo en cuenta el marco de estas dos prácticas que son las máquinas virtuales. ¿Cuál cree que es el futuro de las máquinas virtuales?
El futuro de las máquinas virtuales parece estar profundamente arraigado en el desarrollo continuo de tecnologías de virtualización y la evolución de los entornos de computación. La necesidad de traducir programas escritos en lenguajes de máquinas virtuales a lenguajes de bajo nivel, como se describe en los textos sobre la construcción de traductores VM a Hack, sugiere que las máquinas virtuales seguirán siendo una parte crucial de la abstracción de hardware y la portabilidad de software. A medida que las aplicaciones se vuelven más complejas y distribuidas, las máquinas virtuales proporcionan una forma eficiente de gestionar recursos de hardware y ejecutar aplicaciones de manera aislada. Además, con el aumento de la adopción de la computación en la nube y la necesidad de escalabilidad y flexibilidad, las máquinas virtuales probablemente jugarán un papel importante en la gestión y el aprovisionamiento de recursos en infraestructuras de nube públicas y privadas.

### 2- ¿Cual es la principal similitud entre un contenedor y una máquina virtual?
La principal similitud entre un contenedor y una máquina virtual, es que ambos proporcionan un entorno de ejecución aislado para las aplicaciones. En el caso de las máquinas virtuales, esto se logra mediante la virtualización del hardware subyacente, lo que permite ejecutar múltiples sistemas operativos y aplicaciones en un solo servidor físico. Por otro lado, los contenedores utilizan la virtualización a nivel de sistema operativo para lograr el aislamiento, lo que significa que comparten el mismo kernel del sistema operativo del host pero tienen su propio espacio de usuario y sistemas de archivos. Esto permite que múltiples contenedores se ejecuten en una sola instancia de un sistema operativo, lo que resulta en una mayor eficiencia en términos de recursos compartidos y tiempos de inicio más rápidos en comparación con las máquinas virtuales.

## BONUS

### ¿Cual es la ventaja del contenedor respecto a la máquina virtual?
La ventaja del contenedor sobre la máquina virtual, es su eficiencia y velocidad. Los contenedores comparten recursos con el sistema operativo del host, lo que los hace más livianos en términos de recursos y más rápidos de iniciar en comparación con las máquinas virtuales, que requieren la ejecución de un sistema operativo completo. Esta eficiencia los hace ideales para implementaciones ágiles y escalables en entornos de desarrollo y producción, donde la velocidad y la capacidad de escalar rápidamente son fundamentales. Sin embargo, es importante tener en cuenta que los contenedores también tienen limitaciones en términos de aislamiento de recursos y seguridad en comparación con las máquinas virtuales, lo que significa que la elección entre contenedores y máquinas virtuales depende de los requisitos específicos de cada aplicación y entorno de implementación.




