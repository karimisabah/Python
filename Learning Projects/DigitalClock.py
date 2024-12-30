from tkinter import *
import time
import pytz 
from datetime import datetime
# از این دو کتابخانه یا ماژور می خواهم استفاده کنم 
# از توابع درونی آن تا داخل این پروژه کدهای را بنویسم (در واقع من نمی خواهم از صفر همه چیز را خودم کد نویسی کنم) 
# منظور از خط اول یعنی اینکه تمام نوابعی که در کینتر وجود داره 
# را برای من استخراج بکن و بیار اینجا تا من زمانی من میخواهم تابعی را بنویسم مجبور نباشم تابع تینکر را دوباره بنویسم
window = Tk()
window.title('Digital Clock')
window.geometry('800x500')

select_zone = StringVar(window)
select_zone.set("UTC")

timezones = sorted(pytz.all_timezones)

def myTime():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime('%p')
    day = time.strftime('%A')
    date = time.strftime('%Y-%m-%d')
    zone = time.strftime('%Z')

    myText = hour + ':' + minute + ':' + second + ' ' + am_pm
    myText2 = day + ", " + date + "\n" + zone 

    myLabel.config(text=myText)
    myLabel2.config(text=myText2)

    if selected_timezone.get() != "":
        timezone = pytz.timezone(selected_timezone.get())
        tz_time = datetime.now(timezone)
        tz_hour = tz_time.strftime('%I')
        tz_minute = tz_time.strftime('%M')
        tz_second = tz_time.strftime('%S')
        tz_am_pm = tz_time.strftime('%p')
        tz_day = tz_time.strftime('%A')
        tz_date = tz_time.strftime('%Y-%m-%d')

        tz_text = f"{tz_hour}:{tz_minute}:{tz_second} {tz_am_pm}\n{tz_day}, {tz_date}\n{selected_timezone.get()}"
        tzLable.config(text=tz_text)
    else:
        tzLable.config(text="")

    myLabel.after(1000, myTime)

def search_timezone(event):
    query = search_entry.get().lower()

timezones = pytz.all_timezones

selected_timezone = StringVar()
selected_timezone.set("")

myLabel = Label(window, text="", font=('Calibri', 72, "bold"), fg='Yellow', bg='Gray')
myLabel.pack()

myLabel2 = Label(window, text="", font=("Calibri", 24, "bold"), fg="Yellow", bg="Purple")
myLabel2.pack()

timezone_menu = OptionMenu(window, selected_timezone, *timezones)
timezone_menu.config(font=("Calibri", 14, "bold"))
timezone_menu.pack(pady=10)

tzLable = Label(window, text="", font=("Calibri", 24, "bold"), fg="White", bg="Blue")
tzLable.pack(pady=10)

myTime()

window.mainloop()

