import pygame
from random import randint
pygame.init()

# Creates a blank window with the dimentions of 500 by 500.
win = pygame.display.set_mode((500, 500))
# Sets the title of the window to Pong
pygame.display.set_caption("Pong")

fps = pygame.time.Clock()
x = 25
y = 250
ballx = 250
bally = 250
balls = 10
width = 20
height = 60
vel = 5
bvelx = 2
bvely = 2
player1 = 0
player2 = 0
x1 = 450
y1 = 250
font = pygame.font.Font('ARLRDBD.ttf', 30)
first = True


# Main game loop begins here
run = True
while run:
    pygame.time.delay(25)
    # This will watch every input the user gets and tells it to python
    for event in pygame.event.get():
        # If user presses the close button on the window it stops the main game loop
        if event.type == pygame.QUIT:
            run = False

    text = font.render(str(player2), False, (0, 200, 200))
    text1 = font.render(str(player1), False, (0, 200, 200))
    # Move character
    keys = pygame.key.get_pressed()

    # Check for wall collisions
    if ballx >= 500:
        #bvelx = randint(-10, -5)
        player2 += 1
        print(player2)
        ballx = 250
        bally = 250
        bvelx = 2
        bvely = 2

    if ballx <= 0:
        #bvelx = randint(5, 10)
        player1 += 1
        print(player1)
        ballx = 250
        bally = 250
        bvelx = -2
        bvely = -2

    if bally >= 500:
        bvely = randint(-7, -4)
    if bally <= 0:
        bvely = randint(4, 7)

    # Move ball
    ballx += bvelx
    bally += bvely

    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))

    # Draw character by defining the window (win) then defining the r,g,b color (255, 0, 0 or red) then the position (x and y) and the size (width and height)
    paddle1 = pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    paddle2 = pygame.draw.rect(win, (255, 0, 0), (x1, y1, width, height))
    # Draw Ball to screen
    ball = pygame.draw.circle(win, (0, 0, 255), (ballx, bally), balls)

    # Check for paddle collisions (ball)
    collide = paddle1.colliderect(ball)
    collide1 = paddle2.colliderect(ball)

    if collide == True:
        bvelx = randint(4, 7)
        print("collision")

    if collide1 == True:
        bvelx = randint(-7, -4)
        print("collision")
    
    if bally > y1:
        y1 += vel

    elif bally < y1:
        y1 -= vel

    # Check if it is game over
    if player1 == 9 and player2 != 9:
        run = False
        vic = font.render("Player 1 Wins!", False, (245, 9, 218))
        win.blit(vic, (100, 250))
        if run == True:
            pygame.time.delay(999999)

    elif player2 == 9 and player1 != 9:
        run = False
        vic = font.render("Player 2 Wins!", False, (245, 9, 218))
        win.blit(vic, (100, 250))
        if run == True:
            pygame.time.delay(999999)

    elif player1 == 9 and player2 == 9:
        run = False
        vic = font.render("Draw!", False, (245, 9, 218))
        win.blit(vic, (200, 250))
        if run == True:
            pygame.time.delay(999999)

    # Update the display
    win.blit(text,(100, 50))
    win.blit(text1,(400, 50))
    pygame.display.update()

pygame.quit()
