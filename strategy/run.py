from src import Guerreiro, UsoArco, LutaEspada, Curar, LutaMarchado

cavaleiro = Guerreiro(LutaEspada(6))
arqueiro = Guerreiro(UsoArco(9))
curandeiro = Guerreiro(Curar(7))
cavaleiroMarchado = Guerreiro(LutaMarchado(8))

cavaleiro.acao()
arqueiro.acao()
arqueiro.attributos()
curandeiro.attributos()
cavaleiroMarchado.acao()