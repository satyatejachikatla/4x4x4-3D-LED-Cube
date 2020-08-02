import threading
import ctypes
import numpy as np
import time
from mock_driver import init_voxels,cleanup_voxels,set_voxel_brightness,GRID_SHAPE

class voxels_screen(threading.Thread): 
	def __init__(self): 
		threading.Thread.__init__(self) 
		self.frame_buffer = np.zeros(GRID_SHAPE)

		self._blit_run = False

	def run(self):
		self._blit_run = True
		init_voxels()

		while self._blit_run :
			self.blit_volume()

		cleanup_voxels()

	def start_display(self):
		self.start()

	def stop_display(self):
		self._blit_run = False
		self.join()


	def blit_volume(self):

		h,w,d = self.frame_buffer.shape

		for i in range(h):
			for j in range(w):
				for k in range(d):
					set_voxel_brightness((i,j,k),self.frame_buffer[i][j][k])

	def update_frame_buffer(self,new_buffer):

		h,w,d = self.frame_buffer.shape

		for i in range(h):
			for j in range(w):
				for k in range(d):
						self.frame_buffer[i,j,k] = new_buffer[i,j,k]

	def swap_frame_buffer(self,new_buffer):

		self.frame_buffer , new_buffer = new_buffer , self.frame_buffer