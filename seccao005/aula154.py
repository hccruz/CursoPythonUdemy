# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interno(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interno


@Multiplicar(10)
def soma(x, y):
    return x + y


resultado = soma(2, 4)
print(resultado)
