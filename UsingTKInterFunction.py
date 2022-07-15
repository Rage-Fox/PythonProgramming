#tkinter is used to create interfaces
import tkinter as tk #"as" in "Python" is typedef in "C language"
from tkinter import messagebox
a=tk.Tk()
a.title("Custom Title")
#b=tk.Button(a,text="Submit",fg="Red",bg="Black")
#b.pack(side="left")#indicates particular position where program needs to place the button!
##if you don't give any side mentioning inside pack, then submit will appear in top center position by default
#c=tk.Button(a,text="Submit",fg="Green",bg="Black")#foreground color and background colour
#c.pack(side="left")
#grid or place can be also used as the function pack
#d=tk.Button(a,text="Submit")
#d.grid(row=0,column=0)#works like a matrix
#e=tk.Button(a,text="Submit")
#e.grid(row=1,column=1)
#f=tk.Button(a,text="Submit")
#f.place(x=20,y=10)
#g=tk.Button(a,text="Submit")
#g.place(x=50,y=60)
##h=tk.Label(a,text="First Name: ",fg="black",bg="red")
##h.grid(row=0,column=0)
##i=tk.Entry(a)
##i.grid(row=0,column=1)
##j=tk.Label(a,text="Last Name: ",fg="black",bg="red")
##j.grid(row=1,column=0)
##k=tk.Entry(a)
##k.grid(row=1,column=1)
##l=tk.Checkbutton(a,text="Agree",fg="black",bg="red")
##l.grid(row=3,column=0)
##m=tk.Listbox(a)
##m.insert(1,"c")
##m.insert(2,"c++")
##m.insert(3,"python")
##m.insert(4,"golang")
##m.grid(row=2,column=0)
##n=tk.Toplevel()#opens another widget
##n.title("Submit")
##o=tk.Spinbox(a,from_=10,to=20)
##o.pack(side="left")
##a.geometry("200x250")#shape of window
##p=tk.Spinbox(a,from_=10,to=20)
##p.pack(side="left")
##q=tk.LabelFrame(a,text="This is a Frame")#used to write inside a border
##q.pack(fill="both",expand="yes")
##r=tk.Label(q,text="Hello")
##r.pack()
'''Developing background functionality to the button'''
##def example():
##    #message box has to be imported specifically(see 2nd line)
##    #messagebox also has many functions like askquestion, askretrycancel, etc....
##    messagebox.showinfo("Hey there!","Login Successful")
###s=tk.Button(a,text="Submit",command=a.destroy)#when we click the submit button, then the window closes due to destroy command
##s=tk.Button(a,text="Submit",command=example)
##s.pack()
a.mainloop()#.keeps interface in active condition
