import threading
import ctypes
import numpy as np
import time

class voxels_screen(threading.Thread): 
	def __init__(self,driver): 
		threading.Thread.__init__(self) 
		self._blit_run = False
		self.driver    = driver

	def run(self):
		self._blit_run = True
		self.driver.init_voxels()

		while self._blit_run :
			self.driver.blit_voxels()

		self.driver.cleanup_voxels()

	def start_display(self):
		print('Starting Screen Display')
		self.start()

	def stop_display(self):
		print('Stoping Screen Display')
		self._blit_run = False
		self.join()