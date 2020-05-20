from tkinter import *

window = Tk()
window.title("Welcome to Tkinter")
window.geometry('350x200')
lbl = Label(window, text="Hello World")                           # Label
lbl.grid(column=0, row=0)
txt=Entry(window,width=10)                                       # Textbox
txt.grid(column=1,row=0)

def clicked():
    lbl.configure(text="You clicked button")


btn = Button(window, text="Click_me", command=clicked)           # Button
btn.grid(column=2, row=0)
window.mainloop()
