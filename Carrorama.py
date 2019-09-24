"""import sys

sys.path.insert(0, "./Combustivel")
sys.path.insert(1, "./Veiculo")
from Combustivel import Combustiveis
from Veiculo import Veiculo

carro = Veiculo()

carro.marca = "FIAT"
carro.modelo = "uno"
carro.combustiveis = Combustiveis.Gasolina
carro.motor = 2.0
carro.placa = "JFD-1982"
carro.ano = 1999
carro.cor = "Azul"

print(carro.ano)
print(carro.combustiveis[0])"""

from Veiculo import Veiculo
from Combustivel import Combustiveis
carro = Veiculo()

carro.combustiveis = (Combustiveis.Gasolina, Combustiveis.Diesel)
print(carro.combustiveis)
