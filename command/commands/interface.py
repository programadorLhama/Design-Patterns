from abc import ABC, abstractmethod

class CommandInterface(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass