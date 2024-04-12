import pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 600))

done = False
pause = False

Red = (255, 0, 0)
White = (255, 255, 255)
Black = (0, 0, 0)

street = pygame.image.load('street.png')
font = pygame.font.Font(None, 28)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(25, 350), y)
    
    def update(self, speed):
        self.rect = self.rect.move(0, speed + 2)
        if self.rect.top > 600:
            self.rect.topleft = (random.randint(25, 350), -50)

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 500)
    
    def update(self, speed):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] and self.rect.left > 25:
            self.rect = self.rect.move(-5, 0)
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < 375:
            self.rect = self.rect.move(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, start, image):
        super().__init__()
        self.start = start
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(25, 350), start)

    def update(self, speed):
        self.rect = self.rect.move(0, speed)
        if self.rect.top > 600:
            self.rect.topleft = (random.randint(25, 350), self.start)

def save_score(score):
    f = open('score.txt', 'a')
    f.write(str(score) + ' ')
    f.close()

def get_high_score():
    f = open('score.txt', 'r')
    s = f.read()
    a = list(map(int, s.split()))
    return max(a)

P = Player() 
E1 = Enemy(-400)
E2 = Enemy(-100)
coin = Coin(-500, 'silver_coin.png')
coin2 = Coin(-1000, 'coin.png')

coins = pygame.sprite.Group()
coins.add(coin)
silver_coins = pygame.sprite.Group()
silver_coins.add(coin2)
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_entities = pygame.sprite.Group()
all_entities.add(P)
all_entities.add(E1)
all_entities.add(E2)
all_entities.add(coin)
all_entities.add(coin2)

score = 0
speed = 5

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if pause:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            done = True
        if pressed[pygame.K_SPACE]:
            P = Player() 
            E1 = Enemy(-400)
            E2 = Enemy(-100)
            coin = Coin(-500, 'silver_coin.png')
            coin2 = Coin(-1000, 'coin.png')

            coins = pygame.sprite.Group()
            coins.add(coin)
            silver_coins = pygame.sprite.Group()
            silver_coins.add(coin2)
            enemies = pygame.sprite.Group()
            enemies.add(E1)
            enemies.add(E2)
            all_entities = pygame.sprite.Group()
            all_entities.add(P)
            all_entities.add(E1)
            all_entities.add(E2)
            all_entities.add(coin)
            all_entities.add(coin2)

            score = 0
            speed = 5

            pause = False
        continue

    screen.fill(White)
    screen.blit(street, (0, 0))
    
    for entity in all_entities:
        entity.update(speed)
        screen.blit(entity.image, entity.rect)

    text = font.render(str(score), True, Black)
    screen.blit(text, (375, 10))

    if pygame.sprite.spritecollideany(P, enemies):
        save_score(score)

        screen.fill(Black)
        for entity in all_entities:
            entity.kill()

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

    if pygame.sprite.spritecollideany(P, coins):
        score += 1
        coin.rect.topleft = (random.randint(25, 350), -500)
        if score % 3 == 0:
            speed += 1
    
    if pygame.sprite.spritecollideany(P, silver_coins):
        score += 3
        coin2.rect.topleft = (random.randint(25, 350), -1000)
        speed += 1

    pygame.display.flip()
    clock.tick(60)