import turtle
from PIL import Image
okno = turtle.Screen()
okno.bgcolor("#808080")
okno.title("Pracovný list 02")
pero = turtle.Turtle()
pero.speed(0)

def namiesajFarbu(fr,fg,fb):
    farba = f"#{fr:02x}{fg:02x}{fb:02x}"
    return (farba)

def stvorec(strana,farba):
    pero.color(farba)
    pero.begin_fill()
    for i in range(4):
        pero.forward(strana)
        pero.left(90)



meno = ("obrPixely1.png")
print(meno)
img = Image.open(meno)
print(f"veľkosť obrázka je : {img.size}")

pxl_mapa = img.load()

#img.show()

print(f"červená R = {pxl_mapa[5,7][0]}")
print(f"zelená G = {pxl_mapa[5,7][1]}")
print(f"modrá B = {pxl_mapa[5,7][2]}")
print(f"priesv. A = {pxl_mapa[5,7][3]}")

for stlpec in range(img.size[0]):
    print(stlpec,pxl_mapa[2,stlpec])



print(namiesajFarbu(pxl_mapa[5,7][0],pxl_mapa[5,7][1],pxl_mapa[5,7][2]))

okno.mainloop()
