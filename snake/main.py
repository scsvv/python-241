import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()
pygame.display.set_caption("Snake 🐍")

# locals 
WINDOWS_SIZE = (1080, 720)

clock = pygame.time.Clock() 
screen = pygame.display.set_mode(WINDOWS_SIZE)
font = pygame.font.SysFont(None, 16)


def end_game():
        text = font.render(f"GAME OVER", True, (255, 255, 255))
        text_rect = text.get_rect(center=(540, 360))
        screen.blit(text, text_rect)

def exit_from_game():
    pygame.quit()
    exit()

def display_score(score):
    text = font.render(f"Score {score}", True, (255, 255, 255))
    text_rect = text.get_rect(left=5, top=5)
    screen.blit(text, text_rect)


def load_img(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (20, 20))
    rect = image.get_rect(center=(x, y))
    transpet = image.get_at((0,0))
    image.set_colorkey(transpet)

    return image, rect


def move(snake, key, direction, SPEED):

    if (key[K_UP] or key[K_w]) and direction[0]:
        direction = [0, -SPEED]
    elif (key[K_DOWN] or key[K_s]) and direction[0]:
        direction = [0, SPEED]
    elif (key[K_LEFT] or key[K_a]) and direction[1]:
        direction = [-SPEED, 0]
    elif (key[K_RIGHT] or key[K_d]) and direction[1]:
        direction = [SPEED, 0]

    if snake[0].bottom > WINDOWS_SIZE[1] or snake[0].top < 0 or snake[0].left < 0 or snake[0].right > WINDOWS_SIZE[0]:
        end_game() 

    
    for i in range(len(snake)-1, 0, -1):
        snake[i].x = snake[i-1].x
        snake[i].y = snake[i-1].y

    snake[0].move_ip(direction)
    
    return direction


def pickup(apple, snake, score):
    if snake[0].colliderect(apple):
        apple.x = randint(10, 1050)
        apple.x = randint(10, 700)
        snake.append(snake[1].copy())
        score += 10
    return score


def game_process(
        head, 
        snake,
        apple, 
        score, 
        keys,
        direction,
        speed
):
    direction = move(snake, 
            keys,
            direction, 
            speed)
    
    score = pickup(
        apple, snake, score)
    
    display_score(score)

    return direction, score


def is_play(snake):
    for shape in snake[1:]:
        if snake[0].colliderect(shape):
            return False
    return True


if __name__ == "__main__":
    SPEED = 20
    DIRECTION = [SPEED, 0]
    game_score = 0

    head_image, head_rect = load_img('./snake/img/head.png', 400, 300)
    body_image, body_rect = load_img('./snake/img/body.png', 380, 300)
    apple_image, apple_rect = load_img('./snake/img/apple.png', 300, 200)

    snake = [head_rect, body_rect]
    
    while True:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
               exit_from_game()
        
        if is_play(snake):
            DIRECTION, game_score = game_process(
                head_rect, 
                snake,
                apple_rect, 
                game_score,
                pygame.key.get_pressed(),
                DIRECTION,
                SPEED
        )    
            screen.blit(head_image, head_rect)
            screen.blit(apple_image, apple_rect)
            for body in snake[1:]:
                screen.blit(body_image, body)
        else: 
            end_game()

        pygame.display.update()
        clock.tick(10)
        