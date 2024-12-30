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
    hour = time.strftime('%H')
    minute = time.strftime( '%M')
    second = time.strftime( '%S')
    myText = hour + ':' + minute + ':' + second
    myLabel.config(text=myText)
    myLabel.after(1000, myTime)

myLabel = Label(window, text="", font=('Calibri', 68), fg='Yellow', bg='Gray')
myLabel.pack()

myTime()

window.mainloop()