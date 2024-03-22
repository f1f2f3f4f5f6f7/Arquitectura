import sys
import parseador as ps
import codificador as cd

tabla_de_valores = {
    "SCREEN" : 16384,
    "KBD" : 24576,
    "SP" : 0,
    "LCL" : 1,
    "ARG" : 2,
    "THIS" : 3,
    "THAT": 4
}

for i in range(16):
    llave = "R" + str(i)
    tabla_de_valores[llave] = i

def ejecutar_principal(tabla_de_valores):
    lineas_codigo = []
    nombre_archivo_entrada = sys.argv[1]
    with open(nombre_archivo_entrada, 'r') as archivo:
        for linea in archivo:
            linea = ps.parseo(linea)
            if linea.tipo == None:
                continue
            lineas_codigo.append(linea)
    
    tabla_de_valores = cd.agregar_al_diccionario(tabla_de_valores, lineas_codigo)
    tabla_de_valores = cd.agregar_segundo(tabla_de_valores, lineas_codigo)

    nombre_archivo_salida = nombre_archivo_entrada[:nombre_archivo_entrada.find('.asm')] + ".hack"
    with open(nombre_archivo_salida, 'w') as archivo_salida:
        for i in lineas_codigo:
            instruccion = ""
            if i.tipo == 'C':
                instruccion = "111" + cd.codigo_operacion(i.get_operacion()) + cd.codigo_destino(i.get_destino()) + cd.codigo_salto(i.get_salto())
                archivo_salida.write(instruccion + '\n')
            elif i.tipo == 'A':
                instruccion = cd.codigo_valor(i.get_valor(), tabla_de_valores)
                instruccion = "0" + instruccion
                archivo_salida.write(instruccion + '\n')
    

if __name__ == '__main__':
    ejecutar_principal(tabla_de_valores)
