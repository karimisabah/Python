from tkinter import *
import pytz
from datetime import datetime

def get_timezones_with_offsets():
    timezone_offsets = []
    utc = datetime.utcnow()  
    for tz in pytz.all_timezones:
        timezone = pytz.timezone(tz)
        offset = timezone.utcoffset(utc)  
        if offset is not None:
            offset_hours = int(offset.total_seconds() // 3600)
            offset_minutes = int((offset.total_seconds() % 3600) // 60)
            sign = "+" if offset_hours >= 0 else "-"
            offset_string = f"GMT{sign}{abs(offset_hours):02}:{abs(offset_minutes):02}"
            timezone_offsets.append(f"{tz} ({offset_string})")
    return sorted(timezone_offsets)

def search_timezone(event):
    query = search_entry.get().lower()
    filtered_timezones = [tz for tz in timezones_with_offsets if query in tz.lower()]
    update_listbox(filtered_timezones)

def update_listbox(filtered_timezones):
    timezone_listbox.delete(0, END)
    for tz in filtered_timezones:
        timezone_listbox.insert(END, tz)

def select_timezone(event):
    try:
        selection = timezone_listbox.get(timezone_listbox.curselection())
        selected_timezone.set(selection.split(" (")[0]) 
        update_selected_timezone()
    except TclError:
        pass

def update_selected_timezone():
    if selected_timezone.get():
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

def myTime():
    now = datetime.now()
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    am_pm = now.strftime("%p")
    day = now.strftime("%A")
    date = now.strftime("%Y-%m-%d")

    myText = hour + ":" + minute + ":" + second + " " + am_pm
    myText2 = day + ", " + date + "\nLocal Time"

    myLabel.config(text=myText)
    myLabel2.config(text=myText2)

    update_selected_timezone()
    myLabel.after(1000, myTime)

window = Tk()
window.title("Digital Clock with Timezones")
window.geometry("800x600")

myLabel = Label(window, text="", font=("Calibri", 72, "bold"), fg="Yellow", bg="Gray")
myLabel.pack()

myLabel2 = Label(window, text="", font=("Calibri", 34, "bold"), fg="Yellow", bg="Purple")
myLabel2.pack(pady=10)

tzLabel = Label(window, text="", font=("Calibri", 24, "bold"), fg="White", bg="Blue")
tzLabel.pack(pady=10)

search_entry = Entry(window, font=("Calibri", 14))
search_entry.pack(pady=10)
search_entry.bind("<KeyRelease>", search_timezone)

frame = Frame(window)
frame.pack()

scrollbar = Scrollbar(frame, orient=VERTICAL)
timezone_listbox = Listbox(frame, font=("Calibri", 14), yscrollcommand=scrollbar.set, height=10, width=50)
scrollbar.config(command=timezone_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
timezone_listbox.pack(side=LEFT, fill=BOTH)

timezones_with_offsets = get_timezones_with_offsets()
update_listbox(timezones_with_offsets)

selected_timezone = StringVar()
selected_timezone.set("")
timezone_listbox.bind("<<ListboxSelect>>", select_timezone)

myTime()
window.mainloop()
