from validators import CarneValidator, NosValidator, BananaValidator

class Validacao:

    def __init__(self) -> None:
        self.val = [
            BananaValidator(),
            NosValidator(),
            CarneValidator()
        ]

    def process(self, comida: str):
        for v in self.val:
            if v.validate(comida): return v.action()


validacao = Validacao()
validacao.process('carne')