import pygame
from random import randint
import neat
import os
import pickle
import random
import matplotlib as plt
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

local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config.txt')

config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            config_path)

def train_ai(genome, genome1, config, genomes):
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
    bvelx = random.choice([-2, 2])
    bvely = 2
    player1 = 0
    player2 = 0
    x1 = 450
    y1 = 250
    try:
        font = pygame.font.Font('ARLRDBD.ttf', 30)
    except:
        pass
    first = True
    # Main game loop begins here
    run = True
    has_g_hit = False
    has_g1_hit = False
    while run:
        try:
            last_output = output[0]
            last_output1 = output1[0]
        except:
            pass
        pygame.time.delay(1)
        # This will watch every input the user gets and tells it to python
        for event in pygame.event.get():
            # If user presses the close button on the window it stops the main game loop
            if event.type == pygame.QUIT:
                run = False
        try:
            text = font.render(str(player2), False, (0, 200, 200))
            text1 = font.render(str(player1), False, (0, 200, 200))
        except:
            pass
        # Move character
        keys = pygame.key.get_pressed()
        # Check for wall collisions
        if ballx >= 500:
            #bvelx = randint(-10, -5)
            player2 += 1
            ballx = 250
            bally = 250
            bvelx = random.choice([-2, 2])
            bvely = random.choice([-2, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2])
            genome.fitness -= 2
            if has_g1_hit:
                genome1.fitness += 2
                has_g1_hit = False
        if ballx <= 0:
            #bvelx = randint(5, 10)
            player1 += 1
            ballx = 250
            bally = 250
            bvelx = random.choice([-2, 2])
            bvely = random.choice([-2, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2])
            genome1.fitness -= 2
            if has_g_hit:
                genome.fitness += 2
                has_g_hit = False
        if bally >= 500:
            bvely = randint(-7, -4)
        if bally <= 0:
            bvely = randint(4, 7)
        # Move ball
        ballx += bvelx
        bally += bvely
        if keys[pygame.K_UP]:
            y1 -= vel + 3
        if keys[pygame.K_DOWN]:
            y1 += vel + 3
        if keys[pygame.K_w]:
            y -= vel + 3
        if keys[pygame.K_s]:
            y += vel + 3
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
            bvelx = 4
            print("collision")
            genome1.fitness += 2
            has_g1_hit = True
        if collide1 == True:
            bvelx = -4
            print("collision")
            genome.fitness += 2
            has_g_hit = True
        # Check if it is game over
        if player1 == 9 and player2 != 9:
            if has_g_hit == False:
                genome.fitness -= 3
            if has_g1_hit == False:
                genome1.fitness -= 3
            run = False
        elif player2 == 9 and player1 != 9:
            if has_g_hit == False:
                genome.fitness -= 3
            if has_g1_hit == False:
                genome1.fitness -= 3
            run = False
        elif player1 == 9 and player2 == 9:
            if has_g_hit == False:
                genome.fitness -= 3
            if has_g1_hit == False:
                genome1.fitness -= 3
            run = False
        # Update the display
        try:
            win.blit(text,(100, 50))
            win.blit(text1,(400, 50))
        except:
            pass
        
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        output = net.activate((ballx, bally, y, height,))
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        output1 = net1.activate((ballx, bally, y1, height,))
        
        if output[0] > 0:
            if y > 0:
                y -= 5
        elif output[0] < 0:
            if y < 440:
                y += 5
        
        if output1[0] > 50:
            if y1 > 0:
                y1 -= 5
        elif output1[0] < 50:
            if y1 < 440:
                y1 += 5
            
        try:
            if output1[0] == last_output:
                genome1.fitness -= 1
            if output1[0] == last_output1:
                genome1.fitness -= 1
        except:
            pass
        
        pygame.display.update()
    #pygame.quit()
    
def run(genome, config):
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
    try:
        font = pygame.font.Font('ARLRDBD.ttf', 30)
    except:
        pass
    first = True
    # Main game loop begins here
    run = True
    has_g_hit = False
    has_g1_hit = False
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
            bvely = random.choice([-2, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2])

        if ballx <= 0:
            #bvelx = randint(5, 10)
            player1 += 1
            print(player1)
            ballx = 250
            bally = 250
            bvelx = -2
            bvely = random.choice([-2, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2])

        if bally >= 500:
            bvely = randint(-7, -4)
        if bally <= 0:
            bvely = randint(4, 7)

        # Move ball
        ballx += bvelx
        bally += bvely

        if keys[pygame.K_UP]:
            y1 -= vel
        if keys[pygame.K_DOWN]:
            y1 += vel

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
            bvelx = 4
            print("collision")

        if collide1 == True:
            bvelx = -4
            print("collision")

        net = neat.nn.FeedForwardNetwork.create(genome, config)
        output = net.activate((ballx, bally, y,))

        if output[0] > 50:
            y -= 5
        elif output[0] < 50:
            y += 5

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

def eval_genomes(genomes, config):
    global fitness_values
    fitness_values = []
    genms = []
    
    for i, (genome_id, genome) in enumerate(genomes):
        genome.fitness = 0
        genms.append(genome)
        
    tested = []
        
    for i in range(0, len(genms)):
        if genms[i] in tested:
            continue
        genome = genms[i-1]
        genome1 = genms[i]
        fitness_values.append(genome.fitness)
        fitness_values.append(genome1.fitness)
        tested.append(genome)
        tested.append(genome1)
        
    train_ai(genome, genome1, config, genomes)
                
def run_neat(config):
    # HOW TO LOAD A CHECKPOINT!!!
    # --------------------------------------------------------------
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-599')
    # comment out th p.neat.Population(config) line below
    # --------------------------------------------------------------
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(50))
    winner = p.run(eval_genomes, 10000)
    with open('winner.pkl', 'wb') as f:
        pickle.dump(winner, f)
    
if __name__ == '__main__':
    run_neat(config)
    #with open('winner.pkl', 'rb') as f:
    #    winner = pickle.load(f)
    #run(winner, config)
