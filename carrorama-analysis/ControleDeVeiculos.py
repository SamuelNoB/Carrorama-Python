from Veiculo import Veiculo
from Despesa import Despesa
from TipoDeDespesa import TipoDeDespesa



class ControleDeVeiculos:

    def __init__(self, veiculos=[]):
        self.veiculos = veiculos

    def RegistraVeiculo(self, veiculo): #objeto do tipo Veiculo
        self.veiculos.append(veiculo)
        print("sucesso")

    def RegistrarDespesa(self, veiculo, despesa):
        veiculo.despesas.append(despesa)

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