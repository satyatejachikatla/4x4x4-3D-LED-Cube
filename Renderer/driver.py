import numpy as np
import RPi.GPIO as GPIO
import time

# These are the pin numbers written on the board.
LED_PINS = np.array([[[37,35], [33,31]] , [[29,32] , [23,21]]])
GRID_SHAPE = LED_PINS.shape

def init_voxels():
	global LED_PINS

	GPIO.setmode(GPIO.BOARD)

	for pin in LED_PINS.flatten():
			GPIO.setup(pin, GPIO.OUT)
			#Set Led Off Initially
			GPIO.output(pin, GPIO.LOW)

def set_voxel_brightness(voxle_index,brightness):
	global LED_PINS

	if brightness <= 0:
		GPIO.output(LED_PINS[voxle_index] , GPIO.LOW)
	else:
		GPIO.output(LED_PINS[voxle_index] , GPIO.HIGH)


def cleanup_voxels():
	GPIO.cleanup()