import pyautogui
import random
import time
import keyboard


screenWidth, screenHeight = pyautogui.size()

i = 2
while i > 0:   
   print('i:', i)
   if i == 2:
      print('ATIVO')
   elif i != 2:
      print("i != 2:", i)

   while i == 2:
   #RX Eixo X
   #RY Eixo Y
    RX = random.randint(0, screenWidth)
    RY = random.randint(0, screenHeight)

   
    keyboardpressKey = random.randint(0, 3)
    print('Infected or not:', keyboardpressKey)
    if keyboardpressKey == 3:
       print('Keyboard is active')
       pyautogui.write('INFECTED!', interval=0.05)
    pyautogui.moveTo(RX, RY)
    print('i:', i)
   
    
    if keyboard.is_pressed('esc'):
     print('Parando o código')
     i = 3

    time.sleep(0.5)
    

   if i == 3:
      pyautogui.moveTo(0, 0)
      print('Desligando...')
      time.sleep(3)
      print('Aguardando o comando para reiniciar: "esc"')
      keyboard.wait('esc')
      i = 2