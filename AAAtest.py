import numpy as np
import matplotlib.pyplot as plt 
t_start=0
t_end=2

good_delta_t=0.00001
good_t=np.arange(t_start,t_end+0.001,0.001)

answer_theta = 0.076*(1+4.079*np.exp(-3.66*good_t)-5.079*np.exp(-57.337*good_t))

#plt.subplot(211)
plt.plot(good_t,answer_theta,label="actual answer")