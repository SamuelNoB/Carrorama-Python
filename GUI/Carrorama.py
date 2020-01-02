from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from ControleDeVeiculos import ControleDeVeiculos
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

contrle = ControleDeVeiculos()


class TelaManager(ScreenManager):
    pass


class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class Screen4(Screen):

    def reg_veiculo(self):
        registro  = contrle.registra_veiculo()


class CarroramaApp(App):
    def build(self):
        return TelaManager()

if __name__ == '__main__':
    CarroramaApp().run()