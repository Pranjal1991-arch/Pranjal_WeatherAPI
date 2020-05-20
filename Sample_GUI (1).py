# from tkinter import *
# creating the application main window.
# top = Tk()
# Entering the event main loop
# top.mainloop()

# from tkinter import *
#
# parent = Tk()
# redbutton = Button(parent, text="Red", fg="red")
# redbutton.pack(side=LEFT)
# greenbutton = Button(parent, text="Black", fg="black")
# greenbutton.pack(side=RIGHT)
# bluebutton = Button(parent, text="Blue", fg="blue")
# bluebutton.pack(side=TOP)
# blackbutton = Button(parent, text="Green", fg="green")
# blackbutton.pack(side=BOTTOM)
# parent.mainloop()

from tkinter import *

top = Tk()
top.geometry("100x200")
lab = Label(top, text="Welcome to Tkinter")
lab.pack(side=TOP)
# top.geometry("500x500")
# var = StringVar()
# msg = Message(top, text="\nWelcome to Tkinter")
# msg.pack()
top.mainloop()
