from typing import Type
from .habilidades import Ihabilidade

class Guerreiro:
    
    def __init__(self, habilidade: Type[Ihabilidade]):
        self.habilidade = habilidade
    
    def acao(self):
        # Processamento
        self.habilidade.comportamento()
    
    def attributos(self):
        self.habilidade.nivel_atributo()
