import pygame 

pygame.init()
screen = pygame.display.set_mode((1000, 850))
pygame.display.set_caption("Clock")
done = False
playing = False
clock = pygame.time.Clock()

songs = ['bigears.mp3', 'noizeNOTMC.mp3', 'rickroll.mp3']
i = 0
pygame.mixer.music.load(songs[0])
font = pygame.font.Font(None, 72)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pygame.mixer.music.play()
        playing = True
    if pressed[pygame.K_DOWN]: 
        pygame.mixer.music.stop()
        playing = False
    if pressed[pygame.K_LEFT]: 
        i = (i + 2) % 3
        pygame.mixer.music.load(songs[i])
        if playing: pygame.mixer.music.play()
    if pressed[pygame.K_RIGHT]: 
        i = (i + 1) % 3
        pygame.mixer.music.load(songs[i])
        if playing: pygame.mixer.music.play()

    if playing: text = font.render("Currently playing: " + songs[i], True, (100, 100, 200))
    else: text = font.render("Currently NOT playing: " + songs[i], True, (100, 100, 200))
    screen.fill((255, 255, 255))
    screen.blit(text, (500 - text.get_width() // 2, 250 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(80)