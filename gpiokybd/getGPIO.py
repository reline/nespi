#from threading import Thread
#from time import sleep
#import uinput
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)

#device = uinput.Device([uinput.KEY_Z])

#def threadedFunction(arg, kwargs):
#	while True:
#		print("running")
#		device.emit_click(uinput.KEY_Z)

while True:
	if GPIO.input(32):
		exit("32")
		#thread = Thread(target=threadedFunction, args=(uinput.KEY_Z))
		#thread.start()
		#thread.join()
		#print("thread finished")
