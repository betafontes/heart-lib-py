import turtle
import random
import time

#  Janela
window = turtle.Screen()
window.setup(1000, 750)
window.title("Coração Animado")
window.bgcolor("#fde2e4")
window.tracer(0)

# Coração
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)
heart.pensize(3)

# Corações Flutuantes
floaters = []

# Brilhinhos
sparkles = []

def draw_heart(scale=1.0):
    heart.clear()
    heart.penup()
    heart.goto(0, -20 * scale)
    heart.setheading(0)
    heart.pendown()
    heart.color("#c9184a", "#ff4d6d")

    heart.begin_fill()
    heart.left(140)
    heart.forward(160 * scale)

    for _ in range(200):
        heart.right(1)
        heart.forward(1.8 * scale)

    heart.left(120)

    for _ in range(200):
        heart.right(1)
        heart.forward(1.8 * scale)

    heart.forward(160 * scale)
    heart.end_fill()

# Função dos corações flutuantes
def create_floater():
    f = turtle.Turtle()
    f.hideturtle()
    f.speed(0)
    f.penup()
    f.shape("circle")
    f.shapesize(0.5)
    f.color(random.choice(["#ff758f", "#ff4d6d", "#ffb3c1"]))
    f.goto(random.randint(-450, 450), random.randint(-350, -250))
    f.setheading(90)
    f.showturtle()
    floaters.append(f)

def move_floaters():
    for f in floaters:
        f.goto(f.xcor(), f.ycor() + random.uniform(0.5, 1.5))
        if f.ycor() > 380:
            f.goto(random.randint(-450, 450), -350)

# função dos brilhinhos
def create_sparkle():
    s = turtle.Turtle()
    s.hideturtle()
    s.speed(0)
    s.penup()
    s.shape("circle")
    s.shapesize(0.2)
    s.color(random.choice(["#ffffff", "#ffe5ec", "#ffd6e0"]))
    s.goto(random.randint(-350, 350), random.randint(-150, 300))
    s.setheading(random.randint(0, 360))
    s.showturtle()
    sparkles.append(s)

def move_sparkles():
    for s in sparkles:
        s.forward(0.3)
        if abs(s.xcor()) > 480 or abs(s.ycor()) > 360:
            s.goto(random.randint(-350, 350), random.randint(-150, 300))

#cria os elementos
for _ in range(25):
    create_floater()

for _ in range(30):
    create_sparkle()

# animação do batimento do coração
scale = 1.0
growing = True

# loop principal
while True:
    draw_heart(scale)
    move_floaters()
    move_sparkles()

    # batimentos suaves
    if growing:
        scale += 0.008
        if scale >= 1.06:
            growing = False
    else:
        scale -= 0.008
        if scale <= 0.98:
            growing = True

    window.update()
    time.sleep(0.03)