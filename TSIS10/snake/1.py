import pygame
import random
import datetime
import time
from config import load_config
import psycopg2

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))

done = False
pause = False
dead = False

Red = (255, 0, 0)
Green = (0, 255, 0)
Yellow = (0, 255, 255)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)

font = pygame.font.Font(None, 28)
font2 = pygame.font.Font(None, 16)

class Snake():
    def __init__(self, size = 1):
        self.size = size
        self.dx = 1
        self.dy = 0
        self.elements = [[100, 100] for i in range(size)]

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

def insert(name, score = 0):

    sql = """INSERT INTO snake(name, score)
             VALUES(%s, %s) RETURNING id;"""
    
    id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (name, score,))
                sql = "INSERT INTO snake_hs(name, score) VALUES(%s, %s) RETURNING id;"
                cur.execute(sql, (name, score))

                # get the generated id back                
                rows = cur.fetchone()
                if rows:
                    id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return id

def update(name, score):
    """ Update score of player """
    
    updated_row_count = 0

    sql = """ UPDATE snake
                SET score = %s
                WHERE name = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (score, name))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

def getscore(name):
    """ Retrieve data from the snake table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT score FROM snake WHERE name = %s", (name,))
                rows = cur.fetchall()

                for row in rows:
                    print(row)
                if cur.rowcount == 0:
                    return -1
                else: return int(rows[0][0])
                print("The number of parts: ", cur.rowcount)
                for row in rows:
                    print('\t', *row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get():
    """ Retrieve data from the snake table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name, score FROM snake_hs ORDER BY score")
                rows = cur.fetchall()

                return rows

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
def get_hs(name):
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT score FROM snake_hs WHERE name = %s", (name,))
                rows = cur.fetchall()

                if cur.rowcount == 0:
                    return -1
                else: return int(rows[0][0])

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_hs(name, score):
    """ Update score of player """
    
    updated_row_count = 0

    sql = """ UPDATE snake_hs
                SET score = %s
                WHERE name = %s"""
    
    config = load_config()
    
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                
                # execute the UPDATE statement
                cur.execute(sql, (score, name))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

def save_score(score):
    print(get_hs(name))
    if get_hs(name) < score: update_hs(name, score)

def get_high_score():
    rows = get()
    return rows

speed = 5
score = 0
level = 1

name = input("Enter you name: ")
if getscore(name) == -1:
    insert(name)
else:
    score = getscore(name)
    speed += score // 3
    level += score // 3

print(score)
food = Food()
snake = Snake(score // 3 + 1)

time.sleep(2)

while not done:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and pressed[pygame.K_ESCAPE]:
            pause = True
            screen.fill(Black)
            text = font.render("Your score: " + str(score), True, White)
            screen.blit(text, (120, 150))
            text = font.render("Press S to save current state", True, White)
            screen.blit(text, (120, 200))
            text = font.render("Press ENTER to exit", True, White)
            screen.blit(text, (120, 250))
            pygame.display.flip()


    if pause:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            pause = False
        if pressed[pygame.K_s]:
            update(name, score)
        if pressed[pygame.K_RETURN]:
            done = True
        continue
    if dead:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            done = True
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
        update(name, 0)

        screen.fill(Black)
        death_screen = pygame.image.load('you_died.png')
        screen.blit(death_screen, (0, 0))

        text = font.render("Your score: " + str(score), True, White)
        screen.blit(text, (120, 150))

        text = font.render("High scores: ", True, White)
        screen.blit(text, (120, 250))

        text = font.render("Press ENTER to exit", True, White)
        screen.blit(text, (120, 200))
        rows = get_high_score()
        for i in range(len(rows)):
            text = font2.render(rows[i][0], True, White)
            screen.blit(text, (120, 270 + i * 20))
            text = font2.render(str(rows[i][1]), True, White)
            screen.blit(text, (250, 270 + i * 20))
            if i == 9: 
                break

        pygame.display.flip()
        dead = True

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

    