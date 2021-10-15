from Entorno.Valor import Value
from Generator.Generator import Generator
from abc import ABC, abstractclassmethod
from Entorno.Entorno import Environment

class Instruction(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.generator = Generator()

    @abstractclassmethod
    def compile(self, entorno: Environment) -> Value:
        pass