#!/usr/bin/env python3

from pygame.locals import *
from main import end_game
from local import WINDOWS_SIZE

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