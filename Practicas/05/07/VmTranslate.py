import os
import glob

class VMParser(object):
    def __init__(self, vm_filename):
        # Inicializa el objeto VMParser con el nombre del archivo VM.
        self.vm_archive = vm_filename
        self.vm = open(vm_filename, 'r')
        self.commands = self.commands_dict()
        self.curr_instruction = None
        self.start_file()

    def advance(self):
        # Avanza al siguiente comando en el archivo VM.
        self.curr_instruction = self.next_instruction
        self.load_next_instruction()

    @property
    def has_more_commands(self):
        # Verifica si hay más comandos en el archivo VM.
        return bool(self.next_instruction)

    @property
    def command_type(self):
        # Devuelve el tipo de comando actual.
        return self.commands.get(self.curr_instruction[0].lower())

    @property
    def arg1(self):
        # Devuelve el primer argumento del comando.
        if self.command_type == 'C_ARITHMETIC':
            return self.argn(0)
        return self.argn(1)

    @property
    def arg2(self):
        '''Solo devuelve si es C_PUSH, C_POP, C_FUNCTION, C_CALL'''
        return self.argn(2)

    def start_file(self):
        # Ubica el puntero del archivo al inicio y carga el primer comando.
        self.vm.seek(0)
        line = self.vm.readline().strip()
        while not self.is_instruction(line):
            line = self.vm.readline().strip()
        self.load_next_instruction(line)

    def load_next_instruction(self):
        # Carga el siguiente comando del archivo VM.
        stripped_lines = (line.strip().split("//")[0].strip().split() for line in self.vm)
        self.next_instruction = next((line for line in stripped_lines if self.is_instruction(line)), None)

    def is_instruction(self, line):
        # Verifica si la línea es un comando válido.
        return line and line[:2] != "//"

    def argn(self, n):
        # Devuelve el enésimo argumento del comando.
        if len(self.curr_instruction) >= n+1:
            return self.curr_instruction[n]
        return None

    def commands_dict(self):
        # Diccionario que mapea los comandos VM a sus tipos correspondientes.
        return {
            'add': 'C_ARITHMETIC',
            'sub': 'C_ARITHMETIC',
            'neg': 'C_ARITHMETIC',
            'eq': 'C_ARITHMETIC',
            'gt': 'C_ARITHMETIC',
            'lt': 'C_ARITHMETIC',
            'and': 'C_ARITHMETIC',
            'or': 'C_ARITHMETIC',
            'not': 'C_ARITHMETIC',
            'push': 'C_PUSH',
            'pop': 'C_POP',
            'label': 'C_LABEL',
            'goto': 'C_GOTO',
            'if-goto': 'C_IF',
            'function': 'C_FUNCTION',
            'return': 'C_RETURN',
            'call': 'C_CALL'
        }


