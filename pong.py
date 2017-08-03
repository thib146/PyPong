#!/usr/bin/env python
"""
Pong - Python version
thib146
"""
import time
import os, pygame, sys, random

pygame.init()  # initialise graphics interface
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Pong")
screenWidth = 400
screenHeight = 400
screen = pygame.display.set_mode([screenWidth, screenHeight], 0, 32)
background = pygame.Surface((screenWidth, screenHeight))
font = pygame.font.SysFont("monospace", 15)

pygame.key.set_repeat(1, 10)

# define the colours to use for the user interface
cBackground = (255, 255, 255)
cBlock = (0, 0, 0)
cWall = (155, 155, 155)
cPlayer1 = (0, 0, 255)
cPlayer2 = (255, 0, 0)
background.fill(cBackground)  # make background colour
player1posy = (screenHeight - 50) / 2
player2posy = (screenHeight - 50) / 2
dx = 2.5
dy = 5
score = False

scoreP1 = 0
scoreP2 = 0


def main():
    global player1posy, player2posy, scoreP1, scoreP2, score, dx, dy
    X = screenWidth / 2
    Y = screenHeight / 2
    randomizeDirection()
    screen.blit(background, [0, 0])
    while True:
        checkForEvent()
        time.sleep(0.025)
        drawScreen(X, Y, player1posy, player2posy, scoreP1, scoreP2)
        if (score == False):
            X += dx
            Y += dy
        else:
            X = screenWidth / 2
            Y = screenHeight / 2
            dx = 2.5
            dy = 5
            randomizeDirection()
            score = False
        checkBounds(X, Y)


def checkBounds(px, py):
    global dx, dy, player1posy, player2posy, scoreP1, scoreP2, score
    if (dx < 0 and px < 20 and player1posy < py < player1posy + 50) or (
                    dx > 0 and px > screenWidth - 30 and player2posy < py < player2posy + 50):
        dx = -dx  # Invert X direction
        dx *= 1.1  # Increase the speed
        dy *= 1.1
    if px < 0:
        score = True
        scoreP2 += 1
        time.sleep(0.5)
    if px > screenWidth - 10:
        score = True
        scoreP1 += 1
        time.sleep(0.5)
    if py > screenHeight - 20 or py < 10:
        dy = -dy
    if player1posy > screenHeight - 60:
        player1posy = screenHeight - 60
    if player1posy < 25:
        player1posy = 10
    if player2posy > screenHeight - 60:
        player2posy = screenHeight - 60
    if player2posy < 25:
        player2posy = 10


def drawScreen(px, py, p1y, p2y, scP1, scP2):  # draw to the screen
    screen.blit(background, [0, 0])  # set background colour

    scoreP1 = font.render("Score: " + str(scP1) + "/" + str(scP2), 1, (0, 0, 0))
    screen.blit(scoreP1, (screenWidth / 2 - 40, screenHeight - 50))

    pygame.draw.rect(screen, cWall, (0, 0, screenWidth, 10), 0)  # Top Wall
    pygame.draw.rect(screen, cWall, (0, screenHeight - 10, screenWidth, 10), 0)  # Bottom Wall

    pygame.draw.rect(screen, cBlock, (px, py, 10, 10), 0)  # Ball
    # pygame.draw.circle(screen, cBlock, (px, py), 10, 0)

    pygame.draw.rect(screen, cPlayer1, (10, p1y, 10, 50), 0)  # Player1
    pygame.draw.rect(screen, cPlayer2, (380, p2y, 10, 50), 0)  # Player2
    pygame.display.update()


def terminate(text):  # close down the program
    print (text)
    pygame.quit()  # close pygame
    sys.exit()


def checkForEvent():  # see if you need to quit
    global player1posy, player2posy
    event = pygame.event.poll()
    if scoreP1 == 10:
        terminate("Player 1 WINS !!")
    if scoreP2 == 10:
        terminate("Player 2 WINS !!")
    if event.type == pygame.QUIT:
        terminate("Closing down please wait")
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        terminate("Closing down please wait")
    if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
        player1posy -= 15
    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
        player1posy += 15
    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        player2posy -= 15
    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        player2posy += 15


def randomizeDirection():
    global dx, dy
    a = random.randrange(0, 2, 1)
    b = random.randrange(0, 2, 1)
    if a == 0:
        dx = -dx
    if b == 0:
        dy = -dy


if __name__ == '__main__':
    main()
