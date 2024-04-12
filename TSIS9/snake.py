import pygame
import random
import datetime

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))

done = False
pause = False

Red = (255, 0, 0)
Green = (0, 255, 0)
Yellow = (0, 255, 255)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)

font = pygame.font.Font(None, 28)

class Snake():
    def __init__(self):
        self.size = 1
        self.dx = 1
        self.dy = 0
        self.elements = [[100, 100]]

    def update(self, speed):
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        
        self.elements[0][0] += self.dx * speed
        self.elements[0][1] += self.dy * speed

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, Red, element, 10)

class Food():
    def __init__(self):
        self.time = datetime.datetime.today()
        self.weight = random.randint(1, 3)
        self.x = random.randint(50, 550)
        self.y = random.randint(150, 550)
    
    def draw(self):
        if self.weight == 1: pygame.draw.circle(screen, Green, (self.x, self.y), 10)
        if self.weight == 2: pygame.draw.circle(screen, Yellow, (self.x, self.y), 10)
        if self.weight == 3: pygame.draw.circle(screen, Blue, (self.x, self.y), 10)

def save_score(score):
    f = open('score_snake.txt', 'a')
    f.write(str(score) + ' ')
    f.close()

def get_high_score():
    f = open('score_snake.txt', 'r')
    s = f.read()
    a = list(map(int, s.split()))
    return max(a)

food = Food()
snake = Snake()

speed = 5
score = 0
level = 1


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if pause:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            done = True
        if pressed[pygame.K_SPACE]:
            food = Food()
            snake = Snake()

            speed = 5
            score = 0
            level = 1

            pause = False
        continue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and snake.dx:
        snake.dx = 0
        snake.dy = 1
        speed = -abs(speed)
    if pressed[pygame.K_DOWN] and snake.dx:
        snake.dx = 0
        snake.dy = 1
        speed = abs(speed)
    if pressed[pygame.K_LEFT] and snake.dy:
        snake.dx = 1
        snake.dy = 0
        speed = -abs(speed)
    if pressed[pygame.K_RIGHT] and snake.dy:
        snake.dx = 1
        snake.dy = 0
        speed = abs(speed)
    
    snake.update(speed)
    
    screen.fill(White)
    text = font.render("Score: " + str(score), True, Black)
    screen.blit(text, (10, 10))
    text = font.render("Level: " + str(level), True, Black)
    screen.blit(text, (10, 30))
    pygame.draw.rect(screen, Black, (0, 50, 600, 2))
    snake.draw()
    if (datetime.datetime.today() - food.time).seconds == 5:
        food = Food()
    food.draw()

    x = snake.elements[0][0]
    y = snake.elements[0][1]
    if x - 10 < 0 or x + 10 > 600 or y - 10 < 52 or y + 10 > 600:
        save_score(score)

        screen.fill(Black)
        death_screen = pygame.image.load('you_died.png')
        screen.blit(death_screen, (0, 0))

        text = font.render("Your score: " + str(score), True, White)
        screen.blit(text, (120, 150))

        text = font.render("High score: " + str(get_high_score()), True, White)
        screen.blit(text, (120, 200))

        text = font.render("Press SPACE to play again", True, White)
        screen.blit(text, (120, 250))
        text = font.render("Press ENTER to exit", True, White)
        screen.blit(text, (120, 300))

        pygame.display.flip()
        pause = True

    if abs(x - food.x) + abs(y - food.y) < 20:
        score += food.weight
        if score % 3 - food.weight < 0: 
            level += 1
            if speed > 0: speed += 1
            else: speed -= 1
        snake.elements.append([0, 0])
        snake.size += 1
        food = Food()

    pygame.display.flip()
    clock.tick(60)

    