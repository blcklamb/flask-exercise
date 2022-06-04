import numpy as np
from multiprocessing import shared_memory
# Attach to the existing shared memory block
existing_shm = shared_memory.SharedMemory(name='psm_a285934d')
# Note that a.shape is (6,) and a.dtype is np.int64 in this example
c = np.ndarray((6,), dtype=np.int64, buffer=existing_shm.buf)
print(c) # array([1, 1, 2, 3, 5, 8])
c[-1] = 888
print(c) # array([  1,   1,   2,   3,   5, 888])


# Clean up from within the second Python shell
del c  # Unnecessary; merely emphasizing the array is no longer used
existing_shm.close()