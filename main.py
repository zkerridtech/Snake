import pygame
import rand

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 400))

running = True

purple = (160, 32, 240)
copper = (184, 115, 51)

rect_x = 10
rect_y = 10

# keep track of snake data

snake = [(rect_x, rect_y)]
# keep track of the apple location
apple = 0, 0


def spawn_apple():
    pass


def draw_snake():
    pass


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                rect_y = rect_y + 10
            elif event.key == pygame.K_UP:
                rect_y = rect_y - 10
            elif event.key == pygame.K_LEFT:
                rect_x = rect_x - 10
            elif event.key == pygame.K_RIGHT:
                rect_x = rect_x + 10

    # validate the snake's pos (check for out of bounds & overlap)

    # check if snake's eaten the apple
    # spawn a new apple
    # grow the snake

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(purple)
    # draw the snake
    rect = (rect_x, rect_y, 20, 20)
    pygame.draw.rect(screen, copper, rect)
    # flip() the display to put your work on screen
    pygame.display.flip()
