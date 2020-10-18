import numpy as np
from numpy.fft import fft,fftfreq,ifft
import matplotlib.pyplot as plt
%matplotlib qt
t=np.linspace(0,4*np.pi,1000)

f1=1
f2=2
y=np.sin(2*np.pi*f1*t)
y+=np.sin(2*np.pi*f2*t)
fourier=fft(y)

#plt.plot(fourier)
#plt.xlim(0,2*np.pi)
#plt.show()
#y=real
#x=complex


dt=float(t[1]-t[0])
n=len(y)

fhat=fft(y,n)
PSD=fhat*np.conj(fhat)/n
freq=(1/(dt*n))*np.arange(n)
L=np.arange(1,np.floor(n/2),dtype='int')
plt.subplot(211)
plt.plot(freq[L],PSD[L])
plt.subplot(212)
plt.plot(t,y)
plt.show()
