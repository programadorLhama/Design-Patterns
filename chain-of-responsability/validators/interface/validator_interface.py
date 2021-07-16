from abc import ABC, abstractmethod

class ValidatorInterface(ABC):

    @abstractmethod
    def validate(self, comida: str) -> bool:
        pass
    
    @abstractmethod
    def action(self) -> None:
        pass
