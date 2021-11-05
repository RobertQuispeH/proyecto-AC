import turtle, math, random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("programa Robert")

wn.bgpic("fondo2.gif")
turtle.register_shape("ene3.gif")
turtle.register_shape("drac2.gif")
turtle.register_shape("llamas.gif")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
    
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
border_pen.penup()
border_pen.setposition(-290,-280)
scoreString = "Score: %s" %score
score_pen.write(scoreString, False, align="left", font=("arial",14,"normal"))
score_pen.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("drac2.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 20

num_enemie = 5
enemigos = []
for i in range(num_enemie):
    enemigos.append(turtle.Turtle())
for enemy in enemigos:
    enemy.color("red")
    enemy.shape("ene3.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100,250)
    enemy.setposition(x,y)
    
enemyspeed = 3

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("llamas.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.hideturtle()
bulletstate = "fire"
bulletspeed = 35
xbull = player.xcor() - 10
ybull = player.ycor() + 50
bullet.setposition(xbull,ybull)
bullet.showturtle()




def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False
def position_bullet():
    xbull = player.xcor() - 10
    ybull = player.ycor() + 50
    bullet.setposition(xbull,ybull)
    bullet.showturtle()
def interaccion():
    global enemyspeed
    global bulletstate
    global score
    for enemy in enemigos:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if((enemy.xcor() > 288) or (enemy.xcor() < -280)):
            for e in enemigos:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            position_bullet()
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)
            score += 10
            scoreString = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scoreString, False, align="left", font=("arial",14,"normal"))
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            closeGame("PERDIO")
            break
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    if bullet.ycor() > 255:
        bullet.hideturtle()
        position_bullet()

#turtle.done()  
            
    


