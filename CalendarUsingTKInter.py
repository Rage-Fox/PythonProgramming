from tkinter import *
#'*'-->import all the packages from tkinter
import tkinter as tk
import calendar
r=tk.Tk()
r.geometry("400x300")
r.title("Calendar")
def show():
    m=int(month.get())
    y=int(year.get())
    output=calendar.month(y,m)
    cal.insert("end",output)
def clear():
    cal.delete(1.0,"end")
def exit():
    r.destroy()
m_label=Label(r,text="Month",font=("veranda","10","bold"))
m_label.place(x=70,y=80)
month=Spinbox(r,from_=1,to=12,width="5")
month.place(x=140,y=80)
y_label=Label(r,text="Year",font=("veranda","10","bold"))
y_label.place(x=210,y=80)
year=Spinbox(r,from_=1000,to=3000,width="8")
year.place(x=260,y=80)
cal=Text(r,width=33,height=8,relief=RIDGE,borderwidth=2)
cal.place(x=70,y=110)
show=Button(r,text="Show",command=show)
show.place(x=140,y=250)
clear=Button(r,text="Clear",command=clear)
clear.place(x=200,y=250)
exit=Button(r,text="Exit",command=exit)
exit.place(x=260,y=250)
r.mainloop()
