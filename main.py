from tkinter import *
window = Tk()
width=500
height=500
window.geometry(f"{width}x{height}")
label=Label(window , text=("Hi there "))
label.grid(row=0,column=2)
window.mainloop()
