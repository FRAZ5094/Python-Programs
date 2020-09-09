import cv2
import numpy as np
import os
from time import perf_counter

# Playing video from file:
cap = cv2.VideoCapture('《家有儿女》第一季第1集 Home With Kids Season 1 EP. 1 【超清1080P无删减版】.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

fps = cap.get(cv2.CAP_PROP_FPS)
currentFrame = 0

start=perf_counter()
while currentFrame<1000:
    ret, frame = cap.read()
    if currentFrame%10==0:
        frame=frame[-75:-30,:]
        name = './data/' + str(currentFrame) + '.jpg'
        #print('Creating...' + name)
        cv2.imwrite(name, frame)

    currentFrame+=1

    # To stop duplicate images
end=perf_counter()
print(f"image rate={(end-start)/currentFrame}")

cap.release()
cv2.destroyAllWindows()