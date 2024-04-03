import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        if x < 20: x = 20
        if y < 20: y = 20
        if x > 380: x = 380
        if y > 280: y = 280  
        screen.fill((255, 255, 255))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.circle(screen, color, (x,y), 20)
        
        pygame.display.flip()
        clock.tick(80)
