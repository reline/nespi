import uinput
from time import sleep
from threading import Thread
import sys

device = uinput.Device([uinput.KEY_Z])
running = True

def threadedFunction():
	while running == True:
		device.emit_click(uinput.KEY_Z)

Thread(target=threadedFunction).start()

sleep(.4)
running = False
exit()
