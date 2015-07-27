import uinput
import time
import RPi.GPIO as GPIO
#import evdev

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)

device = uinput.Device([uinput.KEY_H, uinput.KEY_E, uinput.KEY_L, uinput.KEY_O, uinput.KEY_Z])

#ui = evdev.uinput.UInput()
#e = evdev.ecodes
while True:
	device.emit_click(uinput.KEY_Z)
	if GPIO.input(32):
		print("\nalive")
		device.emit_click(uinput.KEY_Z)
		device.emit_click(uinput.KEY_Z)
		device.emit_click(uinput.KEY_Z)
		device.emit_click(uinput.KEY_Z)
		device.emit_click(uinput.KEY_Z)
		device.emit_click(uinput.KEY_Z)
		
		break
		#ui.write(e.EV_KEY, e.KEY_Z, 1) # key Z - down
		#ui.write(e.EV_KEY, e.KEY_Z, 0) # key Z - up
print("break")
