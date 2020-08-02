import numpy as np
import os

GRID_SHAPE = (2,2,2)

BLIT_VOL_FILE_NAME = './BLIT_VOL_FILE'
BLIT_VOL_FILE = None
MOCK_VOXELS   = None

def init_voxels():
	global BLIT_VOL_FILE,MOCK_VOXELS

	BLIT_VOL_FILE = open(BLIT_VOL_FILE_NAME,'w')
	MOCK_VOXELS   = np.zeros(GRID_SHAPE)


def set_voxel_brightness(voxle_index,brightness):
	global BLIT_VOL_FILE,MOCK_VOXELS

	MOCK_VOXELS[voxle_index] = brightness

	if voxle_index == (GRID_SHAPE[0]-1,GRID_SHAPE[1]-1,GRID_SHAPE[2]-1):
		BLIT_VOL_FILE.seek(0)
		BLIT_VOL_FILE.write('{}\n'.format(MOCK_VOXELS))


def cleanup_voxels():
	global BLIT_VOL_FILE
	BLIT_VOL_FILE.close()
	os.remove(BLIT_VOL_FILE_NAME)