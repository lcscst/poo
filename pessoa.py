class Pessoa:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__atribuirsalario(salario)

    def __atribuirsalario
        assert type(valor) == int or type(valor) == float, "Valor a aumentar"
        assert valor > 0, "Valor a aumentar deve ser maior que zero"

    @property
    def salario(self):
        return self.__salario
    
    def aumentar_salario(self, valor):
        assert type(valor) == int or type(valor) == float, "Valor a aumentar"
        assert valor > 0, "Valor a aumentar deve ser maior que zero"
        self.__salario += valor

    @property
    def nome(self):
        self.__nome

    @nome.setter
    def nome(self,nome):
        assert type(nome) == str, "Nome deve ser uma string"
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self,idade):
        #if type(idade) != int:
         #   raise ValorInvalido("Idade deve ser um inteiro", self)
        assert type(idade) == int, "Idade deve ser um inteiro"
        assert 0 <= idade <= 100, "Idade deve ser entre 0 e 100"
        self._idade=idade

if __name__ == '__main__':
    try:
        p = Pessoa("L", 30)
        p2 = Pessoa("J", 102)
        p3 = Pessoa(31415, 22)
    except AssertionError as e:
        print(e)

