import cv2 as cv2
import matplotlib.pyplot as plt

cam = cv2.VideoCapture(0)
ret, frame = cam.read()
cam.release()
image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()



