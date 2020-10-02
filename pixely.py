import turtle
okno = turtle.Screen()
okno.bgcolor("#808080")
okno.title("Pixely")

pero = turtle.Turtle()
pero.speed(0)

def stvorec(strana,farba):
    pero.color(farba)
    pero.begin_fill()
    for i in range(4):
        pero.forward(strana)
        pero.left(90)

    pero.forward(strana)
    pero.end_fill()

def kresli_riadok(zoznam):
    for i in zoznam:

        if i==1:

            stvorec(velkost,"white")
        else:
            pero.up()
            pero.forward(velkost)

pero.up()
pero.setpos(-200,200)
pero.down()
# for i in range(10):
#     stvorec(15,"red")
velkost = 30
# riadok =[1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1]
# kresli_riadok(riadok)

obrazok = [[1,1,1],[1,0,0],[1,1,1],[1,0,0],[1,1,1]]
for i in obrazok:
    kresli_riadok(i)
    pero.backward(velkost*len (i))
    pero.right(90)
    pero.forward(velkost)
    pero.left(90)






okno.exitonclick()
