from abc import ABC, abstractmethod
from typing_extensions import Self

class Veiculo(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

    @abstractmethod
    def obter_tipo_combustivel(self):
        return 'Gasolina'

class carro(Veiculo):
    def acelerar(self):
        return 'Vrum'

    def frear(self):
        return 'Freando'
    
    def obter_tipo_combustivel(self):
        return super().obter_tipo_combustivel()

class bicicleta(Veiculo):
    def acelerar(self):
        return 'Pedalando'

    def frear(self):
        return 'Freando'
    
    def obter_tipo_combustivel(self):
        return "Pedal"

if __name__ == '__main__':
    c = Carro('Fuscão Preto')
    b = Bicicleta('Kaloi')
    for v in [c, b]:
        print 