import pygame,random

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

WHITE = (255,255,255)
GREEN = (0,200,0)
RED = (255,0,0)
BLACK = (0,0,0)

font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 60)

block = 20

def reset_game():
    snake = [(300,300),(280,300),(260,300)]
    dx, dy = 20, 0
    food = (random.randrange(0,WIDTH, block), random.randrange(0, HEIGHT,block))
    score = 0
    return snake, dx, dy, food, score


def draw_game_over(score):
    screen.fill(BLACK)

    game_over_text = big_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)
    retry_text = font.render("Press R to Try Again", True, WHITE)
    quit_text = font.render("Press Q to Quit", True, WHITE)

    screen.blit(game_over_text, (WIDTH//2 - 140, HEIGHT//2 - 80))
    screen.blit(score_text, (WIDTH//2 - 80, HEIGHT//2 - 20))
    screen.blit(retry_text, (WIDTH//2 - 150, HEIGHT//2 + 20))
    screen.blit(quit_text, (WIDTH//2 - 130, HEIGHT//2 + 60))

    pygame.display.update()

snake, dx, dy, food, score = reset_game()

running = True
game_over = False

while running:

    if game_over:
        draw_game_over(score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    snake, dx, dy, food, score = reset_game()
                    game_over = False
                elif event.key == pygame.K_q:
                    running = False
        continue
     
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running: False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx,dy = 0,-block
            elif event.key == pygame.K_DOWN and dy == 0:
                dx,dy = 0, block
            elif event.key == pygame.K_LEFT and dx == 0:
                dx,dy = -block, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx,dy = block, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    if head == food:
        food = (random.randrange(0,WIDTH, block), random.randrange(0, HEIGHT,block))
        score += 1
    else:
        snake.pop()


    if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]):
        game_over = True

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], block, block))

    pygame.draw.rect(screen, RED, (*food,block,block))

    text = font.render(f"score: {score}", True, WHITE)
    screen.blit(text,(10,10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()