from PIL import Image
from multiprocessing import Pool, Lock
import numpy

img = Image.open("example.jpg")

def rz():
    totalPatchCount = 20000
    imgArray = numpy.asarray(patch, dtype=numpy.float32)
    list_im_arr = [imgArray] * totalPatchCount  # A more elegant way than a for loop
    return list_im_arr

if __name__ == '__main__':  
    patch = img #....  Your code to get generate patch here
    patch = patch.resize((60,40), Image.Resampling.LANCZOS)
    patch = patch.convert('L')

    pool = Pool(2)
    imdata = [pool.apply_async(rz).get() for x in range(2)]
    pool.close()
    pool.join()