from Veiculo import Veiculo
from Despesa import Despesa
from Combustivel import Combustiveis
from TipoDeDespesa import TipoDeDespesa
from DescricaoEmBrancoException import DescricaoEmBrancoException
from ValorInvalidoException import ValorInvalidoException



class ControleDeVeiculos:

    def __init__(self, veiculos=[]):
        self.veiculos = veiculos

    def RegistraVeiculo(self): #objeto do tipo Veiculo
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
                veiculo.combustiveis = [Combustiveis(valor), None]
            elif valor == 2:
                flex=[]
                combs = int(input("escolha o primeiro tipo de combustivel de seu carro\n(1) para "+ Combustiveis.Gasolina.name +
                                    "\n(2) para" + Combustiveis.Alccol.name + "\n(3) para"+ Combustiveis.Diesel.name))
                flex.append(combs)
                combs = int(input(
                    "escolha o primeiro tipo de combustivel de seu carro\n(1) para " + Combustiveis.Gasolina.name +
                    "\n(2) para" + Combustiveis.Alccol.name + "\n(3) para" + Combustiveis.Diesel.name))
                flex.append(combs)
                flex[0] = Combustiveis(flex[0])
                flex[1] = Combustiveis(flex[1])
                veiculo.combustiveis = flex

            veiculo.ano = input("Digite o ano de fabricação do veículo: ")
            veiculo.renavam = input("Digite o renavam do veiculo seguindo o seguinte modelo.\nEX: 1234.123456-9\n")
            veiculo.placa = input("Digite a placa no deguinte modelo.\n EX: JKD-1987")
        except(DescricaoEmBrancoException or ValorInvalidoException) as e:
            raise e

        self.veiculos.append(veiculo)
        print("sucesso\ninformações do veiculo registrado: ")
        print(veiculo)

    def RegistrarDespesa(self):
        print("Escolha o carro para o qual deseja adicionar a despesa")
        for i, carro in enumerate(self.veiculos):
            print(str(i+1) + carro)
        valor = int(input()) - 1


    def GerarRelatorioSimples(self):
        relatorio = []
        relatorio.append("Relatório simples\n")
        for veiculo in self.veiculos:
            relatorio.append(veiculo.__str__()+ "\n")

            for despesa in veiculo.despesas:
                relatorio.append('\t' +despesa.nome + "\tvalor: " + str(despesa.valor) + " R$" + despesa.data + "\n")

        return ''.join(relatorio)

#implementar os outros tipos de relatorios
"""
#codigo de testes
controle = ControleDeVeiculos()
carro = Veiculo()
despesa = Despesa()
carro.marca = "FIAT"
carro.modelo = "UNO"
carro.placa = "JKD-1998"
carro.ano = 2018
carro.cor = "Azul"
carro2 = Veiculo()
carro2.marca = "FIAT"
carro2.modelo = "UNO"
carro2.placa = "JKD-1998"
carro2.ano = 2018
carro2.cor = "Azul"

despesa.nome = "Abastecimento na Shell"
despesa.valor = 34.5
despesa.data = "12/03/2019"

controle.RegistraVeiculo(carro)
controle.RegistraVeiculo(carro2)

controle.RegistrarDespesa(carro, despesa)
controle.RegistrarDespesa(carro, despesa)
controle.RegistrarDespesa(carro, despesa)
controle.RegistrarDespesa(carro2, despesa)


print(controle.GerarRelatorioSimples())
"""