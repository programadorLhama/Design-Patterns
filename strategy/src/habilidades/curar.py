from .interfaces import Ihabilidade

class Curar(Ihabilidade):

    def __init__(self, nivel):
        self.nivel = nivel
    
    def comportamento(self):
        print("Curar Personagem")
    
    def nivel_atributo(self):
        print('Nivel de Cura: {}'.format(self.nivel))