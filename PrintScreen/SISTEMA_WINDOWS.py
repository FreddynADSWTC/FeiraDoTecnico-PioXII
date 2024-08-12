import pyautogui
import time

ScreensFPS = 0
ATLTime = time.localtime()

i = 1
while i < 2: 
    screenshot = pyautogui.screenshot()
    screenshot.save(rf'{ScreensFPS}-{ATLTime}.png')
    ScreensFPS += 1
    print(ScreensFPS) 
    time.sleep(10)
