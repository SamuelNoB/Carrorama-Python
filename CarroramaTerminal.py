from ValorInvalidoException import ValorInvalidoException
from Veiculo import Veiculo
import ControleDeVeiculos as CV
import time
import os

controle = CV.ControleDeVeiculos()

print("Bem vindo ao controle de carros via terminal.")
time.sleep(1.5)


while 1:
    escolha = int(input("Digite o numero da opção que deseja acessar\n1) Cadastrar veiculo\n2) Cadastrar despesa\n3) Gerar relatorios\n4) Sair\n"))
    if escolha == 1: controle.registra_veiculo()
    elif escolha== 2: controle.registra_despesa()
    elif escolha == 3:
        while True:
            tipo_relatorio = int(input("Digite o numero da opçao que deseja acessar\n1) Gerar relatorio simples\n"
                                       "2) Gerar relatorio de consumo\n3) Gerar relatorio de custo\n4) Voltar"))

            if tipo_relatorio < 4 and tipo_relatorio > 0:
                if tipo_relatorio == 1: print("\n" + controle.gerar_relatorio_simples())

                elif tipo_relatorio ==2: print(controle.gerar_relatorio_consumo())

                elif tipo_relatorio == 3: print(controle.gerar_relatorio_custo())

                elif tipo_relatorio == 4: pass

                break
            else:
                input("Por favor escolha uma opção válida\n")

    elif escolha == 4: break
    else:
       input("Por favor escolha uma opção válida... Aperte enter para voltar ao inicio\n")
