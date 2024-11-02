import pygame as pygame
import src.Tile as Tile
import src.Snake as Snake
from src.Score import Score
from src.Apple import Apple

WIDTH, HEIGHT = 640, 480
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

map_tile_snake = ["1111111111",
                  "1000000001",
                  "1000000001",
                  "1000000001",
                  "1000000001",
                  "1000000001",
                  "1000000001",
                  "1000000001",
                  "1000000001",
                  "1111111111", ]
tile_snake_setting = {
    "0": {"color": GREEN, "name": "grond"},
    "1": {"color": BLACK, "name": "wall"},
}


def main():
    running = True
    tile_snake = Tile.create_tiles(map_tile_snake, WIDTH, HEIGHT, tile_snake_setting)
    size_tile = Tile.get_tile_size_relative_to_screen(map_tile_snake, WIDTH, HEIGHT)

    clock = pygame.time.Clock()
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    snake = Snake.Snake(pygame.Rect(size_tile, size_tile), 0, 10)
    apple = Apple(pygame.Rect((200, 200), size_tile), BLUE)

    score = Score()
    font = pygame.font.SysFont(None, 24)
    font.render('Score:', True, WHITE)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.set_rotate(270)
                elif event.key == pygame.K_s:
                    snake.set_rotate(90)
                elif event.key == pygame.K_a:
                    snake.set_rotate(180)
                elif event.key == pygame.K_d:
                    snake.set_rotate(0)
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, WIDTH, HEIGHT))
        for tile in tile_snake:
            pygame.draw.rect(screen, tile.color, tile.rect)
            if pygame.Rect.colliderect(snake.rect, tile.rect) and tile.name == "wall":
                running = False
                print("you death")
        for index in range(len(snake.tail)):
            part = snake.tail[index]
            pygame.draw.rect(screen, WHITE, pygame.Rect(part[0], part[1], snake.rect.width, snake.rect.height))
            if (pygame.Rect.colliderect(snake.rect, pygame.Rect(part[0], part[1], snake.rect.width,
                                                                snake.rect.height))) and index >8:
                running = False
                print("you death")
        if pygame.Rect.colliderect(snake.rect, apple.rect):
            score.increment(1)
            snake.add_tail()
            apple.random_spawn(64, 48, WIDTH - 128, HEIGHT - 96)
        pygame.draw.rect(screen, apple.color, apple.rect)
        score_label = font.render(str(score), True, WHITE)
        screen.blit(score_label, (20, 20))
        snake.move(FPS / 1000)
        pygame.draw.rect(screen, RED, snake.rect)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
