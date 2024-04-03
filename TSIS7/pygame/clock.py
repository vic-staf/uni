import pygame
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((1000, 850))
pygame.display.set_caption("Clock")
done = False

clock = pygame.time.Clock()

clock_im = pygame.image.load("mainclock.png")
seconds_im = pygame.image.load("leftarm.png")
minute_im = pygame.image.load("rightarm.png")

pos_seconds = (475, -100)
pos_minute = (-200,-100)

pivot = (500, 425)

offset_minute = pygame.math.Vector2(0, 0)
offset_seconds = pygame.math.Vector2(-6, 0)

rect = seconds_im.get_rect()

rect.topleft = pos_seconds
print(rect.center)

def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.
    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    time = datetime.datetime.today()
    minute = time.minute
    seconds = time.second
    angle1 = seconds * 6
    angle2 = (minute * 6) + (seconds / 10)

   


    new_minute, rect1 = rotate(minute_im, angle2,pivot, offset_minute)
    new_second, rect2 = rotate(seconds_im, angle1,pivot, offset_seconds)

    screen.fill((0, 0, 0))
    screen.blit(clock_im, (-200, -120))
    screen.blit(new_second, rect2)
    screen.blit(new_minute, rect1)

    pygame.display.flip()
    clock.tick(80)





