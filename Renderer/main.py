import numpy as np
from time import sleep
from drivers.hw_driver import hw_driver as driver
from screen import voxels_screen
frame_delay = 1 
def clear_frame(VS):
	pattern = np.zeros(VS.driver.GRID_SHAPE)
	VS.driver.swap_frame_buffer(pattern)
def fill_frame(VS):
	pattern = np.ones(VS.driver.GRID_SHAPE)
	VS.driver.swap_frame_buffer(pattern)
def o_frame_1(VS):
	pattern = np.array(
[

[[0 , 0 , 0 , 1],
[1 , 0 , 0 , 1],
[0 , 0 , 0 , 1],
[1 , 0 , 0 , 1]]
,
[[0 , 0 , 0 , 1],
[1 , 0 , 0 , 1],
[0 , 0 , 0 , 1],
[1 , 0 , 0 , 1]]
,
[[0 , 0 , 0 , 1],
[1 , 0 , 0 , 1],
[0 , 0 , 0 , 1],
[1 , 0 , 0 , 1]]
,
[[0 , 0 , 0 , 1],
[1 , 0 , 0 , 1],
[0 , 0 , 0 , 1],
[1 , 0 , 0 , 1]]
]

)
	VS.driver.swap_frame_buffer(pattern)

def main():

	VS = voxels_screen(driver())
	VS.start_display()

	while True:
		try:
			clear_frame(VS)
			sleep(frame_delay)
			o_frame_1(VS)
			sleep(frame_delay)
			fill_frame(VS)
			sleep(frame_delay)
		except Exception as e:
			print(e)
			break
		except:
			break

	VS.stop_display()

if __name__ == '__main__':
	main()
