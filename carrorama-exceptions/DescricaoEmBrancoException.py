class DescricaoEmBrancoException(Exception):
    def __init__(self, NomeDoCampo):
        self.NomeDoCampo = NomeDoCampo

    def toString(self):
        return "o campo" + self.NomeDoCampo + "está vázio"
