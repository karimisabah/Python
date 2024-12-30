from tkinter import *
import time
from datetime import datetime
import pytz
from timezonefinder import timezonefinder
import geocoder

window = Tk()
window.title("Digital Clock")
window.geometry("800x500")

def myTime():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    secend = time.strftime("%S")
    am_pm = time.strftime("%p")
    day = time.strftime("%A")
    date = time.strftime("%Y-%m-%d")
    zone = time.strftime("%Z")

    myText = hour + ":" + minute + ":" + secend + " " + am_pm
    myText2 = day + ", " + date + "\n" + zone

    myLabel.config(text=myText)
    myLabel2.config(text=myText2)

    myLabel.after(1000, myTime)


myLabel = Label(window, text="", font=("Calibri", 72, "bold"), fg="Yellow", bg="Gray")
myLabel.pack()

myLabel2 = Label(window, text="MK", font=("calibri", 38, "bold"), fg="Yellow", bg="Purple")
myLabel2.pack()

myTime()
window.mainloop()

