from tkinter import *
import subprocess
import signal
import os

root=Tk()
root.geometry("500x500")

def monitor():
    subprocess.run("ifconfig wlan0 down",shell=True)
    subprocess.run("iwconfig wlan0 mode monitor",shell=True)
    subprocess.run("ifconfig wlan0 up",shell=True)

def airodump():
    i=1
    while i<5:
        subprocess.run("airodump-ng wlan0",shell=True,timeout=10)
        i+=1

    String1 = subprocess.check_output('chcp 437 && ping /?', shell=True)
    c.create_text(400, 0, anchor=N, fill='orange', font='Times 15', text=String1)
    # c.create_text(750, 300, anchor=W, fill='orange', font='Times 28', text='List')

    button = Button(root, text="Quit", command=root.destroy)
    c.create_window(400, 0, anchor=N, window=button)

button2=Button(root,text="Monitor Mode",command=monitor)
button2.place(x=200,y=100)

button3=Button(root,text="airodump-ng",command=airodump)
button3.place(x=330,y=100)





root.mainloop()
