import pygame
pygame.init()
height,width=600,600
a=[False]*9
p=[(100,100),(300,100),(500,100),(100,300),(300,300),(500,300),(100,500),(300,500),(500,500)]
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
def board():
    for i in range(1,3):
         pygame.draw.line(screen,(0,0,0),(i*width/3,0),(i*width/3,height))
         pygame.draw.line(screen,(0,0,0),(0,i*height/3),(width,i*width/3))
def update():
    for i in range(9):
        if a[i]:
            pygame.draw.circle(screen,(255,0,0),p[i],50)
def update1():
    if pygame.mouse.get_pos()[0]<200 and pygame.mouse.get_pos()[1]<200:
        a[0]=True
    if 201<= pygame.mouse.get_pos()[0]<400 and pygame.mouse.get_pos()[1]<200:
        a[1]=True
    if 401<=pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[1]<200:
        a[2]=True
    if pygame.mouse.get_pos()[0]<200 and 201<=pygame.mouse.get_pos()[1]<400:
        a[3]=True
    if 201<=pygame.mouse.get_pos()[0]<400 and 201<=pygame.mouse.get_pos()[1]<400:
        a[4]=True
    if 401<=pygame.mouse.get_pos()[0] and 201<=pygame.mouse.get_pos()[1]<400:
        a[5]=True
    if pygame.mouse.get_pos()[0]<200 and 401<=pygame.mouse.get_pos()[1]:
        a[6]=True
    if 201<=pygame.mouse.get_pos()[0]<400 and 401<=pygame.mouse.get_pos()[1]:
        a[7]=True
    if 401<=pygame.mouse.get_pos()[0] and 401<=pygame.mouse.get_pos()[1]:
        a[8]=True

def loop1(done):
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
                    if event.type==pygame.MOUSEBUTTONDOWN:
                      update1()
            screen.fill((255, 255, 255))
            board()
            update()
            pygame.display.flip()
            clock.tick(60)
loop1(False)
pygame.quit()
quit()
