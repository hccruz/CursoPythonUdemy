from time import sleep
from threading import Thread


"""class MeuThread(Thread):
    def __init__(self, texto, tempo):
        super().__init__()
        self.texto = texto
        self.tempo = tempo

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Oi', 10)
t1.start()

t1 = MeuThread('Heraldo', 15)
t1.start()

t1 = MeuThread('Cruz', 5)
t1.start()

for i in range(20):
    print(i)
    sleep(1)
"""


"""def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá, mundo 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá, mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá, mundo 3!', 3))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""


"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá, mundo 1!', 10))
t1.start()
t1.join()

# while t1.is_alive():
#     print('Esperando o thread...')
#     sleep(2)

print('Thread finalizada.')  # A thread finaliza quando o seu loop termina.
"""


class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            print(f'Foram vendidos {quantidade} ingressos. '
                  f'Ainda temos {self.estoque} ingressos disponíveis.')
        else:
            print(f'Estoque insuficiente. {self.estoque} ingressos disponíveis.')


if __name__ == '__main__':
    ingresso = Ingresso(10)

    for i in range(1, 20):
        t = Thread(target=ingresso.comprar, args=(i,))
        t.start()

    print(ingresso.estoque)
