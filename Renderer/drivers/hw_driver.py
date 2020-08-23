import numpy as np
import RPi.GPIO as GPIO
import time
import math

GRID_SHAPE   = (4,4,4)
VOXEL_BUFFER = np.zeros(GRID_SHAPE)

s1 = None
s2 = None
ls = None

class ShiftRegister():
	def __init__(self,shift_pin,latch_pin,data_pin):
		self.shift_pin = shift_pin
		self.latch_pin = latch_pin
		self.data_pin  = data_pin

		GPIO.setup(self.shift_pin, GPIO.OUT)
		GPIO.setup(self.latch_pin, GPIO.OUT)
		GPIO.setup(self.data_pin, GPIO.OUT)

		GPIO.output(self.shift_pin, GPIO.LOW)
		GPIO.output(self.latch_pin, GPIO.LOW)
		GPIO.output(self.data_pin, GPIO.LOW)

	def shift_bit(self,data):
		if data > 0 :
			GPIO.output(self.data_pin, GPIO.HIGH)
		else:
			GPIO.output(self.data_pin, GPIO.LOW)
		GPIO.output(self.shift_pin, GPIO.HIGH)
		GPIO.output(self.shift_pin, GPIO.LOW)	

	def latch_output(self):
		GPIO.output(self.latch_pin, GPIO.HIGH)
		GPIO.output(self.latch_pin, GPIO.LOW)	

	def send_data_8_bit(self,data):
		count = 0 
		while count < 8:
			self.shift_bit(data&1)
			data = data >> 1
			count += 1

class LayerSelector():
	def __init__(self,layer_pins):
		self.layer_pins = layer_pins

		for pin in self.layer_pins:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, GPIO.LOW)

	def select_layer(self,layer_index):
		GPIO.output(self.layer_pins[layer_index-1], GPIO.LOW)
		GPIO.output(self.layer_pins[layer_index], GPIO.HIGH)

def init_voxels():
	global s1,s2,latch_second_request,latch_request,ls

	GPIO.setmode(GPIO.BOARD)
	s2 = ShiftRegister(15,13,7)
	s1 = ShiftRegister(22,18,16)

	ls = LayerSelector([37,35,33,31])

	latch_request = False
	latch_second_request = False

def blit_voxels():
	global VOXEL_BUFFER,s1,s2,latch_request,latch_second_request,ls
	d,h,w = VOXEL_BUFFER.shape

	for i in range(d):
		data = 0
		for j in range(h):
			for k in range(w):
				b = VOXEL_BUFFER[i,j,k]
				data = data << 1
				if b > 0:
					data |= 1
				else:
					data |= 0

		s1.send_data_8_bit((data & 0x00FF))
		s2.send_data_8_bit((data & 0xFF00) >> 8)

		ls.select_layer(i)
		s1.latch_output()
		s2.latch_output()

def swap_frame_buffer(new_buffer):
	global VOXEL_BUFFER,s1,s2,latch_request
	VOXEL_BUFFER , new_buffer = new_buffer , VOXEL_BUFFER
	latch_request = True

def cleanup_voxels():
	GPIO.cleanup()

class hw_driver():
	def __init__(self):
		self.GRID_SHAPE = GRID_SHAPE
		self.swap_frame_buffer = swap_frame_buffer

		self.init_voxels = init_voxels
		self.blit_voxels = blit_voxels
		self.cleanup_voxels = cleanup_voxels
