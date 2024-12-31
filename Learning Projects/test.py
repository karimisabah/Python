from tkinter import *
import time
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder
import geocoder

window = Tk()
window.title("Digital Clock")
window.geometry("650x650")


def get_user_location():
    g = geocoder.ip("me")
    latitude, longitude = g.latlng
    tf = TimezoneFinder()
    timezone = tf.timezone_at(lng= longitude, lat= latitude)
    location = g.city if g.city else "Unknown Location"
    return location, timezone

user_location, user_timezone = get_user_location()

# تابع به‌روزرسانی زمان
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

    if selected_timezone.get() != "":
        timezone = pytz.timezone(selected_timezone.get())
        tz_time = datetime.now(timezone)
        tz_hour = tz_time.strftime("%I")
        tz_minute = tz_time.strftime("%M")
        tz_second = tz_time.strftime("%S")
        tz_am_pm = tz_time.strftime("%p")
        tz_day = tz_time.strftime("%A")
        tz_date = tz_time.strftime("%Y-%m-%d")

        tz_text = f"{tz_hour}:{tz_minute}:{tz_second} {tz_am_pm}\n{tz_day}, {tz_date}\n{selected_timezone.get()}"
        tzLabel.config(text=tz_text)
    else:
        tzLabel.config(text="")

    myLabel.after(1000, myTime)

# تابع برای جستجوی مناطق زمانی
def search_timezone(event):
    query = search_entry.get().lower()
    filtered_timezones = [tz for tz in pytz.all_timezones if query in tz.lower() ]
    update_listbox(filtered_timezones)

# به‌روزرسانی لیست مناطق زمانی
def update_listbox(filtered_timezones):
    timezone_listbox.delete(0, END)
    for tz in filtered_timezones:
        timezone_listbox.insert(END, tz)

# انتخاب منطقه زمانی از لیست
def select_timezone(event):
    selected_timezone.set(timezone_listbox.get(timezone_listbox.curselection()))

# لیبل‌های ساعت اصلی
myLabel = Label(window, text="", font=("Calibri", 72, "bold"), fg="Yellow", bg="Gray")
myLabel.pack()

myLabel2 = Label(window, text="", font=("calibri", 38, "bold"), fg="Yellow", bg="Purple")
myLabel2.pack(pady=10)

# لیبل برای ساعت منطقه زمانی انتخاب‌شده
tzLabel =Label(window, text="", font=("Calibri", 24, "bold"), fg="White", bg="Blue")
tzLabel.pack(pady=10)

# فیلد جستجو
search_entry = Entry(window, font=("Calibri", 14))
search_entry.pack(pady=10)
search_entry.bind("<KeyRelease>", search_timezone)

# اسکرول و لیست مناطق زمانی
frame = Frame(window)
frame.pack()

scrollbar = Scrollbar(frame, orient=VERTICAL)
timezone_listbox = Listbox(frame, font=("Calibri", 14), yscrollcommand=scrollbar.set, height=10, width=40)
scrollbar.config(command=timezone_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
timezone_listbox.pack(side=LEFT, fill=BOTH)

# مقداردهی اولیه لیست مناطق زمانی
timezones = sorted(pytz.all_timezones)
update_listbox(timezones)

# اتصال انتخاب منطقه زمانی به لیست
selected_timezone = StringVar()
selected_timezone.set("")
timezone_listbox.bind("<<ListboxSelect>>", select_timezone) 

# اجرای تابع ساعت
myTime()

window.mainloop()

