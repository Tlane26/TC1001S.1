"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    up() #Mueve el cursor sin dibujar
    goto(start.x, start.y)
    down() #Mueve el cursor mientras dibuja
    begin_fill() #Funcion que permite el trazado de la figura

    for count in range(2): #Bucle para el trazado y rellenado de la figura
        forward(end.x - start.x)
        left(90)
        forward(end.x + start.x / 2)
        left(90)
    end_fill()  # Termina la funcion de rellenado // sin esta linea la figura solo tiene borde

def triangle(start, end):
    "Draw triangle from start to end."
    up() #Mueve el cursor sin dibujar
    goto(start.x, start.y)
    down() #Mueve el cursor mientras dibuja
    begin_fill() #Funcion que permite el trazado de la figura

    for count in range(1): #Bucle para el trazado y  rellenado de la figura
        forward(end.x - start.x) 
        left(120)
        forward(end.x - start.x)
        left(120)
        forward(end.x - start.x)
        
    end_fill() # Termina la funcion de rellenado // sin esta linea la figura solo tiene borde

def trapeze(start, end): # Funcion de trapecio agregada 
    "Draw trapeze from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(120)
        forward(end.x - start.x)
        left(60)
        
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', trapeze), 'p')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()