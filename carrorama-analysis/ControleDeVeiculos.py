from Veiculo import Veiculo
from Despesa import Despesa
from Manutencao import Manutencao
from Combustivel import Combustiveis
from TipoDeDespesa import TipoDeDespesa
from DescricaoEmBrancoException import DescricaoEmBrancoException
from ValorInvalidoException import ValorInvalidoException
from Abastecimento import Abastecimento
import time

import mysql.connector.locales.eng.client_error
import mysql.connector


class ControleDeVeiculos:

    def __init__(self, veiculos=[]):
        self.veiculos = veiculos
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Samuel09",

            db="carrorama")
        self.mycursor = self.mydb.cursor()

    def __del__(self):
        self.mycursor.close()
        self.mydb.close()

    # -------------Registra veiculos----------------------------------------
    def registra_veiculo(self): # objeto do tipo Veiculo
        sqlVeiculo = "INSERT INTO veiculo(modelo,marca,cor,placa,renavam,motor,ano)VALUES(%s, %s, %s, %s, %s, %s, %s)"
        sqlComb = "INSERT INTO combustiveis(combustivel,Veiculo_idVeiculo) VALUES(%s, %s)"

        while True:
            try:
                veiculo = Veiculo()
                print(len(veiculo.combustiveis))
                print(veiculo.marca)
                veiculo.marca = input("Digite a marca do veículo: ")
                veiculo.modelo = input("Digite o modelo: ")
                veiculo.cor = input("Qual a cor do veículo? ")
                veiculo.motor = input("qual o motor do Veiculo?\n EX: 1.0, 2.0\n")

                valor = int(input("qual seu tipo de carro?\n(1) para comum\n(2) para FLEX\n"))
                if valor == 1:
                    valor = int(input("escolha o tipo de combustivel de seu carro\n(1) para "+ Combustiveis.Gasolina.name +
                                      "\n(2) para " + Combustiveis.Alccol.name + "\n(3) para "+ Combustiveis.Diesel.name+"\n"))
                    veiculo.combustiveis = valor
                elif valor == 2:

                    combs = int(input("Escolha o primeiro tipo de combustivel de seu carro\n(1) para "+ Combustiveis.Gasolina.name +
                                        "\n(2) para " + Combustiveis.Alccol.name + "\n(3) para "+ Combustiveis.Diesel.name + "\n"))
                    veiculo.combustiveis = combs

                    combs = int(input(
                        "Escolha o segundo tipo de combustivel de seu carro\n(1) para " + Combustiveis.Gasolina.name +
                        "\n(2) para " + Combustiveis.Alccol.name + "\n(3) para " + Combustiveis.Diesel.name +"\n"))
                    veiculo.combustiveis = combs

                    for combustivel in veiculo.combustiveis:
                        print(combustivel.value)

                veiculo.ano = input("Digite o ano de fabricação do veículo: ")
                veiculo.renavam = input("Digite o renavam do veiculo seguindo o seguinte modelo.\nEX: 1234.123456-9\n")
                veiculo.placa = input("Digite a placa no deguinte modelo.\n EX: JKD-1987")
                break
            except(DescricaoEmBrancoException, ValorInvalidoException):
                print("Um dos campos foi preenchido incorretamente, refaça o cadastro")

        insertveiculo = (veiculo.modelo, veiculo.marca, veiculo.cor, veiculo.placa, veiculo.renavam,veiculo.motor, veiculo.ano)

        self.mycursor.execute(sqlVeiculo, insertveiculo)
        veiculo_id = self.mycursor.lastrowid

        for combustivel in veiculo.combustiveis:
            insertcombustivel = (combustivel.value, veiculo_id)
            self.mycursor.execute(sqlComb, insertcombustivel)

        self.veiculos.append(veiculo)

        print("sucesso\ninformações do veiculo registrado. ")
        print(veiculo, "\n")

        self.mydb.commit()

