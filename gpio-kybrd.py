import uinput
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)
GPIO.setup(36, GPIO.IN)



device = uinput.Device([uinput.KEY_U, uinput.KEY_F])

device.emit_click(uinput.KEY_Z)

up = False
down = False
left = False
right = False
b = False
a = False
select = False
start = False

while True:
	if GPIO.input(32):
		device.emit_click(uinput.KEY_F)
	if GPIO.input(36):
		device.emit_click(uinput.KEY_U)
