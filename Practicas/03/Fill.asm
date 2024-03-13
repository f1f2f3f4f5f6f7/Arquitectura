// Ejecuta un bucle infinito que escucha la entrada del teclado.
// Cuando se presiona una tecla (cualquier tecla), el programa ennegrece la pantalla,
// es decir, escribe "negro" en cada píxel;
// la pantalla debe permanecer completamente negra mientras se presione la tecla. 
// Cuando no se presiona ninguna tecla, el programa borra la pantalla, es decir, escribe
// "blanco" en cada píxel;
// la pantalla debe permanecer completamente clara mientras no se presione ninguna tecla.


(inicio)
    @color  // Almacena el color actual de la pantalla: 0 para blanco, -1 para negro.
    M=0

    // Almacena la posición actual en la que estamos iterando en la pantalla.
    @SCREEN
    D=A
    @posicion
    M=D

    // Se mantiene a la espera de la presión de una tecla.
(presionar)
    @KBD
    D=M
    @negro
    D; JGT // Si hay alguna tecla presionada, almacena el color negro.

    @blanco
    D; JEQ // Si no hay tecla presionada, almacena blanco.

    @presionar
    0; JMP // Vuelve al ciclo para seguir esperando la presión de teclas.

(negro)
    @color
    M=-1 // Almacena el color negro (-1 significa que todos los bits están activados).
    @mostrar
    0; JMP // Saltamos para pintar la pantalla de negro.

(blanco)
    @color
    M=0 // Almacena el color blanco (todos los bits desactivados).
    @mostrar
    0; JMP // Saltamos para pintar la pantalla de blanco.

(mostrar)
    // Almacenamos el color actual en el registro D.
    @color
    D=M

    // Tomamos la posición almacenada y le asignamos el color.
    @posicion
    A=M
    M=D

    // Incrementamos la posición en uno.
    @posicion
    M=M+1

    // Verificamos si la siguiente posición es igual a la dirección de KBD para finalizar.
    @KBD
    D=A
    @posicion
    D=D-M

    // Si la posición de KBD menos la almacenada sigue siendo positiva, continuamos.
    @mostrar
    D; JGT

    // Si terminamos de pintar, regresamos al inicio.
    @inicio
    0; JMP