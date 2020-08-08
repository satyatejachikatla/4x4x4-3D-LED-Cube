import numpy as np
import RPi.GPIO as GPIO
import time
from .utils.driver_common import index_to_pin_out
import math

# These are the pin numbers written on the board.


LED_PINS        = [40,38,36,26,24,22]
LED_PINS_SELECT = {
				0b00 : { 0 : [40,38,36,26,24,22] , 1 : [] },
				0b10 : { 0 : [26,24,22]          , 1 : [40,38,36] },
				0b01 : { 0 : [40,38,36]          , 1 : [26,24,22] },
			}

GRID_SHAPE            = (2,2,2)
TOTAL_OUT_PINS        = GRID_SHAPE[0]*GRID_SHAPE[1]

DECODER_IN_BITS       = 3
DECODER_OUT_BITS      = 2**DECODER_IN_BITS
DECODER_OUT_BITS_MASK = 2**DECODER_OUT_BITS - 1
TOTAL_DECODERS        = math.ceil(TOTAL_OUT_PINS/DECODER_OUT_BITS)

decoder_details = {
	'TOTAL_DECODERS' : TOTAL_DECODERS,
	'DECODER_OUT_BITS_MASK' : DECODER_OUT_BITS_MASK,
	'DECODER_OUT_BITS' : DECODER_OUT_BITS
}

temp_voxel_details = {
		'grid_shape' : GRID_SHAPE,
		'brightness' : 0,
		'voxel_index': (0,0,0) 
}

def init_voxels():

	GPIO.setmode(GPIO.BOARD)

	for pin in LED_PINS:
			GPIO.setup(pin, GPIO.OUT)
			#Set Led Off Initially
			GPIO.output(pin, GPIO.LOW)

def pins_low(pins):
	for pin in pins:
		GPIO.output(pin , GPIO.LOW)

def pins_high(pins):
	for pin in pins:
		GPIO.output(pin , GPIO.HIGH)

def pins_low_high(pins,low_high):
	for i in range(len(pins)):
		if low_high[i]:
			GPIO.output(pin[i] , GPIO.HIGH)
		else
			GPIO.output(pin[i] , GPIO.LOW)

def set_voxel_brightness(voxel_index,brightness):

	temp_voxel_details['voxel_index'] = voxel_index
	temp_voxel_details['brightness']  = brightness	

	decoder_input , select_decoder = index_to_pin_out(temp_voxel_details,decoder_details)

	pins_low(LED_PINS_SELECT[select_decoder][0])

	low_high = [ bit == '1' for bit in ('{:0'+str(DECODER_IN_BITS)+'b}').format(decoder_input) ]

	pins_low_high(LED_PINS_SELECT[select_decoder][1],low_high)


def cleanup_voxels():
	GPIO.cleanup()