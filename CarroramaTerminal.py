from ValorInvalidoException import ValorInvalidoException
from Veiculo import Veiculo
import ControleDeVeiculos as CV
import time
import os

# TODO criar um banco de dados
"""
carro = Veiculo()
carro.marca = "FIAT"
carro.modelo = "UNO"
carro.placa = "JKD-1998"
carro.ano = 2018
carro.cor = "Azul"
carro.renavam = "2586.870488-7"
carro.motor = 1.0
carro.combustiveis = [1,2]
carro2 = Veiculo()
carro2.marca = "chevrolet"
carro2.modelo = "cobalt"
carro2.placa = "JKD-1923"
carro2.ano = 2014
carro2.cor = "prata"
carro2.renavam = "4914.315127-7"
carro2.motor = 2.0
carro2.combustiveis = [1]
"""
controle = CV.ControleDeVeiculos()

print("Bem vindo ao controle de carros via terminal.")
time.sleep(1.5)


while 1:
    escolha = int(input("Digite o numero da opção que deseja acessar\n1) Cadastrar veiculo\n2) Cadastrar despesa\n3) Gerar relatorios\n4) Sair\n"))
    if escolha == 1: controle.registra_veiculo()
    elif escolha== 2: controle.registra_despesa()
    elif escolha == 3:
        tipo_relatorio = int(input("Digite o numero da opçao que deseja acessar\n1) Gerar relatorio simples\n"
                                 "2) Gerar relatorio de consumo\n3) Gerar relatorio de custo"))
        if tipo_relatorio == 1: print("\n" + controle.gerar_relatorio_simples())
        elif tipo_relatorio ==2: print(controle.gerar_relatorio_consumo())
        elif tipo_relatorio == 3: print(controle.gerar_relatorio_consumo())
        else:
            input("Por favor escolha uma opção válida\n digite qualquer tecla para voltar ao inicio\n")
    elif escolha == 4: break
    else:
       input("Por favor escolha uma opção válida... Aperte enter para voltar ao inicio\n")

