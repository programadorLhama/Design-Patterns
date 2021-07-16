from .interface import ValidatorInterface

class CarneValidator(ValidatorInterface):

    def validate(self, comida: str) -> bool:
        if comida == 'carne': return True
        return False
    
    def action(self) -> None:
        print('O Leao come a carne')