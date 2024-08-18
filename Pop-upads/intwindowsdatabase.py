import os
import sys
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import random

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

image1 = Image.open(resource_path("./Pop-upads/images/VirusAd1.png"))
image2 = Image.open(resource_path("./Pop-upads/images/VirusAd2.png"))
image3 = Image.open(resource_path("./Pop-upads/images/VirusAd3.png"))
image4 = Image.open(resource_path("./Pop-upads/images/VirusAd4.png"))
image5 = Image.open(resource_path("./Pop-upads/images/VirusAd5.png"))

class App(ttk.Frame):
    def __init__(self, master=None, image=None):
        super().__init__(master)
        master.title("ADS")
        self.image = image
        self.label = ttk.Label(master, image=self.image)
        self.label.place(x=0, y=0)


def show_popup():
    AdsPTime = random.randint(2, 5)
    root = Tk()  
    root.geometry("350x250")
    root.overrideredirect(False)
    root.iconbitmap('')  
    root.attributes('-topmost', True)  
    root.after(random.randint(AdsPTime*1000, AdsPTime*2000), root.destroy)
    root.overrideredirect(True)
    root.geometry("350x250")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = random.randint(0, screen_width - 350)
    y = random.randint(0, screen_height - 250)
    root.geometry(f"350x250+{x}+{y}")

    
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


i = 1
while i < 2:
    AdsPTime = random.randint(2, 5)

   
    print(AdsPTime)
    show_popup()
    time.sleep(AdsPTime)
    print(AdsPTime/2)
    show_popup()
    time.sleep(AdsPTime/2)
