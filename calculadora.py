from numbers import Number

class ZeroMultiplicationError(Exception):
    pass

class Calculadora:
    def __init__(self, n1, n2):
        self.__n1 = n1
        self.__n2 = n2
    
    @property
    def n1(self):
        return self.__n1

    @property
    def n2(self):
        return self.__n2

    def somar(self):
        return self.n1 + self.n2
    def subtrair(self):
        return self.n1 - self.n2
    def multiplicar(self):
        if self.n1 == 0 or self.n2 == 0:
            raise ZeroMultiplicationError('Não é possível multiplicar por zero')
        return self.n1 * self.n2
    def dividir(self):
        return self.n1 / self.n2

if __name__ == '__main__':
    try:
        c = Calculadora(5, 10)
        print(f"Soma = {c.somar()}")
        print(f"Subtração = {c.subtrair()}")
        print(f"Multiplicação = {c.multiplicar()}")
        print(f"Divisão = {c.dividir()}")
    except AssertionError as e:
        print(e)
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    except ZeroMultiplicationError:
        print('Não é possível multiplicar por zero')
    except Exception:
        print('Erro desconhecido')