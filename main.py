
from readData import dataString
import Graphics
from tkinter import *
# Initialize a window
window= Tk()
window.geometry('900x500')
# Create an instance of a canvas
_canvas = Canvas(window,height=200,width=200)
_canvas.place(anchor='center', x=450, y=250)
# create rectangle
#_canvas.create_line(50, 50, 180, 120)

r=Graphics.shape('cube.obj', _canvas)
r.origin=[0,3,0]
r.color="white"
r.rotation=[0,0,45]
r.render()

label = Label(
    text="Hello, Tkinter",
    foreground="white"
)
label.place(anchor='center', x=450, y=20)

B0 = Button(window, text='Button')
B0.place(x=40, y=40)
B1 = Button(window, text='Button')
B1.place(x=40, y=80)
B2 = Button(window, text='Button')
B2.place(x=40, y=120)


window.mainloop()

