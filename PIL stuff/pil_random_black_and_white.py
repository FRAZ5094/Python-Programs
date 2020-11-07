import numpy as np
from PIL import Image
from random import randint
dim=(100,100)
array = np.zeros(dim, dtype=np.uint8)

# Set grey value to black or white depending on x position
for x in range(array.shape[1]):
    for y in range(array.shape[0]):
        if randint(0,1):
            array[y][x]=255
        else:
            array[y][x]=0

img = Image.fromarray(array)
img.show()
img.save('testgrey.png')