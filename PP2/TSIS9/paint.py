import pygame
import math

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 800))

done = False

colors = {
    "Red": (255, 0, 0),
    "White": (255, 255, 255),
    "Green": (0, 255, 0), 
    "Blue": (0, 0, 255), 
    "Black": (0, 0, 0),
    "Grey": (128, 128, 128)
}

def intersect_rect(point, rect):
    if rect[0] <= point[0] <= rect[0] + rect[2] and rect[1] <= point[1] <= rect[1] + rect[3]: return True
    else: return False
def intersect_circle(point, start, radius):
    if math.sqrt((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2) <= radius: return True
    else: return False

def Controls():
    pygame.draw.rect(screen, colors["White"], (0, 600, 600, 200))
    text = font.render("Controls:", True, colors["Black"])
    screen.blit(text, (20, 610))
    text = font.render("Colors:", True, colors["Black"])
    screen.blit(text, (20, 630))
    text = font.render("1 - Red", True, colors["Black"])
    screen.blit(text, (20, 650))
    text = font.render("2 - Green", True, colors["Black"])
    screen.blit(text, (20, 670))
    text = font.render("3 - Blue", True, colors["Black"])
    screen.blit(text, (20, 690))
    text = font.render("4 - White", True, colors["Black"])
    screen.blit(text, (20, 710))
    if mode == "Square" or True:
        if startx == -1:
            text = font.render("LMB - choose corner point", True, colors["Black"])
            screen.blit(text, (200, 630))
        else:
            text = font.render("LMB - draw Polygon", True, colors["Black"])
            screen.blit(text, (200, 630))
    text = font.render("Q - Romb", True, colors["Black"])
    screen.blit(text, (200, 670))
    text = font.render("W - Square", True, colors["Black"])
    screen.blit(text, (200, 690))
    text = font.render("E - Equilateral Triangle", True, colors["Black"])
    screen.blit(text, (200, 710))
    text = font.render("R - Right Triangle", True, colors["Black"])
    screen.blit(text, (200, 730))
    text = font.render("ENTER - Exit", True, colors["Black"])
    screen.blit(text, (20, 750))

    
    if color == "White": text = font.render("You are in mode: " + mode + " (White)", True, colors["Black"])
    else: text = font.render("You are in mode: " + mode, True, colors[color])
    screen.blit(text, (200, 750))


radius = 10
mode = "Romb"
color = "Red"
Rombs = []
squares = []
ETs = []
RTs = []

font = pygame.font.Font(None, 28)
startx = -1
starty = -1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        done = True
    if pressed[pygame.K_1]:
        color = "Red"
    if pressed[pygame.K_2]:
        color = "Green"
    if pressed[pygame.K_3]:
        color = "Blue"
    if pressed[pygame.K_4]:
        color = "White"
    if pressed[pygame.K_q]:
        mode = "Romb"
    if pressed[pygame.K_w]:
        mode = "Square"
        startx = -1
        starty = -1
    if pressed[pygame.K_e]:
        mode = "ET"
        startx = -1
        starty = -1
    if pressed[pygame.K_r]:
        mode = "RT"
        startx = -1
        starty = -1

    
    m_pressed = pygame.mouse.get_pressed()

    if m_pressed[0] and mode == "Square":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            #rectangle (x, y, dx, dy), color
            dx = abs(pos[0] - startx)
            dy = abs(pos[1] - starty)
            squares.append(((min(pos[0], startx), min(pos[1], starty), max(dx, dy), max(dx, dy)), colors[color]))
            startx = -1
            starty = -1

    if m_pressed[0] and mode == "RT":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            #([topleft, bottomleft, bottomright], color)
            x = pos[0]
            y = pos[1]
            RTs.append(([(startx, starty), (startx, y), (x, y)], colors[color]))
            startx = -1
            starty = -1
    
    if m_pressed[0] and mode == "ET":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            #([A, B, C], color)
            ETs.append(([(startx, starty), (x, y), (startx - (x - startx), y)], colors[color]))
            startx = -1
            starty = -1

    if m_pressed[0] and mode == "Romb":
        if startx == -1:
            pos = pygame.mouse.get_pos()
            startx = pos[0]
            starty = pos[1]
        else:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            #([A, B, C, D], color)
            dy = y - starty
            Rombs.append(([(startx, starty), (startx - dy / 2, starty + dy / 2), (startx, y), (startx + dy / 2, starty + dy / 2)], colors[color]))
            startx = -1
            starty = -1


    screen.fill(colors["Black"])

    for rect in squares:
        pygame.draw.rect(screen, rect[1], rect[0])
    for RT in RTs:
        pygame.draw.polygon(screen, RT[1], RT[0])
    for ET in ETs:
        pygame.draw.polygon(screen, ET[1], ET[0])
    for romb in Rombs:
        pygame.draw.polygon(screen, romb[1], romb[0])
        
    if mode == "Square":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            dx = abs(pos[0] - startx)
            dy = abs(pos[1] - starty)
            pygame.draw.rect(screen, colors[color], (min(pos[0], startx), min(pos[1], starty), max(dx, dy), max(dx, dy)))
            
    if mode == "RT":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            pygame.draw.polygon(screen, colors[color], [(startx, starty), (startx, y), (x, y)])

    if mode == "ET":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            pygame.draw.polygon(screen, colors[color], [(startx, starty), (x, y), (startx - (x - startx), y)])

    if mode == "Romb":
        if startx != -1:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            dy = y - starty
            pygame.draw.polygon(screen, colors[color], [(startx, starty), (startx - dy / 2, starty + dy / 2), (startx, y), (startx + dy / 2, starty + dy / 2)])

    Controls()

    pygame.display.flip()
    if mode == "Paint": clock.tick(200)
    else: clock.tick(60)
    
