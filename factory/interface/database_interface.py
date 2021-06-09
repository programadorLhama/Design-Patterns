from abc import ABC, abstractmethod

class DatabaseInterface(ABC):

    @abstractmethod
    def select_one(self):
        pass
