# Ping-Pong game com turtle module.

import turtle as t
import os

# Variáveis de pontuação

player_a_score = 0
player_b_score = 0

win = t.Screen()    # Criando uma janela
win.title("Ping-Pong Game") # Dando nome ao jogo.
win.bgcolor('black')    # Fornecendo cor para a HomeScreen
win.setup(width=800,height=600) # Tamanho do painel do jogo
win.tracer(0)   # Qual velocidade é o jogo.

# Criando uma raquete esquerda para o jogo

paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('red')
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

# Criando uma raquete direita para o jogo

paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.color('red')
paddle_right.penup()
paddle_right.goto(350,0)

# Criando uma bola de pong para o jogo

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5   # Configurando os pixels para o movimento da bola.
ball_dy = 1.5

# Criando uma caneta para atualizar o score

pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=('Monaco',24,"normal"))


# Movendo a raquete para esquerda usando o teclado

def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)

# Movendo a raquete para esquerda no sentido para baixo

def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)

# Movendo a raquete para direita no sentido cima

def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)

# Movendo a raquete para direita no sentido baixo

def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)

# Ligacao do teclado com o game

win.listen()
win.onkeypress(paddle_left_up,"u")
win.onkeypress(paddle_left_down,"e")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")




# Loop do jogo principal e logica

while True:
    win.update() # Este método é obrigatório para executar qualquer jogo

    # Movendo a bola
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # configurando a fronteira de ate onde pode ir

    if ball.ycor() > 290:   # Borda da raquete, direita cima
        ball.sety(290)
        ball_dy = ball_dy * -1
        
    
    if ball.ycor() < -290:  # Borda da raquete, esquerda cima
        ball.sety(-290)
        ball_dy = ball_dy * -1
        

    if ball.xcor() > 390:   # borda da raquete, largura direita
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")



    if(ball.xcor()) < -390: # borda da raquete, largura esquerda
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")


    # Lidar com as colisões

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")