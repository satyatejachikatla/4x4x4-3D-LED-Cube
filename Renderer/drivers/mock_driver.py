import numpy as np
import os
from time import sleep
from .utils.driver_common import index_to_pin_out
import math

GRID_SHAPE            = (4,4,4)
TOTAL_OUT_PINS        = GRID_SHAPE[0]*GRID_SHAPE[1]

DECODER_IN_BITS       = 3
DECODER_OUT_BITS      = 2**DECODER_IN_BITS
DECODER_OUT_BITS_MASK = 2**DECODER_OUT_BITS - 1
TOTAL_DECODERS        = math.ceil(TOTAL_OUT_PINS/DECODER_OUT_BITS)

BLIT_VOL_FILE_NAME    = './BLIT_VOL_FILE'

decoder_details = {
	'TOTAL_DECODERS' : TOTAL_DECODERS,
	'DECODER_OUT_BITS_MASK' : DECODER_OUT_BITS_MASK,
	'DECODER_OUT_BITS' : DECODER_OUT_BITS
}

BLIT_VOL_FILE = None
MOCK_VOXELS   = None

def blit_voxels():
	global BLIT_VOL_FILE,MOCK_VOXELS
	h,w,d = MOCK_VOXELS.shape

	for i in range(h):
		for j in range(w):
			for k in range(d):
				set_voxel_brightness((i,j,k),MOCK_VOXELS[i][j][k])

def swap_frame_buffer(new_buffer):
	global BLIT_VOL_FILE,MOCK_VOXELS
	MOCK_VOXELS , new_buffer = new_buffer , MOCK_VOXELS

def init_voxels():
	global BLIT_VOL_FILE,MOCK_VOXELS

	BLIT_VOL_FILE = open(BLIT_VOL_FILE_NAME,'w')
	MOCK_VOXELS   = np.zeros(GRID_SHAPE)

def set_voxel_brightness(voxel_index,brightness):
	global BLIT_VOL_FILE,MOCK_VOXELS

	MOCK_VOXELS[voxel_index] = brightness

	voxel_details = {
		'grid_shape' : GRID_SHAPE,
		'brightness' : brightness,
		'voxel_index': voxel_index 
	}

	decoder_input , select_decoder = index_to_pin_out(voxel_details,decoder_details)
	pin_out = ('{:0'+str(DECODER_IN_BITS)+'b}' + ' {:0'+str(TOTAL_DECODERS)+'b}').format(decoder_input,select_decoder)

	# Prints to Debug
	BLIT_VOL_FILE.seek(0)
	BLIT_VOL_FILE.write('Expected LED\n')
	BLIT_VOL_FILE.write('{}\n'.format(MOCK_VOXELS))
	BLIT_VOL_FILE.write('Index-Pin out\n')
	BLIT_VOL_FILE.write('Brightness:{} Voxel Index:{} Pin_out:{}\n'.format(brightness,voxel_index,pin_out))

def cleanup_voxels():
	global BLIT_VOL_FILE
	BLIT_VOL_FILE.close()
	os.remove(BLIT_VOL_FILE_NAME)

class mock_driver():
	def __init__(self):
		self.GRID_SHAPE = GRID_SHAPE
		self.swap_frame_buffer = swap_frame_buffer

		self.init_voxels = init_voxels
		self.blit_voxels = blit_voxels
		self.cleanup_voxels = cleanup_voxels

