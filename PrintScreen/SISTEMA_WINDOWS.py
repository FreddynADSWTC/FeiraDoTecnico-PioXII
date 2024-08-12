#tem que baixar o pillow tbm (pip install pillow & pip install pyautogui)
import pyautogui
import time

ScreensFPS = 0
ATLTime = time.localtime() #time.gmtime <- Puxa do centro da Terra 

#tacar time.localtime no Keylogger dps (Ignora isso)

i = 1
while i < 2: #codigo é so isso
    screenshot = pyautogui.screenshot()
    screenshot.save(rf'{ScreensFPS}-{ATLTime}.png')
    ScreensFPS += 1
    print(ScreensFPS) #so p debug
    time.sleep(10)

#Comando p fazer em .exe
#Tem que dar > cd "Diretorio\PythonTEste" p dar o pyinstaller
#pyinstaller --noconsole --onefile --icon=iconscreen.ico "C:\Users\cauar\Downloads\PythonTEste\PythonTEste\ImageGrab.py"