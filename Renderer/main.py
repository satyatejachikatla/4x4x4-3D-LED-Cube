import threading
import numpy as np
from blit_vol import blit_volume_loop,swap_buffer,frame_buffer

def update_frame():
	pattern = np.random.randint(0,2,frame_buffer.shape)
	swap_buffer(pattern)
	sleep(1)

 
if __name__ == "__main__":
	# creating thread for voxel update from framebuffer
	t_blit_volume_loop = threading.Thread(target=blit_volume_loop)

	while True:
		update_frame()

	t_blit_volume_loop.join()