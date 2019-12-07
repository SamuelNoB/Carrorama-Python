from Veiculo import Veiculo
from Despesa import Despesa
from Manutencao import Manutencao
from Combustivel import Combustiveis
from TipoDeDespesa import TipoDeDespesa
from DescricaoEmBrancoException import DescricaoEmBrancoException
from ValorInvalidoException import ValorInvalidoException
import Abastecimento
import time


class ControleDeVeiculos:

    def __init__(self, veiculos=[]):
        self.veiculos = veiculos

    def registra_veiculo(self): # objeto do tipo Veiculo
        while True:
            try:
                veiculo = Veiculo()
                veiculo.marca = input("Digite a marca do veículo: ")
                veiculo.modelo = input("Digite o modelo: ")
                veiculo.cor = input("Qual a cor do veículo? ")
                veiculo.motor = input("qual o motor do Veiculo?\n EX: 1.0, 2.0\n")

                valor = int(input("qual seu tipo de carro?\n(1) para comum\n(2) para FLEX\n"))
                if valor == 1:
                    valor = int(input("escolha o tipo de combustivel de seu carro\n(1) para "+ Combustiveis.Gasolina.name +
                                      "\n(2) para" + Combustiveis.Alccol.name + "\n(3) para"+ Combustiveis.Diesel.name+"\n"))
                    veiculo.combustiveis = [valor-1]
                elif valor == 2:
                    flex=[]
                    combs = int(input("escolha o primeiro tipo de combustivel de seu carro\n(1) para "+ Combustiveis.Gasolina.name +
                                        "\n(2) para" + Combustiveis.Alccol.name + "\n(3) para"+ Combustiveis.Diesel.name))
                    flex.append(combs)
                    combs = int(input(
                        "escolha o primeiro tipo de combustivel de seu carro\n(1) para " + Combustiveis.Gasolina.name +
                        "\n(2) para" + Combustiveis.Alccol.name + "\n(3) para" + Combustiveis.Diesel.name))
                    flex.append(combs)
                    veiculo.combustiveis = flex

                veiculo.ano = input("Digite o ano de fabricação do veículo: ")
                veiculo.renavam = input("Digite o renavam do veiculo seguindo o seguinte modelo.\nEX: 1234.123456-9\n")
                veiculo.placa = input("Digite a placa no deguinte modelo.\n EX: JKD-1987")
                break
            except(DescricaoEmBrancoException, ValorInvalidoException):
                print("Um dos campos foi preenchido incorretamente, refaça o cadastro")

        self.veiculos.append(veiculo)
        print("sucesso\ninformações do veiculo registrado. ")
        print(veiculo)

    def registra_despesa(self):
        if enumerate(self.veiculos) == 0:
            print("Não há carros cadastrados para se vincular uma despesa a ele, por favor cadastre um carro primeiro\n"
                  "voltando ao menu principal\n")
            time.sleep(3)
            return

        print("Escolha o carro para o qual deseja adicionar a despesa\n")
        for i, carro in enumerate(self.veiculos):
            print(str(i+1), end=" - ")
            print(carro)
        carro_escolhido = int(input()) - 1

        if carro_escolhido > len(self.veiculos):
            raise ValorInvalidoException("Indice")

        while True:
            try:

                categoria = int(input("digite o numero dacategoria de despesa que deseja adicionar\n"
                                                            "(1) Imposto\n(2) Seguro\n(3) Manutenção\n(4) Financiamento\n"
                                                            "(5) Multas\n(6) Abastecimento\n"))

                valor_despesa = float(input("digite o valor da despesa: "))

                if categoria == 6:

                    abastecimento = Abastecimento.Abastecimento()
                    abastecimento.categoria = 6
                    abastecimento.valor = valor_despesa

                    if len(self.veiculos[carro_escolhido].combustiveis) == 2:
                        print("Coloque o numero do combustivel usado no abastecimento.\n(1) " +
                              self.veiculos[carro_escolhido].combustiveis[0].name + "\n(2) " + self.veiculos[carro_escolhido].combustiveis[1].name)
                        Comb_abastecido = int(input())-1

                        abastecimento.combustivel = self.veiculos[carro_escolhido].combustiveis[Comb_abastecido]
                    else:
                        abastecimento.combustivel = self.veiculos[carro_escolhido].combustiveis[0].value

                    print(abastecimento.combustivel)

                    abastecimento.ValorDoLitro = float(input("Digite o valor do litro na hora do abastecimento: "))

                    quilometragem_inicial = int(input("Digite a quilometragem antes do abastecimento: "))
                    abastecimento.QuilometragemInicial = quilometragem_inicial

                    tanque = int(input("informe se o abastecimento foi de tanque cheio ou não\n(1)Tanque cheio\n(2)normal\n"))-1

                    if tanque == 0:
                        abastecimento.IsTanqueCheio = False
                    elif tanque == 1:
                        abastecimento.IsTanqueCheio = True
                    else:
                        raise ValorInvalidoException

                    self.veiculos[carro_escolhido].despesas.append(abastecimento)
                    print(abastecimento)

                elif categoria == 3:

                    manutencao = Manutencao()
                    manutencao.valor = valor_despesa
                    manutencao.quilometragem = int(input("Digite a quilometragem antes da manutenção: "))
                    self.veiculos[carro_escolhido].despesas.append(manutencao)
                    print(manutencao)

                else:

                    despesa = Despesa()
                    despesa.categoria = TipoDeDespesa(categoria)
                    despesa.valor = valor_despesa
                    self.veiculos[carro_escolhido].despesas.append(despesa)
                    print(despesa)
                break
            except(DescricaoEmBrancoException or ValorInvalidoException):
                print("algum dos campos foi digitado erroneamente, por favor refaça o cadastro.")

    def gerar_relatorio_simples(self):
        relatorio=[]
        relatorio.append("Relatório simples\n")
        for veiculo in self.veiculos:
            relatorio.append(veiculo.__str__() + "\n")
#            print(veiculo)
            for despesa in veiculo.despesas:
                relatorio.append('\t' + despesa.__str__() + "\n")
 #               print(despesa)

        return ''.join(relatorio)

    # TODO implementar relatorio de consumo
    def gerar_relatorio_consumo(self):
        pass

    # TODO implementar relatorio de custo
    def gerar_relatorio_custo(self):
        pass
