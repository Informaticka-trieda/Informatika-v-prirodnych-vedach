# K pracovnemu listu 1
#
# Vykreslenie obrazku pomocou korytnacej grafiky
# Pouzitie kniznice s korytnacou grafikou
import turtle

# Priprava grafickeho okna na vykreslenie
okno = turtle.Screen()
okno.bgcolor(0.7, 0, 0.5)
okno.title("Vykreslenie obsahu 0/1 pola")

# Priprava pera a rychlosti a farby korytnacky kor
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")

##################################################################################
# Funkcia vykresli stvorcek, jeho strany a potom ho vyplni pouzitim funkcie fill
# Parameter fstvorcek predstavuje velkost stvorceka
##################################################################################
fvelkost = 7
def stvorcek(fvelkost):
    myPen.begin_fill()
    for i in range(4):
        myPen.forward(fvelkost)
        myPen.left(90)
    myPen.end_fill()
    myPen.setheading(0)

###################################################################################
# Funkcia vykresli pole pixelov pixs s velkostou stvorceka fstvorcek
###################################################################################
def kresli(pixs, fvelkost):
    farba="#00FF00"
    for i in range(0, len(pixs)):
        for j in range(0, len(pixs[i])):
            if pixs[i][j] == 1:
                myPen.color(farba)
                stvorcek(fvelkost)
            myPen.penup()
            myPen.forward(fvelkost)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(fvelkost)
        myPen.setheading(180)
        myPen.forward(fvelkost * len(pixs[i]))
        myPen.setheading(0)
        myPen.pendown()

def riadok(pixely,vel):
    for i ina range(len(pixely)):
        if pixely[i] == 1:
            stvorcek(vel)
        myPen(vel)













# Ulozenie 0/1 PixelArt (pouzitim "zoznamu v zozname")
# Tak vieme namodelovat akykolvek 0/1 zoznam v zozname

# Nastavenie pozicie pera korytnacky na poziciu, kde zacne kreslenie;
# Na zaciatku je v lavom hornom rohu
myPen.penup()
myPen.forward(-90)
myPen.setheading(90)
myPen.forward(90)
myPen.setheading(0)

velkost = 20
myPen.setposition(-120,150)
for i in range(4):
    stvorcek(velkost)
    myPen.forward(velkost)
print("Velkost boxu pre pixel je", velkost)

riadok(pixely)
pixels1 =[1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1]

pixels =     [[0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]
pixels.append([0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
pixels.append([0, 1, 0, 0, 0, 0, 0, 0, 1, 0])
pixels.append([0, 1, 0, 1, 0, 0, 1, 0, 1, 0])
pixels.append([0, 1, 0, 0, 0, 0, 0, 0, 1, 0])
pixels.append([0, 1, 0, 0, 0, 0, 0, 0, 1, 0])
pixels.append([0, 1, 0, 1, 1, 1, 1, 0, 1, 0])
pixels.append([0, 1, 0, 0, 0, 0, 0, 0, 1, 0])
pixels.append([0, 0, 1, 0, 0, 0, 0, 1, 0, 0])
pixels.append([0, 0, 0, 1, 1, 1, 1, 0, 0, 0])
print(pixels)
myPen.penup()
myPen.forward(90)
myPen.pendown()
#kresli(pixels, velkost)
myPen.getscreen().update()



okno.exitonclick()
