import uinput
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)

device = uinput.Device([uinput.KEY_Z])
device.emit_click(uinput.KEY_Z)

while True:
	if GPIO.input(32):
		print("hello world")
		device.emit_click(uinput.KEY_Z)
