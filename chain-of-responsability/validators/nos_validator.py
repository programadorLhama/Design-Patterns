from .interface import ValidatorInterface

class NosValidator(ValidatorInterface):

    def validate(self, comida: str) -> bool:
        if comida == 'nos': return True
        return False
    
    def action(self) -> None:
        print('O esquilo come a nos')