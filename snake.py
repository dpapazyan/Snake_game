import turtle

WIDTH = 500
HEIGHT = 500
DELAY = 400  # милисекунды

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    if new_head in snake or new_head[0] < - WIDTH/2 or new_head[0] > WIDTH/2 \
        or new_head[1] < - HEIGHT/2 or new_head[1] > HEIGHT/2:
        turtle.bye()
    else:
        # добавляем новую голову змейки
        snake.append(new_head)

        # удаляем хвост змейки
        snake.pop(0)

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # обновляем экран
        screen.update()

        # поворяем
        turtle.ontimer(game_loop, DELAY)


# создание окна для рисования
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)  # отключает автоматическую анимацию


# управление событиями
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")


stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# создаем змейку как список координат
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"

# рисуем змею
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

game_loop()

turtle.done()