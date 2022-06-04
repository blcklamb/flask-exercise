import numpy as np
a = np.array([1, 1, 2, 3, 5, 8])  # Start with an existing NumPy array

from multiprocessing import shared_memory

shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
# Now create a NumPy array backed by shared memory
b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
b[:] = a[:]  # Copy the original data into shared memory
print(b) 
print(type(b))
print(type(a))
print(shm.name)


# Back in the first Python interactive shell, b reflects this change
print(b) # array([  1,   1,   2,   3,   5, 888])

# Clean up from within the first Python shell
del b  # Unnecessary; merely emphasizing the array is no longer used
shm.close()
shm.unlink()