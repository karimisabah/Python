from tkinter import *
import time
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder
import geocoder

# Initialize Tkinter window
window = Tk()
window.title("Digital Clock")
window.geometry("800x500")

# Get the user's location and timezone
def get_user_location():
    g = geocoder.ip('me')  # Gets user's approximate location using their IP
    latitude, longitude = g.latlng
    tf = TimezoneFinder()
    timezone = tf.timezone_at(lng=longitude, lat=latitude)
    location = g.city if g.city else "Unknown Location"
    return location, timezone

user_location, user_timezone = get_user_location()

# Function to update the clock
def myTime():
    now = datetime.now(pytz.timezone(user_timezone))
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    am_pm = now.strftime("%p")
    day = now.strftime("%A")
    date = now.strftime("%Y-%m-%d")

    myText = hour + ":" + minute + ":" + second + " " + am_pm
    myText2 = day + ", " + date + "\n" + user_location + " (" + user_timezone + ")"

    myLabel.config(text=myText)
    myLabel2.config(text=myText2)

    myLabel.after(1000, myTime)

# UI elements
myLabel = Label(window, text="", font=("Calibri", 72, "bold"), fg="Yellow", bg="Gray")
myLabel.pack()

myLabel2 = Label(window, text="MK", font=("calibri", 38, "bold"), fg="Yellow", bg="Purple")
myLabel2.pack()

myTime()
window.mainloop()
