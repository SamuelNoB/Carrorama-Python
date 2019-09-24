class DescricaoEmBrancoException(Exception):
    def __init__(self, NomeDoCampo):
        self.NomeDoCampo = NomeDoCampo

    def __str__(self):
        return "o campo" + self.NomeDoCampo + "está vázio"
