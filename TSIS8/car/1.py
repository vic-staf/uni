import pygame
import random


pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Car racing")
done = False

clock = pygame.time.Clock()

done = False
pause = False

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

street = pygame.image.load('street.png')
font = pygame.font.Font(None, 30)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(25,360),y)

    def update(self, speed):
        self.rect = self.rect.move(0,speed)
        if self.rect.top > 1000:
            self.rect.topleft = (random.randint(25,360), -50)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (200,300)

    def update(self, speed):
        press = pygame.key.get_pressed()
        if press[pygame.K_LEFT]:
            self.rect = self.rect.move(-speed,0)
        if press[pygame.K_RIGHT]:
            self.rect = self.rect.move(speed,0)

        if press[pygame.K_UP]:
            self.rect = self.rect.move(0,-speed)
        if press[pygame.K_DOWN]:
            self.rect = self.rect.move(0,speed)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 400:
            self.rect.right = 400

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(50,350), -50)
    def update(self, speed):
        self.rect = self.rect.move(0,speed)
        if self.rect.top > 1000:
            self.rect.topleft = (random.randint(50,350), -50)

P = Player()
coin = Coin()
E1 = Enemy(-100)
E2 = Enemy(-400)

coins = pygame.sprite.Group()
coins.add(coin)

enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)

all = pygame.sprite.Group()
all.add(P)
all.add(E1)
all.add(E2)
all.add(coin)

def savescore(score):
    f = open('score.txt', 'a')
    f.write(str(score)+ ' ')
    f.close()

def highscore():
    f = open('score.txt', 'r')
    s = f.read()
    a = list(map(int, s.split()))
    return max(a)

score = 0
speed = 4

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
    
    if pause:
        
        press = pygame.key.get_pressed()

        if press[pygame.K_RETURN] :
            done = True

        if press[pygame.K_SPACE]:
            P = Player() 
            E1 = Enemy(-400)
            E2 = Enemy(-100)
            coin = Coin()

            coins = pygame.sprite.Group()
            coins.add(coin)
            enemies = pygame.sprite.Group()
            enemies.add(E1)
            enemies.add(E2)
            all = pygame.sprite.Group()
            all.add(P)
            all.add(E1)
            all.add(E2)
            all.add(coin)

            score = 0
            speed = 4

            pause = False
        
        continue

    
    screen.fill(white)
    screen.blit(street, (0,0))

    for a in all:
        a.update(speed)
        screen.blit(a.image, a.rect)

   
    
    if pygame.sprite.spritecollideany(P, enemies):
        screen.fill(black)
        savescore(score)

        deathscreen = pygame.image.load('you_died.png')
        screen.blit(deathscreen, (-150,-50))
        text = font.render("Your score: " + str(score), True, white)
        screen.blit(text, (140,400))

        text = font.render("High score: " + str(highscore()), True, white)
        screen.blit(text, (140,450))

        text = font.render("Press SPACE to try again ", True, white)
        screen.blit(text, (90,500))

        pause = True
        

    if pygame.sprite.spritecollideany(P, coins):
        score += 1
        coin.rect.topleft = (random.randint(15,575), -50)
        if score % 4 == 0 and score != 0:
            speed += 1 
        
    scorevis = font.render(str(score), True, black)
    screen.blit(scorevis, (0,0))

    

    if pygame.sprite.spritecollideany(coin, enemies):
        coin.rect.topleft = (random.randint(15,575), -50)
    
    

    pygame.display.flip()
    clock.tick(80)