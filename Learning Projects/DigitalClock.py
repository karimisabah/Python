from tkinter import *
import time
# از این دو کتابخانه یا ماژور می خواهم استفاده کنم 
# از توابع درونی آن تا داخل این پروژه کدهای را بنویسم (در واقع من نمی خواهم از صفر همه چیز را خودم کد نویسی کنم) 
# منظور از خط اول یعنی اینکه تمام نوابعی که در کینتر وجود داره 
# را برای من استخراج بکن و بیار اینجا تا من زمانی من میخواهم تابعی را بنویسم مجبور نباشم تابع تینکر را دوباره بنویسم
window = Tk()
window.title('Digital Clock')
window.geometry('500x250')

def myTime():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime('%p')
    day = time.strftime('%A')
    zone = time.strftime('%z')

    myText = hour + ':' + minute + ':' + second + ' ' + am_pm
    myText2 = day + ", " + zone

    myLabel.config(text=myText)
    myLabel2.config(text=myText2)
    myLabel.after(1000, myTime)

myLabel = Label(window, text="", font=('Calibri', 72), fg='Yellow', bg='Gray')
myLabel.pack()
myLabel2 = Label(window, text="", font=("Calicri", 48, "bold"), fg="Yellow", bg="Purple")
myLabel2.pack()

myTime()

window.mainloop()