#Em teoria, tbm funciona, cria e apaga a PrintShareTWO, e faz tudo ai bonitinho, Então ta poggers, falta so ver se roda como adm

#Import pillow
import pyautogui
import time
import os

dirToRename = 'C:\PrintSHARE'
if not os.path.exists(dirToRename):
    os.mkdir(dirToRename)
    print('Feito PRINTSHARE -> C:/')
    
os.rename(dirToRename, 'C:/PRINTshareTWO')

if not os.path.exists(dirToRename):
    os.mkdir(dirToRename)

print("b" ,dirToRename)


ScreensFPS = 0
ATLTime = time.localtime()


i = 1
while i < 2: 
    
    dirt = pyautogui.screenshot()
    print("e" ,dirToRename)
    dirt.save(rf'{dirToRename}/{ScreensFPS}-{ATLTime}.png')
    
    # screenshot = pyautogui.screenshot()
    #screenshot.save(rf'{ScreensFPS}-{ATLTime}.png')
    
    ScreensFPS += 1
    print(ScreensFPS) 
    time.sleep(10)
    #Executar como adm p ver se roda isso aq (os.remove)
    os.remove('C:/PRINTshareTWO')
    os.mkdir('C:/PRINTshareTWO')
    #copia da pasta de rede configurar