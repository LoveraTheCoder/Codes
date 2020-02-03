import pygame, sys
from pygame.locals import *
from Paddle import *
from Ball import *
from Scorer import *
from random import randint

#Start Pygame
pygame.init()
pygame.font.init()
running = True
limit = 1

#Variables.
SCREEN_WIDTH = 780
SCREEN_HEIGHT = 720
FRAMERATE = 60
BG = pygame.image.load("assets/pongBG.png")
FONT = pygame.font.Font("assets/munro.ttf", 30)

#Create screen, clock, and name window.
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('PONG')
clock = pygame.time.Clock()

# Create the scorer
scorer = Score()

# Create the Paddles(x,y,length,width,speed,playernumber).
paddle2 = Paddle(20, 10, 100, 20, 10, 2)
paddle1 = Paddle(740, 10, 100, 20, 10, 1)

# Spawn the Ball(x, y, xspeed, yspeed, size) at a random speed and direction.
randomx = randint(2,3)
randomy = randint(3,5)
if(randint(0,1) == 1):
    randomx = -randomx
if(randint(0,1) == 1):
    randomy = -randomy
pongball = Ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, randomx, randomy, 20)

# Draw a padle on the screen.
def drawPaddle(x, y, length, width):
    pygame.draw.rect(DISPLAYSURF, (255,255,255), (x,y,length,width))

# Dibujar la bola
def drawBall(x, y, size):
    pygame.draw.rect(DISPLAYSURF, (255,255,255), (x,y,size,size))

# bucle del juego
while True:
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #verificando variables
        k = pygame.key.get_pressed()
        paddle1.move(paddle1.ypos, k, paddle1.number)
        paddle2.move(paddle2.ypos, k, paddle2.number)
        pongball.move(pongball.xpos, pongball.ypos, pongball.xspeed, pongball.yspeed, paddle2, paddle1)
        
        # Dibujar pantalla
        DISPLAYSURF.blit(BG, (0,0))
        
        # Draw ball and paddles
        drawBall(pongball.xpos, pongball.ypos, pongball.size)
        drawPaddle(paddle1.xpos, paddle1.ypos, paddle1.width, paddle1.length)
        drawPaddle(paddle2.xpos, paddle2.ypos, paddle2.width, paddle2.length)

        # Check for a point
        scorer.checkPoint(pongball.xpos, pongball, SCREEN_WIDTH, SCREEN_HEIGHT, FRAMERATE)
        scorer.printScore(scorer.player1score, scorer.player2score)
        running = scorer.checkWin(scorer.player1score, scorer.player2score, limit)

        # Update display and tick clock.
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FRAMERATE)

    # Que salga juego terminado 
    while not running:
        
        
        if(scorer.player1score == limit):
            string = "GAME OVER."
            winText = FONT.render(string, True, (255,255,255))
            DISPLAYSURF.blit(winText, (100,200))
            pygame.display.update()
            
        else:
            string = "GAME OVER."
            winText = FONT.render(string, True, (255,255,255))
            DISPLAYSURF.blit(winText, (500,200))
            pygame.display.update()
        

        # Que la pantalla se refresque cada vez que haya movimiento
        
        pygame.display.flip()
        clock.tick(FRAMERATE)



        
