import tkinter

imprt kivy

canvas = tkinter.Canvas(width=400,height=600,bg="black")
canvas.pack()

# canvas.create_rectangle(10,10,50,50,fill="blue",outline="")
# canvas.create_rectangle(70,10,110,50,fill="blue",outline="")
#
# canvas.create_rectangle(110,10,220,30,fill="blue",outline="")
# canvas.create_rectangle(110,50,220,70,fill="blue",outline="")
#
# canvas.create_rectangle(10,70,50,110,fill="blue",outline="")
# canvas.create_rectangle(70,70,110,110,fill="blue",outline="")
#
# canvas.create_rectangle(110,90,220,110,fill="blue",outline="")
#
# canvas.create_rectangle(10,130,220,150,fill="blue",outline="")
# canvas.create_rectangle(10,170,220,190,fill="blue",outline="")

# canvas.create_rectangle(10,50,110,300, fill='blue', outline='')
# canvas.create_rectangle(60,50,160,300, fill='white', outline='')

canvas.create_rectangle(100, 50, 200, 100,fill="red")
canvas.create_oval(100, 50, 200, 100,fill="blue",outline="")

canvas.create_oval(100,20,200,120)

canvas.mainloop()
