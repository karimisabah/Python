from tkinter import *
import time
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder
import geocoder

window = Tk()
window.title("Digital Clock")
window.geometry("800x500")


def get_user_location():
    g = geocoder.ip("me")
    latitude, longitude = g.latlng
    tf = TimezoneFinder()
    timezone = tf.timezone_at(lng= longitude, lat= latitude)
    location = g.city if g.city else "Unknown Location"
    return location, timezone

user_location, user_timezone = get_user_location()

def myTime():
    now = datetime.now(pytz.timezone(user_timezone))
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    secend = now.strftime("%S")
    am_pm = now.strftime("%p")
    day = now.strftime("%A")
    date = now.strftime("%Y-%m-%d")

    myText = hour + ":" + minute + ":" + secend + " " + am_pm
    myText2 = day + ", " + date + "\n" + user_location + " (" + user_timezone + ")"

    myLabel.config(text=myText)
    myLabel2.config(text=myText2)

    if selected_timzone.get() != "":
        timezone = pytz.timezone(selected_timzone.get())
        tz_time = datetime.now(timezone)
        tz_hour = tz_time.strftime("%I")
        tz_minute = tz_time.strftime("%M")
        tz_second = tz_time.strftime("%S")
        tz_am_pm = tz_time.strftime("%p")
        tz_day = tz_time.strftime("%A")
        tz_date = tz_time.strftime("%Y-%m-%d")

        tz_text = f"{tz_hour}:{tz_minute}:{tz_second} {tz_am_pm}\n{tz_day}, {tz_date}\n{selected_timzone.get()}"
        tzLabel.config(text=tz_text)
    else:
        tzLabel.config(text="")


    myLabel.after(1000, myTime)


myLabel = Label(window, text="", font=("Calibri", 72, "bold"), fg="Yellow", bg="Gray")
myLabel.pack()

myLabel2 = Label(window, text="", font=("calibri", 38, "bold"), fg="Yellow", bg="Purple")
myLabel2.pack(pady=10)

tzLabel =Label(window, text="", font=("Calibri", 24, "bold"), fg="White", bg="Blue")
tzLabel.pack(pady=10)

search_entry = Entry(window, font=("Calibri", 14))
search_entry.pack(pady=10)

frame = Frame(window)
frame.pack()

selected_timzone = StringVar()
selected_timzone.set("")


myTime()
window.mainloop()

