# @property + @setter - getter e setter no modo Pythonico
# - como getter
# - para evitar quebrar código cliente
# - para habilitar setter
# - para executar ações ao obter o atributo
# Atributos que começa com um ou dois underlines
# não devem ser usdos forma da classe.
class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, value):
        self._cor = value

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, value):
        self._cor_tampa = value


caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)