# ----------------Registrar despesas-------------------------------------
    def registra_despesa(self):

        """if len(self.veiculos) == 0:
            print("Não há carros cadastrados para se vincular uma despesa a ele, por favor cadastre um carro primeiro.\n"
                  "voltando ao menu principal\n")
            time.sleep(3)
            return

        print("Escolha o carro para o qual deseja adicionar a despesa\n")
        for i, carro in enumerate(self.veiculos):
            print(str(i+1), end=" - ")
            print(carro)
        carro_escolhido = int(input()) - 1

        if carro_escolhido > len(self.veiculos):
            raise ValorInvalidoException("Indice")"""

        veiculos_id = []
        sql_despesa = "INSERT INTO despesa(categoria, valor, DATA, veiculo_idVeiculo) VALUES(%s, %s, %s, %s)"

        req = "SELECT idVeiculo, modelo, marca, placa FROM veiculo"

        while 1:
            self.mycursor.execute(req)
            for (idVeiculo, modelo, marca, placa) in self.mycursor:
                veiculos_id.append(idVeiculo)
                print("{})\t{} - {} - {}".format(idVeiculo, marca, modelo, placa))
            carro_escolhido = int(input("\nSelecione o numero indicado do carro em que deseja cadastrar a despesa: "))

            if self.bin_search(veiculos_id, carro_escolhido) == len(veiculos_id) or self.bin_search(veiculos_id, carro_escolhido) == -1:
                print("Numero invalido. Por favor escolha um dos numeros impressos.\n")
                time.sleep(2)
            elif veiculos_id[self.bin_search(veiculos_id, carro_escolhido)] != carro_escolhido:
                print("Numero invalido. Por favor escolha um dos numeros impressos.\n")
                time.sleep(2)
            else:
                break

        while True:  # ---------cadastra uma despesa comum------------------
            try:

                categoria = int(input("digite o numero dacategoria de despesa que deseja adicionar\n(1) Imposto\n(2) Seguro\n(3) Manutenção\n"
                                      "(4) Financiamento\n(5) Multas\n(6) Abastecimento\n"))
                if categoria < 1 or categoria > 6:
                    raise ValorInvalidoException("categoria")

                valor_despesa = input("digite o valor da despesa: ")
                if valor_despesa == '':
                    raise DescricaoEmBrancoException("valor da despesa")
                elif float(valor_despesa) < 0:
                    raise ValorInvalidoException("valor da despesa")

                if categoria == 6:  # ----------------Despesa de abastecimento-----------------------

                    sql_abastecimento = "INSERT INTO abastecimento(combustiveis, quilometragem_inicial, valor_do_litro, tanque_cheio, despesa_iddespesa) " \
                                        "VALUES(%s, %s ,%s ,%s ,%s)"

                    abastecimento = Abastecimento()
                    abastecimento.categoria = 6
                    abastecimento.valor = valor_despesa

                    req = "SELECT combustivel FROM combustiveis WHERE Veiculo_idVeiculo = %s"
                    entrada_req = (carro_escolhido, )
                    self.mycursor.execute(req, entrada_req)

                    for combustivel in self.mycursor:
                        print("{})\t{}".format(combustivel[0], Combustiveis(combustivel[0]).name))

                    combustivel = int(input("Selecione o numero correspondente ao tipo de combustivel usado no abastecimento: "))
                    abastecimento.combustivel = Combustiveis(combustivel)

                    abastecimento.ValorDoLitro = input("Digite o valor do litro na hora do abastecimento: ")

                    quilometragem_inicial = input("Digite a quilometragem antes do abastecimento: ")
                    abastecimento.QuilometragemInicial = quilometragem_inicial

                    tanque = input("informe se o abastecimento foi de tanque cheio ou não\n(1)Tanque cheio\n(2)normal\n")
                    if tanque == '':
                        raise DescricaoEmBrancoException("Tanque")
                    elif int(tanque) < 1 or int(tanque) > 2:
                        raise ValorInvalidoException("Tanque")

                    tanque = int(tanque)-1
                    abastecimento.IsTanqueCheio = tanque

                    insert_despesa = (abastecimento.categoria, abastecimento.valor, abastecimento.data, carro_escolhido)
                    self.mycursor.execute(sql_despesa, insert_despesa)
                    id_despesa = self.mycursor.lastrowid

                    insert_abastecimento = (combustivel, abastecimento.QuilometragemInicial, abastecimento.ValorDoLitro, abastecimento.IsTanqueCheio, id_despesa)
                    self.mycursor.execute(sql_abastecimento, insert_abastecimento)

                    print(abastecimento)

                elif categoria == 3:  # ------------despesa de manutencao----------------

                    sql_manutencao = "INSERT INTO manutencao(quilometragem, despesa_iddespesa) VALUES (%s, %s)"
                    manutencao = Manutencao()
                    manutencao.valor = valor_despesa
                    manutencao.quilometragem = input("Digite a quilometragem antes da manutenção: ")

                    print(manutencao)

                    insert_despesa = (categoria, valor_despesa, manutencao.data, carro_escolhido)
                    self.mycursor.execute(sql_despesa, insert_despesa)
                    despesa_id = self.mycursor.lastrowid

                    insert_manutencao = (manutencao.quilometragem, despesa_id)
                    self.mycursor.execute(sql_manutencao, insert_manutencao)

                else: # ------------Registra uma despesa comum--------------------
                    despesa = Despesa()
                    despesa.categoria = TipoDeDespesa(categoria)
                    despesa.valor = valor_despesa

                    insert_despesa = (categoria, valor_despesa, despesa.data, carro_escolhido)
                    self.mycursor.execute(sql_despesa, insert_despesa)

                    print(despesa)

                self.mydb.commit()
                break

            except(DescricaoEmBrancoException, ValorInvalidoException, ValueError):
                print("Algum dos campos foi digitado erroneamente, por favor refaça o cadastro apertando ENTER, ou qualquer outra letra.")
                print("Caso não queira digite 'n'.")
                escolha = input()
                if escolha == 'n': break
                elif escolha == '' or escolha != 'n': pass



# ------------------------------------funções para gerar relatorios---------------------------------------------------

    def gerar_relatorio_simples(self):

        relatorio=[]
        relatorio.append("Relatório simples\n")
        for veiculo in self.veiculos:
            relatorio.append(veiculo.__str__() + "\n")
            for despesa in veiculo.despesas:
                relatorio.append('\t' + despesa.__str__() + "\n")

        return ''.join(relatorio)

    # TODO implementar relatorio de consumo
    def gerar_relatorio_consumo(self):
        pass

    # TODO implementar relatorio de custo
    def gerar_relatorio_custo(self):
        pass

# -------------------------------------------Sub-rotinas------------------------------------

    def bin_search(self, vetor, x):
        e = -1
        d = len(vetor)
        while e < (d - 1):
            m = int((e+d) / 2)
            if vetor[m] < x:
                e = m
            else:
                d = m
        return d
