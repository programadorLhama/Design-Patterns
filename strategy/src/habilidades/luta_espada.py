from .interfaces import Ihabilidade

class LutaEspada(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel
    
    def comportamento(self):
        print("Lutar com espada")
    
    def nivel_atributo(self):
        print('Nivel de uso Espada: {}'.format(self.nivel))
