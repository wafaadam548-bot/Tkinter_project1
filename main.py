from tkinter import *
window = Tk()
width=500
height=500
window.geometry(f"{width}x{height}")
def hi():
    label=Label(window , text=("Hi there "))
    label.grid(row=4,column=4)
start=Button(window, text=("start",font=("Arial",30)),command=hi)
start.grid(row=0,column=0,columnspan=4)
window.mainloop()
