"""
This module is used to emulate a CPU.
The CPU should have access to the code, the stack and may execute opcodes.
"""

from simplemachine.processor.decoder import Decoder
from simplemachine.processor.executor import Executor
from simplemachine.processor.exceptions import IPOutOfBounds


class Processor(object):
    """
    The processor is the main unit which is used to process and run the SimpleMachine opcodes
    This implementation imitates the normal pipeline of opcode execution in an average CPU
    """
    def __init__(self, memory):
        """

        :param memory: The memory which the processor may access and use
        :type memory: simplemachine.memory.memory.Memory
        """
        self.__ip = 0
        self.__memory = memory
        self.__executor = Executor(self)

    @property
    def memory(self):
        return self.__memory

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, value):
        """
        Sets the instruction pointer of the CPU
        The instruction pointer may not point to outside of the code section

        :param value: The new value of the ip
        """
        if value < 0:
            raise IPOutOfBounds("IP must be greater than 0!")
        if value > len(self.__memory.code):
            raise IPOutOfBounds("IP must be smaller than the length of the code")

        self.__ip = value

    def run(self):
        """
        Runs the CPU with the current code loaded.
        The CPU works in a similar fashion to a regular CPU execution flow.

        Fetched the opcode from the code memory
        Decodes the opcode and finds the matching executor
        Executes the matching executor with it's arguments
        """
        idx = 0
        code_length = len(self.__memory.code)
        while 0 <= self.__ip < code_length:
            idx += 1
            opcode = self.__memory.code[self.__ip]
            self.__ip += 1
            opcode_executor_function, args = Decoder.decode(opcode)
            opcode_executor_function(self.__executor, *args)
