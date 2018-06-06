from decoder import register_opcode, register_range_opcode
from alu import ArithmeticLogicUnit
from sys import stdout, stdin


class Executor(object):
    """
    This class is the executor of the CPU.
    All of the opcodes are implemented here.
    """
    STDIN = stdin
    STDOUT = stdout

    def __init__(self, cpu):
        """
        :param cpu: The CPU
        :type cpu: simplemachine.processor.cpu.Processor
        """
        self.__cpu = cpu

    @register_opcode(0x0)
    def add(self):
        """
        Pops 2 items from the stack and adds them.
        The result is pushed to the stack.
        """
        first_operand = self.pop()
        second_operand = self.pop()
        self.__cpu.memory.stack.push(ArithmeticLogicUnit.add(first_operand, second_operand))

    @register_opcode(0x1)
    def subtract(self):
        """
        Pops 2 items from the stack. Subtracts the second popped item from the first.
        The result is pushed to the stack.
        """
        first_operand = self.pop()
        second_operand = self.pop()
        self.__cpu.memory.stack.push(ArithmeticLogicUnit.subtract(first_operand, second_operand))

    @register_opcode(0x2)
    def divide(self):
        """
        Pops 2 items from the stack. Divides the first popped item by the second.
        The division result and remainder are pushed to the stack. The remainder pushed last.
        """
        first_operand = self.pop()
        second_operand = self.pop()
        div_result, mod_result = ArithmeticLogicUnit.divide(first_operand, second_operand)
        self.__cpu.memory.stack.push(div_result)
        self.__cpu.memory.stack.push(mod_result)

    @register_opcode(0x3)
    def multiply(self):
        """
        Pops 2 items from the stack and multiplies them.
        The result is pushed to the stack.
        """
        first_operand = self.pop()
        second_operand = self.pop()
        self.__cpu.memory.stack.push(ArithmeticLogicUnit.multiply(first_operand, second_operand))

    @register_opcode(0x8)
    def read(self):
        """
        Reads a byte from stdin. The byte is pushed to the stack
        """
        self.__cpu.memory.stack.push(ord(Executor.STDIN.read(1)))

    @register_opcode(0x9)
    def write(self):
        """
        Writes an ASCII char to stdout
        """
        Executor.STDOUT.write(chr(self.pop()))

    @register_opcode(0x10)
    def jump(self):
        """
        Pops an offset from the stack, adds it to IP.
        """
        offset = self.pop()
        self.__cpu.ip += offset

    @register_opcode(0x11)
    def call(self):
        """
        Pops an offset from the stack, adds it to IP.
        Before jumping, pushes the current IP.
        """
        offset = self.pop()
        self.__cpu.memory.stack.push(self.__cpu.ip)
        self.__cpu.ip += offset

    @register_opcode(0x12)
    def ret(self):
        """
        Pops value from the stack, moves IP to the popped value.
        """
        self.__cpu.ip = self.pop()

    @register_opcode(0x14)
    def cje(self):
        """
        Jumps to stack[0] if stack[1] == stack[2]. pops all values either way.
        """
        offset = self.pop()
        if self.pop() == self.pop():
            self.__cpu.ip += offset

    @register_opcode(0x18)
    def jse(self):
        """
        Pops an offset from the stack. If the stack is empty after, jumps to the offset popped.
        """
        offset = self.pop()
        if self.__cpu.memory.stack.empty():
            self.__cpu.ip += offset

    @register_opcode(0x20)
    def pop(self):
        """
        Pops an item from the top of the stack.
        """
        return self.__cpu.memory.stack.pop()

    @register_range_opcode(0x20, 0x40)
    def swap(self, index):
        """
        Swaps the element at HEAD with the element at index.

        :param index: The index of the element to swap the head of the stack with
        """
        self.__cpu.memory.stack.swap(index)

    @register_range_opcode(0x40, 0x7f)
    def load(self, offset):
        """
        Pushes the value at stack[offset] to the stack.

        :param offset: The element offset from the head of the stack to load
        """
        self.__cpu.memory.stack.load(offset)

    @register_range_opcode(0x80, 0xff)
    def push(self, value):
        """
        Pushes a value to the top of the stack

        :param value: The value to push to the stack
        """
        self.__cpu.memory.stack.push(value)
