from tkinter import *
from datetime import datetime
import pytz

# تابع برای به‌دست آوردن مناطق زمانی به همراه اختلاف از گرینویچ
def get_timezones_with_offsets():
    timezone_offsets = []
    utc = datetime.utcnow()  # زمان فعلی به صورت ناوابسته به منطقه زمانی
    for tz in pytz.all_timezones:
        timezone = pytz.timezone(tz)
        offset = timezone.utcoffset(utc)  # محاسبه اختلاف زمانی
        if offset is not None:
            offset_hours = int(offset.total_seconds() // 3600)
            offset_minute = int((offset.total_seconds() % 3600) // 60)
            sign = "+" if offset_hours >= 0 else "-"
            offset_string =f"GMT{sign}{abs(offset_hours):02}:{abs(offset_minute):02}"
            timezone_offsets.append(f"{tz} ({offset_string})")
    return sorted(timezone_offsets)



# ایجاد پنجره اصلی
window = Tk()
window.title("Digital Clock")
window.geometry("800x600")

# لیبل‌های ساعت محلی
myLabel = Label(window, text="SABAH", font=("Calibri", 72, "bold"), foreground="Yellow", background="Gray")
myLabel.pack()

myLabel2 = Label(window, text="HELLO", font=("Calibri", 48, "bold"), foreground="Yellow", background="Gray")
myLabel2.pack()

# لیبل ساعت منطقه انتخاب‌شده
tzLabel = Label(window, text="Mahdi", font=("Calibri", 24, "bold"), foreground="White", background="Blue")
tzLabel.pack(pady=10)

# فیلد جستجو
search_entry = Entry(window, font=("Calibri", 14))
search_entry.pack(pady=10)
search_entry.bind("<KeyRelease>", search_timezone)

# قاب برای لیست مناطق زمانی و اسکرول
frame = Frame(window)
frame.pack

scrollar = Scrollbar(frame, orient=VERTICAL)
timezone_listbox = Listbox(frame, font=("Calibri", 14), yscrollcommand=scrollar.set, height=10, width=50)
scrollar.config(command=timezone_listbox.yview)
scrollar.pack(side=RIGHT, fill=Y)
timezone_listbox.pack(side=LEFT, fill=BOTH)

# مقداردهی اولیه لیست مناطق زمانی
selected_timezone = StringVar()
selected_timezone.set("")
timezone_listbox.bind("<<ListboxSelect>>", select_timezone)

# به‌روزرسانی زمان
# myTime()

window.mainloop()
