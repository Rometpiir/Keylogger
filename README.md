This is for educational purpose ONLY. To run this pip install imports you need.
setup email address and password and Set file_path to a writable directory (e.g., C:\\Users\\YourName\\Documents).

Data Collection:
System Information: Gathers details like processor type, OS, machine type, hostname, and IP address.
Microphone Recording: Records audio input for a specified duration (microphone_time).
Clipboard Data: Accesses the clipboard and writes its content to a file.
Screenshot: Captures and saves the screen's image.
Keylogger: Logs keystrokes in real-time and stores them in a file.

Libraries Imported:
email.mime and smtplib: Used to send the collected data via email.
socket and platform: Used to fetch system and network details.
sounddevice and scipy.io.wavfile: For recording audio through the microphone.
win32clipboard: To access clipboard contents.
pyscreenshot: For capturing screenshots.
pynput: To monitor and log keyboard inputs.
os and time: For file handling and timing the script's actions.


!!!!Warning!!!!
Running this script without explicit permission violates ethical and legal standards. Use it responsibly, ideally in isolated environments for educational purposes only.
