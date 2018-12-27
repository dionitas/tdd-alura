import sys


class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def propoe(self, lance: Lance):
        if self.__lances:
            stateLance = not self.__lances
            print('{} : {} - lances: {}'.format(self.__lances[-1].usuario.nome,lance.usuario.nome, stateLance))

        if not self.__lances or self.__lances[-1].usuario.nome != lance.usuario.nome and lance.valor > self.__lances[-1].valor:

            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError("O mesmo usuario nao pode propor dois lances seguidos")

    @property
    def lances(self):
        return self.__lances[:]