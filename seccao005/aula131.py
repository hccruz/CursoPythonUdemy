# @property - getter no modo Pythonico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythonico - modo Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo
# Geralmente é usada nas seguintes situações
# - como getter
# - para evitar quebrar código cliente
# - para habilitar setter
# - para executar ações ao obter o atributo
# Código cliente é o código que usa o seu código
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)

###########################################

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
