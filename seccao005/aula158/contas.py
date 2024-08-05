from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def deposito(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO R${valor:.2f})')
        return self.saldo

    def detalhes(self, msg=''):
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}, {attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        print('Não foi possível sacar o valor desejado.')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0,
                 limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= -self.limite:
            self.saldo -= valor
            self.detalhes(f'(SAQUE R${valor:.2f})')
            return self.saldo

        print('Não foi possível sacar o valor desejado.')
        print(f'Seu limite atual é R${-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO R${valor:.2f})')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}, {attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(1)
    cp1.deposito(1)
    cp1.sacar(1)
    cp1.sacar(1)

    cc1 = ContaCorrente(111, 333, 0, 100)
    cc1.sacar(101)
    cc1.deposito(1)
    cc1.sacar(1)
    cc1.sacar(2)
    cc1.sacar(6)
    cc1.deposito(10)
