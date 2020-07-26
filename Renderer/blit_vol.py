import numpy as np
import RPi.GPIO as GPIO
import time

# These are the pin numbers written on the board.
led_pins = np.array([[[37,35], [33,31]] , [[29,32] , [23,21]]])

frame_buffer = np.zeros(led_pins.shape)

def init_voxels():
	global led_pins

	GPIO.setmode(GPIO.BOARD)

	for pin in led_pins.flatten():
			GPIO.setup(pin, GPIO.OUT)
			#Set Led Off Initially
			GPIO.output(pin, GPIO.LOW)

def cleanup_voxels():
	GPIO.cleanup()

def blit_volume():
	global frame_buffer,led_pins

	h,w,d = frame_buffer.shape

	for i in range(h):
		for j in range(w):
			for k in range(d):
				if frame_buffer[i][j][k] <= 0:
					GPIO.output(led_pins[i][j][k], GPIO.LOW)
				else:
					GPIO.output(led_pins[i][j][k], GPIO.HIGH)
						
def blit_volume_loop():
	global frame_buffer,led_pins
	init_voxels()

	h,w,d = frame_buffer.shape

	try:
		while True:
			for i in range(h):
				for j in range(w):
					for k in range(d):
						if frame_buffer[i][j][k] <= 0:
							GPIO.output(led_pins[i][j][k], GPIO.LOW)
						else:
							GPIO.output(led_pins[i][j][k], GPIO.HIGH)
						
	except KeyboardInterrupt:
		pass
	finally:
		cleanup_voxels()

def swap_buffer(new_buffer):
	global frame_buffer

	new_buffer , frame_buffer = frame_buffer , new_buffer

	return new_buffer