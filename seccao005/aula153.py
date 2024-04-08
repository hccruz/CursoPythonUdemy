# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes noramis, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(f'{nome} está chamando {self.phone}')


call1 = CallMe('1234567890')
call1('Heraldo')
