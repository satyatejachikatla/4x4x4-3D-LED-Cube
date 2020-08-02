import numpy as np
from time import sleep

from screen import voxels_screen,GRID_SHAPE

def update_frame(VS):
	pattern = np.random.randint(0,2,GRID_SHAPE) # Random image
	VS.swap_frame_buffer(pattern)

def main():

	VS = voxels_screen()
	VS.start_display()

	while True:
		try:
			update_frame(VS)
		except:
			break
	VS.stop_display()

if __name__ == '__main__':
	main()