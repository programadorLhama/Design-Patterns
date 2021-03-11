from abc import ABC, abstractmethod

class Observador(ABC):

    @abstractmethod
    def update(self):
        pass
