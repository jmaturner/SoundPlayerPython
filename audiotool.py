import tkinter as tk
import numpy as np
import sounddevice as sd
import soundfile as sf
from matplotlib import pyplot as plt
from matplotlib import style
from tkinter import *


LARGE_FONT = ("Verdana", 12)

class soundz(tk.Tk):

    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container,self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="snew")

        self.show_frame(StartPage)
        

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

#this function allows the user to browse for the data file
def uploaddata():
    global fileloc
    fileloc = filedialog.askopenfilename()
   
#plays the file
def playfile():
    global data,fs
    data,fs=sf.read(fileloc)
    sd.play(data,fs)

def stopfile():
    sd.stop(data)

#this function performs fft on data
def dofft(self):
    style.use('ggplot')
    data,fs=sf.read(fileloc)
    fft1=np.fft.fft(data)
    freqs=np.fft.fftfreq(len(fft1))
    inhertz=abs(freqs*fs)
    plt.plot(inhertz,abs(fft1))
    plt.title('Signal Spectrum FFT')
    plt.xlabel('Freq Hz')
    plt.ylabel('Power')
    plt.show()



class StartPage(tk.Frame): #makes a new page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Upload a wav file", font=LARGE_FONT)
        label.pack(pady=20,padx=10)

        #uploads the wav file
        button2 = tk.Button(self, text="Upload a data file",
                            command=uploaddata)
        button2.pack(pady=10,padx=10,side=LEFT)

        #plays the file
        button3 = tk.Button(self, text="Play",
                            command=playfile)
        button3.pack(pady=10,padx=10,side=RIGHT)
        #stops the file
        button4 = tk.Button(self, text="Stop",
                            command=stopfile)
        button4.pack(pady=10,padx=10,side=RIGHT)    

        #add button to perform FFT on data
        button5 = tk.Button(self, text="Perform the FFT and plot",
                            command=lambda: dofft("this worked"))
        button5.pack(pady=10,padx=10,side=RIGHT)
        
        
        

app = soundz()
app.mainloop()









