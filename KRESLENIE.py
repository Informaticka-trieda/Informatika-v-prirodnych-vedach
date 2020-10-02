import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(10,10,150,100)
canvas.create_rectangle(150,100,300,10)


canvas.mainloop()
