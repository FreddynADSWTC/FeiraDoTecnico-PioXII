import os
import sys
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import random

#Funciona TOOMMMMMAAAAAA, o EXE funcionou na fé em Deus ---->>>>
# pyinstaller --noconsole --onefile --icon=iconscreen.ico "C:\Users\cauar\OneDrive\Área de Trabalho\VirusFeiraDoTecnico\Pop-upads\intwindowsdatabase.py"
#Se der erro tem q mexer no .spec e add a /images como data e depois recompilar
#Tem como fechar o virus no ALT+F4, mas ele sempre volta
#Slk programação mt pog

# Função para determinar o caminho correto, mesmo quando empacotado
def resource_path(relative_path):
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho nela
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Carregando as imagens de forma universal
image1 = Image.open(resource_path("images/VirusAd1.png"))
image2 = Image.open(resource_path("images/VirusAd2.png"))
image3 = Image.open(resource_path("images/VirusAd3.png"))
image4 = Image.open(resource_path("images/VirusAd4.png"))
image5 = Image.open(resource_path("images/VirusAd5.png"))

# Faz a janela poggers
class App(ttk.Frame):
    def __init__(self, master=None, image=None):
        super().__init__(master)
        master.title("ADS")
        self.image = image
        self.label = ttk.Label(master, image=self.image)
        self.label.place(x=0, y=0)

# X e Y pra randomizar o lugar da tela, facil, np
def show_popup():
    AdsPTime = random.randint(2, 5)
    root = Tk()  # Nao pode usar TopLevel pq se n n vai, tem q ser root.Tk()
    root.geometry("350x250")
    root.overrideredirect(False)
    root.iconbitmap('')  # so p tirar aquela pena feia de icone (nao tirou)
    root.attributes('-topmost', True)  # nao deixa sair dela
    root.after(random.randint(AdsPTime*1000, AdsPTime*2000), root.destroy)
    root.overrideredirect(True)
    root.geometry("350x250")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = random.randint(0, screen_width - 350)
    y = random.randint(0, screen_height - 250)
    root.geometry(f"350x250+{x}+{y}")

    # Aleatoriza a imagem, UAUUUUU PROGRAMACAOOOO
    ImageToShow = random.randint(1, 5)
    if ImageToShow == 1:
        image = ImageTk.PhotoImage(image1)
    elif ImageToShow == 2:
        image = ImageTk.PhotoImage(image2)
    elif ImageToShow == 3:
        image = ImageTk.PhotoImage(image3)
    elif ImageToShow == 4:
        image = ImageTk.PhotoImage(image4)
    elif ImageToShow == 5:
        image = ImageTk.PhotoImage(image5)
    print(ImageToShow)

    app = App(master=root, image=image)
    root.mainloop()

# loopzin de cria, tem 4 pop-ups (tinha, consegui otimizar e diminuir p 1)
i = 1
while i < 2:
    AdsPTime = random.randint(2, 5)

    # verifica o time.sleep e printa o showpop1 \/
    print(AdsPTime)
    show_popup()
    time.sleep(AdsPTime)
    print(AdsPTime/2)
    show_popup()
    time.sleep(AdsPTime/2)
