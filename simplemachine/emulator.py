from utils.exceptions import EmulatorException

from memory import memory
from processor import cpu


class Emulator(object):
    """
    This class is used to manage the entire emulation process.
    It is practically a wrapper which joins the CPU and the memory to a unified data structure
    """

    def __init__(self):
        self.__memory = memory.Memory()
        self.__cpu = cpu.Processor(self.__memory)

    def load_code(self, code):
        """
        Loads the code to the memory.
        A SimpleMachine can load the code only once.

        :param code: A list of bytes
        """
        self.__memory.code = code

    def run(self):
        """
        Starts the CPU with the given code
        """
        if not len(self.__memory.code):
            raise EmulatorException("No code was loaded to the SimpleMachine")
        self.__cpu.run()
