# Created by Delitel

import keyboard
import pyautogui
from time import sleep
import wave
import pyaudio


working = False

keyboard.add_hotkey("alt+z", lambda: hotkey_run())

def mus(): # ЗВУКОВОЙ ЭФФЕКТ
	CHUNK = 1024
	wf = wave.open("bing.wav", 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
	data = wf.readframes(CHUNK)

	while data != b'':
		stream.write(data)
		data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()

	p.terminate()


def hotkey_run():
	global working

	if working:
		print("Скрипт выключен!")
		working = False
		pyautogui.mouseUp()

	else:
		print("Скрипт включен!")
		working = True
	mus()


print("Нажмите alt+z чтобы включить скрипт!")
def main():
	global working

	while True:
		sleep(1)
		if working:
			pyautogui.mouseDown()






if __name__ == "__main__":
	main()