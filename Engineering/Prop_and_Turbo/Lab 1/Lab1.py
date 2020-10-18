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
    
    mic_sens=0.0495
    mic_pressure=data["microphone signal"]/mic_sens


    fhat=fft(mic_pressure,n)
    PSD=fhat*np.conj(fhat)/n
    freq=(1/(dt*n))*np.arange(n)
    L=np.arange(1,np.floor(n/2),dtype='int')
    
    

    max_pressure=max(mic_pressure)
    dB_max_pressure=pressure_to_dB(max_pressure)

    rms = np.sqrt(np.mean(mic_pressure**2))
    dB_rms=pressure_to_dB(rms)


    print(title)
    print(f"rms={round(dB_rms,2)}")
    print(f"max={round(dB_max_pressure,2)}")

    
    #plt.plot(data["time"],mic_pressure)
    plt.figure(figure_n)
    figure_n+=1
    plt.title(title)
    plt.plot(freq[L],PSD[L])

    estimate=547
    number_of_lines=int(freq[L[-1]]/estimate)
    print(number_of_lines)
    #print()
    for i in range(1,number_of_lines+1):
        print(i)
        plt.plot([i*estimate,i*estimate],[0,120000])
    plt.show()


def square_wave(data,title):
    global figure_n
    #print(data["time"])
    dt=float(data["time"][1]-data["time"][0])
    n=len(data)

    fhat=fft(data["square wave"],n)
    PSD=fhat*np.conj(fhat)/n
    freq=(1/(dt*n))*np.arange(n)
    L=np.arange(1,np.floor(n/2),dtype='int')


    """
    min=7000
    found_freq=[]
    for i,value in enumerate(PSD[L]):
        if value>min:
            found_freq.append((freq[i],value))
    """

    #print(found_freq)
    plt.figure(figure_n)
    figure_n+=1
    plt.title(title)
    plt.plot(freq[L],PSD[L])
    plt.show()


#square_wave(data148,"148 Square wave")
#square_wave(data192,"192 Square wave")


microphone_signal(data148,"Thrust=148N")
#microphone_signal(data192,"Thrust=192N")