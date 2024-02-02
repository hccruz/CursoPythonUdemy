'''
 Herança simples - Relações entre classes
 Associação - usa, Agregação - tem
 Composição - é dono de, Herança - É um

 Herança vs Composição

 Classe principal(Pessoa)
    -> super class, base class, parent class
 Classes filhos(Cliente)
    -> sub class, child class, derived class 
'''
class Pessoa:
    '''
    ...
    '''
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        '''
        ...
        '''
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    '''
    ...
    '''

class Aluno(Pessoa):
    '''
    ...
    '''
    cpf = 'cpf aluno'

c1 = Cliente('Heraldo', 'Cruz')
c1.falar_nome_classe()
a1 = Aluno('João', 'Pedro')
a1.falar_nome_classe()
print(a1.cpf)
# help(Cliente)