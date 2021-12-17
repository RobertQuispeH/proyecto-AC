import turtle, math, random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("programa Robert")

wn.bgpic("fondo2.gif")
turtle.register_shape("drac2.gif")
turtle.register_shape("llama_opt.gif")
turtle.register_shape("llama1_opt.gif")
turtle.register_shape("rojodr_opt.gif")

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
score2 = 0
score_pen2 = turtle.Turtle()
score_pen2.speed(0)
score_pen2.color("white")
scoreString2 = " Score2: %s" %score2
scoreString = "Score1: %s" %score + scoreString2 
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

player2 = turtle.Turtle()
player2.color("red")
player2.shape("rojodr_opt.gif")
player2.penup()
player2.speed(0)
player2.setposition(0, 250)
player2.setheading(90)

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("llama_opt.gif")
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

bullet2 = turtle.Turtle()
bullet2.color("yellow")
bullet2.shape("llama1_opt.gif")
bullet2.penup()
bullet2.speed(0)
bullet2.setheading(90)
bullet2.hideturtle()
xbull2 = player2.xcor() - 10
ybull2 = player2.ycor() - 50
bullet2.setposition(xbull2,ybull2)
bullet2.showturtle()



def move_left(player):
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_leftRed():
    move_left(player2)
def move_leftBlue():
    move_left(player)
    
def move_right(player):
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    
def move_rightRed():
    move_right(player2)
def move_rightBlue():
    move_right(player)

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
    
def position_bullet2():
    xbull2 = player2.xcor() - 10
    ybull2 = player2.ycor() - 50
    bullet2.setposition(xbull2,ybull2)
    bullet2.showturtle()
def interaccion():
    global bulletstate
    global score
    global score2
    global player
    global player2
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        y2 = bullet2.ycor()
        y2 -= bulletspeed
        bullet.sety(y)
        bullet2.sety(y2)
    if isCollision(player,bullet2):
        bullet2.hideturtle()
        position_bullet2()
        score2 += 10
        scoreString2 = " Score2: %s" %score2
        scoreString = "Score1: %s" %score + scoreString2 
        score_pen.clear()
        score_pen.write(scoreString, False, align="left", font=("arial",14,"normal"))
    if isCollision(player2,bullet):
        bullet.hideturtle()
        position_bullet2()
        score += 10
        scoreString2 = " Score2: %s" %score2
        scoreString = "Score1: %s" %score +scoreString2 
        score_pen.clear()
        score_pen.write(scoreString, False, align="left", font=("arial",14,"normal"))
    if bullet.ycor() > 255:
        bullet.hideturtle()
        position_bullet()
    if bullet2.ycor() < -255:
        bullet2.hideturtle()
        position_bullet2() 


