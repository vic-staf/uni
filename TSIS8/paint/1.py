import pygame
import math


pygame.init()
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Paint")
done = False

clock = pygame.time.Clock()

colors = {
    "Red": (255, 0, 0),
    "White": (255, 255, 255),
    "Green": (0, 255, 0), 
    "Blue": (0, 0, 255), 
    "Black": (0, 0, 0),
    "Grey": (128, 128, 128)
}
font = pygame.font.Font(None, 30)

def intersect_rect(point, rect):
    if rect[0] <= point[0] <= rect[0] + rect[2] and rect[1] <= point[1] <= rect[1] + rect[3]: return True
    else: return False
def intersect_circle(point, start, radius):
    if math.sqrt((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2) <= radius: return True
    else: return False

def Controls():
    pygame.draw.rect(screen,colors['White'], (0,500, 1000,250))
    text = font.render("Control panel", True, colors["White"])
    screen.blit(text, (0,480))
    text = font.render("Colors:", True, colors["Black"])
    screen.blit(text, (0,505))
    text = font.render("1 - Red", True, colors["Black"])
    screen.blit(text, (0,535))
    text = font.render("2 - Green", True, colors["Black"])
    screen.blit(text, (0,565))
    text = font.render("3 - Blue", True, colors["Black"])
    screen.blit(text, (0,595))
    text = font.render("4 - White", True, colors["Black"])
    screen.blit(text, (0,625))

    text = font.render("P - Paint", True, colors["Black"])
    screen.blit(text, (200,535))
    text = font.render("C - Circle", True, colors["Black"])
    screen.blit(text, (200,565))
    text = font.render("R - Rectangle", True, colors["Black"])
    screen.blit(text, (200,595))
    text = font.render("E - Eraser", True, colors["Black"])
    screen.blit(text, (200,625))

   
    if mode == "Eraser": text = font.render("You are in mode: " + mode, True, colors["Grey"])
    elif color == "White": text = font.render("You are in mode: " + mode + " (White)", True, colors["Black"])
    else: text = font.render("You are in mode: " + mode, True, colors[color])
    screen.blit(text, (400,625))

    text = font.render("Q - Quit", True, colors["Black"])
    screen.blit(text, (400,595))

mode = "Paint"
color = "Red"
rectangles = []
circles = []
radius = 10
points = []
paint = 0

while not done:
    pos = pygame.mouse.get_pos() 
    x = pos[0]
    y = pos[1]

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        done = True
    if pressed[pygame.K_1]:
        color = "Red"
    if pressed[pygame.K_2]:
        color = "Green"
    if pressed[pygame.K_3]:
        color = "Blue"
    if pressed[pygame.K_4]:
        color = "White"
    if pressed[pygame.K_e]:
        mode = "Eraser"
    if pressed[pygame.K_p]:
        mode = "Paint"
    if pressed[pygame.K_r]:
        mode = "Rectangle"
        startx = -1
        starty = -1
    if pressed[pygame.K_c]:
        mode = "Circle"
        startx = -1
        starty = -1


    screen.fill(colors["Black"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

        if mode == "Rectangle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                startx = x
                starty = y
            if event.type == pygame.MOUSEBUTTONUP:
                rectangles.append(((min(x, startx), min(y, starty), abs(x-startx), abs(y-starty)), colors[color]))
                startx = -1
                starty = -1
        

        if mode == "Circle":
            if event.type == pygame.MOUSEBUTTONDOWN:
                startx = x
                starty = y
            if event.type == pygame.MOUSEBUTTONUP:
                circles.append((( (x+startx)/2   , (y + starty)/2 ), (math.sqrt((startx-x)**2 + (starty - y)**2))/2, colors[color]) )
                startx = -1
                starty = -1

        if mode == "Paint":
            if event.type == pygame.MOUSEBUTTONDOWN:
                paint = 1
            if event.type == pygame.MOUSEBUTTONUP:
                paint = 0

        if mode == "Eraser":
            if event.type == pygame.MOUSEBUTTONDOWN:
                i = 0
                while i < len(rectangles):
                    if intersect_rect(pos, rectangles[i][0]):
                        rectangles.pop(i)
                    else: i += 1
                i = 0
                while i < len(circles):
                    if intersect_circle(pos, circles[i][0], circles[i][1]):
                        circles.pop(i)
                    else: i += 1
    for i in range(len(points) - 1, -1, -1):
        cur_color = points[i][0]
        R = max(0, cur_color[0] - i // 4)
        G = max(0, cur_color[1] - i // 4)
        B = max(0, cur_color[2] - i // 4)
        pygame.draw.circle(screen, (R, G, B), points[i][1], points[i][2])
    for rect in rectangles:
        pygame.draw.rect(screen, rect[1], rect[0])
    for circle in circles:
        pygame.draw.circle(screen, circle[2], circle[0], circle[1])
    
    if mode == "Paint":
        pygame.draw.circle(screen, colors[color], pos, radius)
        if paint:
            points.insert(0, (colors[color], pos, radius))
        else:
            points.insert(0, (colors[color], (-100, -100), radius))
    else:
        points.insert(0, (colors[color], (-100, -100), radius))
    if len(points) == 1024:
        points.pop(-1)

    if mode == "Rectangle" and startx != -1:
            pygame.draw.rect(screen, colors[color], (min(x, startx), min(y, starty), abs(x-startx), abs(y-starty)) )
    if mode == "Circle" and startx != -1:
            pygame.draw.circle(screen, colors[color], ( (x+startx)/2   , (y + starty)/2 ), (math.sqrt((startx-x)**2 + (starty - y)**2))/2)
    Controls()

    pygame.display.flip()
    clock.tick(160)