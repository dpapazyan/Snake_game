import turtle
import random

WIDTH = 700
HEIGHT = 700
DELAY = 300  # милисекунды
FOOD_SIZE = 20

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def bind_direction_key():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")


def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":
            snake_direction = "up"
    if direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    if direction == "left":
        if snake_direction != "right":
            snake_direction = "left"
    if direction == "right":
        if snake_direction != "left":
            snake_direction = "right"


# def go_up():
#     global snake_direction
#     if snake_direction != "down":
#         snake_direction = "up"
#
#
# def go_down():
#     global snake_direction
#     if snake_direction != "up":
#         snake_direction = "down"
#
#
# def go_right():
#     global snake_direction
#     if snake_direction != "left":
#         snake_direction = "right"
#
#
# def go_left():
#     global snake_direction
#     if snake_direction != "right":
#         snake_direction = "left"


def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2 or DELAY == 0:
        reset()
    else:
        # добавляем новую голову змейки
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)

            for segment in snake:
                stamper.goto(segment[0], segment[1])
                stamper.stamp()

        # обновляем экран
        screen.title(f"Snake game. Score: {score}")
        screen.update()

        # поворяем
        turtle.ontimer(game_loop, DELAY)


def food_collision():
    global food_pos, score, DELAY
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        DELAY -= 25
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(-WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.randint(-HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # теорема Пифагора (поиск гипотенузы)
    return distance


def reset():
    global score, snake, snake_direction, food_pos, DELAY
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()
    DELAY = 300


# создание окна для рисования
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("orange")
screen.tracer(0)  # отключает автоматическую анимацию

# управление событиями
screen.listen()
bind_direction_key()
# screen.onkey(go_up, "Up")
# screen.onkey(go_right, "Right")
# screen.onkey(go_down, "Down")
# screen.onkey(go_left, "Left")

stamper = turtle.Turtle()
stamper.shape("circle")
stamper.penup()

# создаем змейку как список координат
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"
score = 0

# рисуем змею
# for segment in snake:
#     stamper.goto(segment[0], segment[1])
#     stamper.stamp()

food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.shapesize(FOOD_SIZE / 20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

reset()

turtle.done()
