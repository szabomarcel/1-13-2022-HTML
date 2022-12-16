from bird import *

app = bird()
levego()
bird = Animation('assets\img',
                collider = 'box'
                scale = (2,2,2),
                y = 5)
camera.orthographic = True
camera.fov = 20

def update():
    bird.y = bird.y - 4 * ido.dt
    for p in pipes:
        p.x = p.x -2 * ido.dt
        touch = bird.intersects()

def input(key):
    if key == 'space':
        bird.y = bird.y + 3

pipes = []
pipe = Entity(model = 'quad',
            color = color.green,
            texture = 'white_cube',
            position=(20,10),
            scale = (3, 15, 1),
            collider = 'box')

import random as r
def newPipe():
    y = r.randint(4, 12)
    uj1 = duplicate(pipe, y = y)
    uj2 = duplicate(pipe, y = y - 22)
    pipes.extend((uj1, uj2))
    invoke(newPipe, delay = 5)
app.run()