class VMCodeWriter(object):
    def __init__(self, asm_filename):
        # Inicializa el objeto VMCodeWriter con el nombre del archivo de salida.
        self.asm = open(asm_filename, 'w')
        self.curr_file = None
        self.bool_count = 0 
        self.addresses = self.address_dict()

    def set_file_name(self, vm_filename):
        # Establece el nombre del archivo VM actual.
        self.curr_file = vm_filename.replace('.vm', '').split('/')[-1]

    def write_arithmetic(self, operation):
        # Escribe el código ensamblador para comandos aritméticos.
        operations = {
            'add': 'M=M+D',
            'sub': 'M=M-D',
            'and': 'M=M&D',
            'or': 'M=M|D',
            'neg': 'M=-M',
            'not': 'M=!M',
        }

        jumps = {
            'eq': 'D;JEQ',
            'gt': 'D;JGT',
            'lt': 'D;JLT',
        }

        if operation not in ['neg', 'not']:
            self.pop_stack_to_D()
        self.decrement_SP()
        self.set_A_to_stack()

        if operation in operations:
            self.write(operations[operation])
        elif operation in jumps:
            self.write('D=M-D')
            self.write(f'@BOOL{self.bool_count}')
            self.write(jumps[operation])
            self.set_A_to_stack()
            self.write('M=0')
            self.write(f'@ENDBOOL{self.bool_count}')
            self.write('0;JMP')
            self.write(f'(BOOL{self.bool_count})')
            self.set_A_to_stack()
            self.write('M=-1')
            self.write(f'(ENDBOOL{self.bool_count})')
            self.bool_count += 1
        else:
            self.raise_unknown(operation)
        self.increment_SP()

    def write_push_pop(self, command, segment, index):
        # Escribe el código ensamblador para comandos push y pop.
        self.resolve_address(segment, index)
        if command == 'C_PUSH':
            if segment == 'constant':
                self.write('D=A')
            else:
                self.write('D=M')
            self.push_D_to_stack()
        elif command == 'C_POP': 
            self.write('D=A')
            self.write('@R13') 
            self.write('M=D')
            self.pop_stack_to_D()
            self.write('@R13')
            self.write('A=M')
            self.write('M=D')
        else:
            self.raise_unknown(command)

    def close(self):
        # Cierra el archivo de salida.
        self.asm.close()

    def write(self, command):
        # Escribe una línea de código en el archivo de salida.
        self.asm.write(command + '\n')

    def raise_unknown(self, argument):
        # Lanza una excepción para argumentos desconocidos.
        raise ValueError('{} is an invalid argument'.format(argument))

    def resolve_address(self, segment, index):
        # Resuelve la dirección de memoria para un segmento dado.
        address = self.addresses.get(segment)
        if segment == 'constant':
            self.write(f'@{index}')
        elif segment == 'static':
            self.write(f'@{self.curr_file}.{index}')
        elif segment in ['pointer', 'temp']:
            self.write(f'@R{address + int(index)}') 
        elif segment in ['local', 'argument', 'this', 'that']:
            self.write(f'@{address}') 
            self.write('D=M')
            self.write(f'@{index}')
            self.write('A=D+A') 
        else:
            self.raise_unknown(segment)

    def address_dict(self):
        # Diccionario que mapea los segmentos de memoria a sus direcciones.
        return {
            'local': 'LCL',
            'argument': 'ARG', 
            'this': 'THIS', 
            'that': 'THAT', 
            'pointer': 3, 
            'temp': 5, 
            'static': 16, 
        }

    def push_D_to_stack(self):
        # Realiza la operación push en la pila.
        self.write('@SP') 
        self.write('A=M') 
        self.write('M=D') 
        self.write('@SP') 
        self.write('M=M+1')

    def pop_stack_to_D(self):
        # Realiza la operación pop desde la pila.
        self.write('@SP')
        self.write('M=M-1') 
        self.write('A=M') 
        self.write('D=M') 

    def decrement_SP(self):
        # Decrementa el puntero de pila (SP).
        self.write('@SP')
        self.write('M=M-1')

    def increment_SP(self):
        # Incrementa el puntero de pila (SP).
        self.write('@SP')
        self.write('M=M+1')

    def set_A_to_stack(self):
        # Establece el registro A al valor en la cima de la pila (SP).
        self.write('@SP')
        self.write('A=M')


class Main(object):
    def __init__(self, file_path):
        # Inicializa el proceso de traducción para los archivos VM.
        self.parse_files(file_path)
        self.cw = VMCodeWriter(self.asm_file)
        for vm_file in self.vm_files:
            self.translate(vm_file)

    def translate(self, vm_file):
        # Traduce un archivo VM dado en código ensamblador.
        parser = VMParser(vm_file)
        self.cw.set_file_name(vm_file)
        while parser.has_more_commands:
            parser.advance()
            self.cw.write('// ' + ' '.join(parser.curr_instruction))
            if parser.command_type == 'C_PUSH':
                self.cw.write_push_pop('C_PUSH', parser.arg1, parser.arg2)
            elif parser.command_type == 'C_POP':
                self.cw.write_push_pop('C_POP', parser.arg1, parser.arg2)
            elif parser.command_type == 'C_ARITHMETIC':
                self.cw.write_arithmetic(parser.arg1)

    def parse_files(self, file_path):
        # Analiza los archivos VM o el directorio de archivos VM en la ruta especificada.
        file_path = file_path.rstrip('/')
        if file_path.endswith('.vm'):
            self.asm_file = file_path.replace('.vm', '.asm')
            self.vm_files = [file_path]
        else:
            self.asm_file = os.path.join(file_path, os.path.basename(file_path) + '.asm')
            self.vm_files = glob.glob(os.path.join(file_path, '*.vm'))


if __name__ == '__main__':
    import sys

    file_path = sys.argv[1]
    Main(file_path)
