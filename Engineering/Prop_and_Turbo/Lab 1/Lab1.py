import pandas as pd 
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq,ifft
import numpy as np
%matplotlib qt

global figure_n
figure_n=0

data148=pd.read_csv("testhigh.dat",sep="\t",header=None)
data148=data148.T
data148=data148.drop(columns=[1])
data148.columns=["microphone signal","square wave","time"]

data192=pd.read_csv("testhigh80.dat",sep="\t",header=None)
data192=data192.T
data192=data192.drop(columns=[1])
data192.columns=["microphone signal","square wave","time"]

def pressure_to_dB(value):
    reference_sound_pressure=0.00002
    return 20*np.log10((value)/(reference_sound_pressure))

def microphone_signal(data,title):
    global figure_n
    dt=float(data["time"][1]-data["time"][0])
    n=len(data)
    

   


    fhat=fft(data["microphone signal"],n)
    PSD=fhat*np.conj(fhat)/n
    freq=(1/(dt*n))*np.arange(n)
    L=np.arange(1,np.floor(n/2),dtype='int')
    
    mic_sens=0.0495
    mic_pressure=data["microphone signal"]/mic_sens

    max_pressure=max(mic_pressure)
    dB_max_pressure=pressure_to_dB(max_pressure)

    rms = np.sqrt(np.mean(mic_pressure**2))
    dB_rms=pressure_to_dB(rms)


    print(title)
    print(dB_rms)
    print(dB_max_pressure)

    
    #plt.plot(data["time"],mic_pressure)
    plt.figure(figure_n)
    figure_n+=1
    plt.title(title)
    plt.plot(freq[L],PSD[L])
    plt.show()


def square_wave(data):
    dt=float(data["time"][1]-data["time"][0])
    n=len(data)

    fhat=fft(data["square wave"],n)
    PSD=fhat*np.conj(fhat)/n
    freq=(1/(dt*n))*np.arange(n)
    L=np.arange(1,np.floor(n/2),dtype='int')



    min=7000
    found_freq=[]
    for i,value in enumerate(PSD[L]):
        if value>min:
            found_freq.append((freq[i],value))


    print(found_freq)
    plt.title("Sample square wave")
    plt.plot(freq[L],PSD[L])
    plt.show()

microphone_signal(data148,"Thrust=148N")
microphone_signal(data192,"Thrust=192N")