import pandas as pd 
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy import signal
import numpy as np
%matplotlib qt

global figure_n
figure_n=0
if 'data148' not in locals():
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


def microphone_signal(data,title,estimate):
    global figure_n
    dt=float(data["time"][1]-data["time"][0])
    n=len(data)
    
    mic_sens=0.0495
    mic_pressure=data["microphone signal"]/mic_sens


    fhat=np.fft.fft(mic_pressure,n)
    print(fhat)
    PSD=fhat*np.conj(fhat)/n
    #f,PSD = signal.periodogram(fhat,4000)
    freq=(1/(dt*n))*np.arange(n)
    L=np.arange(1,np.floor(n/2),dtype='int')
    
    

    max_pressure=max(mic_pressure)
    dB_max_pressure=pressure_to_dB(max_pressure)

    rms = np.sqrt(np.mean(mic_pressure**2))
    dB_rms=pressure_to_dB(rms)


    print(title)
    print(f"rms={round(dB_rms,2)}dB ({round(rms,2)})")
    print(f"max={round(dB_max_pressure,2)}dB ({round(max_pressure,2)})")

    
    #plt.plot(data["time"],mic_pressure)
    plt.figure(figure_n)
    figure_n+=1
    #plt.title(title)
    plt.plot(freq[L],PSD[L])

    number_of_lines=int(freq[L[-1]]/estimate)
    #print(number_of_lines)
    for i in range(1,number_of_lines+1):
        #print(i)
        #plt.plot([i*estimate,i*estimate],[0,210000],'r--',alpha=0.3)
        pass
    #plt.text(0,100000,"dont copy",size=50)
    plt.xlabel("frequency (Hz)")
    plt.ylabel("Power spectral density (Vrms^2)")
    #plt.ylim(0,210000)
    plt.xlim(0)
    plt.tight_layout()
    plt.show()
    plt.savefig(f"{title}.png")

def scipy_python_test(data,title):
    global figure_n
    T=float(data["time"][1]-data["time"][0])
    N=len(data)
    
    mic_sens=0.0495
    mic_pressure=np.array(data["microphone signal"]/mic_sens)

    yf=fft(mic_pressure)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    plt.figure(figure_n)
    figure_n+=1
    plt.plot(xf,2.0/N*np.abs(yf[0:N//2]))
    #plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.title(title)
    plt.show()

    max_pressure=max(mic_pressure)
    dB_max_pressure=pressure_to_dB(max_pressure)

    rms = np.sqrt(np.mean(mic_pressure**2))
    dB_rms=pressure_to_dB(rms)

    print(title)
    print(f"rms={round(dB_rms,2)}")
    print(f"max={round(dB_max_pressure,2)}")

def scipy_python_test_square(data,title):
    global figure_n
    T=float(data["time"][1]-data["time"][0])
    N=len(data)
    
    mic_sens=0.0495
    mic_pressure=np.array(data["microphone signal"]/mic_sens)
    print(mic_pressure)
    print("bruh")
    yf=fft(mic_pressure)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    figure(figure_n)
    figure_n+=1
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.title(title)
    plt.grid()
    plt.show()

def square_wave(data,title):
    global figure_n
    estimate=261
    dt=float(data["time"][1]-data["time"][0])
    n=len(data)

    fhat=np.fft.fft(data["square wave"],n)
    PSD=fhat*np.conj(fhat)/n
    freq=(1/(dt*n))*np.arange(n)
    L=np.arange(1,np.floor(n/2),dtype='int')

    
    
    plt.figure(figure_n)
    figure_n+=1
    plt.plot(freq[L],PSD[L])
    plt.xlim(0,3000)
    plt.ylim(0)
    estimate=261
    number_of_lines=int(freq[L[-1]]/estimate)

    for i in np.arange(1,19,2):
        plt.plot([i*estimate,i*estimate],[0,max(PSD[L])],'r--',alpha=0.3)
    print(max(PSD))
    plt.xlabel("frequency (Hz)")
    plt.ylabel("Power spectral density (Vrms^2)")
    plt.tight_layout()
    plt.show()
    plt.savefig(f"{title}.png")


def fft_matlab_example(data):
    Fs=40000
    t=data["time"]
    T=1/Fs
    L=1000

    mic_sens=0.0495
    mic_pressure=data["microphone signal"]/mic_sens

    Y = np.fft.fft(mic_pressure)

    P2=abs(Y/L)
    print((L/2)+1)
    P1= P2[0:int(L/2)]
    P1*=2

    f=(Fs/L)*(np.arange(0,L/2))
    plt.plot(f,P1,linewidth=1)
    plt.title("Fourier Transform of microphone signal")
    plt.xlabel("frequency (Hz)")
    plt.ylabel("|Pressure (Pa)|")
    plt.xlim(0,20000)
    plt.ylim(0,80)
    plt.savefig("2388083M_PropLab_Fourier.png")

#square_wave(data148,"Square wave")
#square_wave(data192,"192 Square wave")

#microphone_signal(data148,"Thrust=148N",1646)
#microphone_signal(data192,"Thrust=192N",1772)

#scipy_python_test(data148,"Scipy 148")
#scipy_python_test(data192,"Scipy 192")

fft_matlab_example(data148)