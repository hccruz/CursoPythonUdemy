# abstractmethod para qualquer método já decorado
# É possível criar @property, @property.setter, @classmethod,
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod commo decorador mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, nome):
        self._nome = None
        self.nome = nome

    @property
    @abstractmethod
    def nome(self): ...

    @nome.setter
    @abstractmethod
    def nome(self, nome): ...


class Foo(AbstractFoo):
    def __init__(self, nome):
        super().__init__(nome)
        # print('Sou inútil')


foo = Foo('Bar')
print(foo.nome)
