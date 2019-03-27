import pygame
pygame.init()
height,width=600,600
screen = pygame.display.set_mode((width, height))
done = False
clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        for i in range(1,3):

            pygame.draw.line(screen,(0,0,0),(i*width/3,0),(i*width/3,height))
            pygame.draw.line(screen,(0,0,0),(0,i*height/3),(width,i*width/3))

        
        pygame.display.flip()
        clock.tick(60)

