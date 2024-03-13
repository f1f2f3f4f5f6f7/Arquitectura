// Determinar si RAM[0] es menor que cero
@0
D=M
@terminar
D; JLT

// Determinar si RAM[1] es menor que cero
@1
D=M
@terminar
D; JLT

@2
M=0

// Inicializar el contador
@contador
M=D

// Donde se almacenará la multiplicación
@multiplicacion
M=0

(LOOP)

// Si el contador es igual a cero, hacer stop
@contador
D=M
@STOP
D; JEQ

// Disminuir el contador en uno
@contador
M=M-1

// Sumar
@multiplicacion
D=M
@0
D=D+M
@multiplicacion
M=D

@LOOP
0; JMP

(STOP)

// Asignar la multiplicación a RAM[2]
@multiplicacion
D=M
@2
M=D

(terminar)

(FINAL)
@FINAL
0; JMP
