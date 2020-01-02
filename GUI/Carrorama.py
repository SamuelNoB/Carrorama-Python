from kivy.app import App
from ControleDeVeiculos import ControleDeVeiculos

contrle = ControleDeVeiculos()


class CarroramaApp(App):

    def cadastra_veiculo_trigger(self):
        contrle.registra_veiculo()


class Teste(App):
    pass

if __name__ == '__main__':
    CarroramaApp().run()