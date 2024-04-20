import pygame
from pygame.locals import *
from sys import exit


pygame.init()
pygame.display.set_caption("Snake 🐍")

# locals 
WINDOWS_SIZE = (1080, 720)

clock = pygame.time.Clock() 
screen = pygame.display.set_mode(WINDOWS_SIZE)


def end_game():
    pygame.quit()
    exit()


def move(snake, key, direction, SPEED):

    if (key[K_UP] or key[K_w]) and direction[0]:
        direction = [0, -SPEED]
    elif (key[K_DOWN] or key[K_s]) and direction[0]:
        direction = [0, SPEED]
    elif (key[K_LEFT] or key[K_a]) and direction[1]:
        direction = [-SPEED, 0]
    elif (key[K_RIGHT] or key[K_d]) and direction[1]:
        direction = [SPEED, 0]

    if snake.bottom > WINDOWS_SIZE[1] or snake.top < 0 or snake.left < 0 or snake.right > WINDOWS_SIZE[0]:
        end_game() 

    snake.move_ip(direction)
    
    return direction

if __name__ == "__main__":
    head = Rect(400, 300, 20, 20)

    SPEED = 20
    DIRECTION = [SPEED, 0]
    
    while True:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                end_game()
        
        DIRECTION = move(head, 
                         pygame.key.get_pressed(), 
                         DIRECTION, 
                         SPEED)

        pygame.draw.rect(screen, (255, 255, 255), head)
        pygame.display.update()
        clock.tick(10)
        