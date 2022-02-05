from tkinter import *
import subprocess
import signal
import os
import signal

root=Tk()
root.geometry("500x500")

def monitor():
    subprocess.run("ifconfig wlan0 down",shell=True)
    subprocess.run("iwconfig wlan0 mode monitor",shell=True)
    subprocess.run("ifconfig wlan0 up",shell=True)

def airodump():
    i=1
    while i<5:
        subprocess.run("airodump-ng wlan0 --write wifinetworks",shell=True,timeout=10)
        i+=1

def stop():
    signal.SIGINT
    exit()

button2=Button(root,text="Monitor Mode",command=monitor)
button2.place(x=200,y=100)

button3=Button(root,text="airodump-ng",command=airodump)
button3.place(x=330,y=100)

button4=Button(root,text="Stop",command=stop)
button4.place(x=200,y=200)


root.mainloop()
