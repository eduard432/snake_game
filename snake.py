from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def random_color(discard_color = None):
    "Generate random color"
    colors = ['magenta', 'green', 'black', 'blue', 'cyan']
    if(discard_color):
        colors.remove(discard_color)
    
    return choice(colors)
    

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    "Move food one step randomly, staying inside boundaries."
    # Generar movimiento aleatorio: arriba, abajo, izquierda o derecha
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move = choice(directions)
    
    # Calcular nueva posición
    new_x = food.x + move.x
    new_y = food.y + move.y
    
    # Verificar que la nueva posición esté dentro de los límites
    if -200 < new_x < 190 and -200 < new_y < 190:
        food.x = new_x
        food.y = new_y

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, body_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
body_color = random_color()
food_color  = random_color(discard_color=body_color)
move()
done()