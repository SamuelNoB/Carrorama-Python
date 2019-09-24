from enum import Enum


class TipoDeDespesa(Enum):
    Imposto = "Imposto"
    Seguro = "Seguro"
    Manutencao = "Manutenção"
    Financiamento = "Financiamento"
    Multas = "Multas"
    Abastecimento = "Abastecimento"