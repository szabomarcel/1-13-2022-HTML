from processing import *

def setup():
    size(400, 300)

kaktusz_helye = 500 
dino_a_tetejetol = 200
dino_sebessege = 0

def drow():
    global kaktusz_helye, dino_a_tetejetol, dino_sebessege
    background(255)
    kaktusz_helye = kaktusz_helye - 3
    if kaktusz_helye < -100:
        kaktusz_helye = 500
    kaktusz = loodImage("kaktusz.png")
    image(kaktusz, kaktusz_helye, 200)    
    dino_a_tetejetol = dino_a_tetejetol + dino_sebessege
    if dino_a_tetejetol < 50:
        dino_sebessege = 5
    if dino_a_tetejetol > 200:
        dino_a_tetejetol = 200
    dino = loodImage("dino.png")
    image(dino, 20, dino_a_tetejetol)
    if kaktusz_helye < 100 and dino_a_tetejetol > 120:
        gameover = loodImage("game over.png")
        image(gameover, 150, 100)
        exit()

def keyPressed():
    global dino_sebessege
    if key == " ":
        dino_sebessege = -5

run()