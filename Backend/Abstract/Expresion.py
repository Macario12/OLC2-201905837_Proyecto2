from Entorno.Entorno import Environment
from Entorno.Valor import Value
from Generator.Generator import Generator
from abc import ABC, abstractclassmethod


class Expresion(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.generator: Generator = None
        self.trueLabel = ""
        self.falseLabel = ""

    @abstractclassmethod
    def compile(self, entorno: Environment) -> Value:
        pass