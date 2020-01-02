




"""from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size=30))


class Application(App):
    def build(self):
        return Tarefas(['fazer compras', 'buscar crianças', 'lavar louça', 'correr', 'brincar'])


from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from ControleDeVeiculos import ControleDeVeiculos

controle = ControleDeVeiculos()


class Prinpcipal(ScrollView):
    def __init__(self, veiculos, **kwargs):
        super().__init__(**kwargs)
        sair = Button(text='Sair.')
        add_carro = Button(text='Adicionar carro')
        self.ids.topo.add_widget(sair)
        self.ids.topo.add_widget(add_carro)
        if(veiculos == []):
            for carro in veiculos:
                self.ids.carros.add_widget(Button(text=carro.__str__()))


class Application(App):
    def build(self):
        return Prinpcipal(controle.veiculos, orientation='horizontal')

app = Application
app.run()
"""