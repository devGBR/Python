
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


GUI = Builder.load_file('tela.kv')

class Meuapp(App):
    def build(self):
        return GUI
    def boxlayout(self):
            return BoxLayout()
    
    def renomearArquivo(nome):
        if exists(nome):
            print("Arquivo existe")
            remove = nome[:-4]
            substituir = remove.replace(" ", "_")
            substituir1 = substituir.replace(",", "")
            substituir2 = substituir1.replace("º", "")
            form = substituir2.replace(".", "")
            result = form.upper()
            name = result + ".pdf"
            return name

        else:
            print("Arquivo não encontrado")

Meuapp().run()