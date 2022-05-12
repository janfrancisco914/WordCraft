import pygame
pygame.init()

SCREEN_WIDTH = 400
SCREE_HEIGHT = 690
black =     (0, 0, 0)
gray =      (80, 80 , 80)
white =     (255, 255, 255)
lightBlue = (100, 130, 255)
lightGray = (120, 120, 120)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREE_HEIGHT))
pygame.display.set_caption("WordCraft")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Background color
    screen.fill(white)

    # Back button
    pygame.draw.line(screen, black, (30, 20), (20, 30), 6)
    pygame.draw.line(screen, black, (20, 30), (30, 40), 6)

    # Input circle
    pygame.draw.circle(screen, lightBlue, (200, 540), 115)

    # HInt circle
    pygame.draw.circle(screen, gray, (100, 370), 23)

    # Shuffle circle
    pygame.draw.circle(screen, gray, (300, 370), 23)

    # Boxes where answer is displayed
    yBoxes = 280
    pygame.draw.rect(screen, lightGray, (30, yBoxes, 40, 40))
    pygame.draw.rect(screen, lightGray, (80, yBoxes, 40, 40))
    pygame.draw.rect(screen, lightGray, (130, yBoxes, 40, 40))
    pygame.draw.rect(screen, lightGray, (180, yBoxes, 40, 40))
    pygame.draw.rect(screen, lightGray, (230, yBoxes, 40, 40))
    pygame.draw.rect(screen, lightGray, (280, yBoxes, 40, 40))
    pygame.draw.rect(screen, lightGray, (330, yBoxes, 40, 40))
    
    pygame.display.update()

pygame.quit()
