from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Gato(Animal):
    def emitir_som(self):
        return 'Miau'

class Cachorro(Animal):
    def emitir_som(self):
        return 'Au au'

class Passaro(Animal):
    def emitir_som(self):
        return 'Prrrrfp'

animais = [Gato(), Cachorro(), Passaro()]
for animal in animais:
    print(animal.emitir_som())