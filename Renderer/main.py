import numpy as np
from time import sleep
from drivers.mock_driver import mock_driver as driver
from screen import voxels_screen

def update_frame(VS):
	pattern = np.random.randint(0,2,VS.driver.GRID_SHAPE) # Random image
	VS.driver.swap_frame_buffer(pattern)

def main():

	VS = voxels_screen(driver())
	VS.start_display()

	while True:
		try:
			update_frame(VS)
		except:
			break
	VS.stop_display()

if __name__ == '__main__':
	main()