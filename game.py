import pygame
pygame.init()
win=pygame.display.set_mode((800,450))
pygame.display.set_caption("My first game")
bg=pygame.image.load('back2.png')
man=pygame.image.load('standing.png')
manleft=pygame.image.load('L2.png')
manleft1=pygame.image.load('L2E.png')
manright=pygame.image.load('R2.png')
manright1=pygame.image.load('R2E.png')
manright2=pygame.image.load('R2E.png')
manleft2=pygame.image.load('L2E.png')
x=350
y=360
x1=700
y1=365
x2=100
y2=365
width=20
hight=35
vel=8
motionr=False
motionl=True
motionr1=False
motionl1=True
run=True
space=False
left=False
right=False
left1=True
right1=False
left2=True
right2=False
jump=9
speed=5
speed1=8
point=0
clock=0
while run:
    n=0
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x=x-vel
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and x<740:
        x=x+vel
        right=True
        left=False
    else:
        left=False
        right=False
    if motionl:
        x1=x1-speed
        if x1<5:
            motionl=False
            motionr=True
            left1=False
            right1=True 
    if motionr:
        x1=x1+speed
        if x1>745:
            motionl=True
            motionr=False
            left1=True
            right1=False 
    if keys[pygame.K_UP]:
        space=True
    if space:
        if(jump>=-9):
            if(jump>0):
                y=y-(jump**2)*0.3
            else:
                y=y+(jump**2)*0.3
            jump-=1
        else:
            space=False
            jump=9  
    if ((x>=(x1-19)) and (x<=(x1+19))and (y>315)):
        run=False
    clock+=1
    if ((clock%60)==0):
        point+=1
        speed+=1
        speed1+=0.2
    print(point)
    win.blit(bg,(0,-135))
    if left:
        win.blit(manleft,(x,y))
    if right:
        win.blit(manright,(x,y))
    if not(left)and not(right):
        win.blit(man,(x,y))
    if right1:
        win.blit(manright1,(x1,y1))
    if left1:
        win.blit(manleft1,(x1,y1))
#second man
    if(point>=5):
        if motionl1:
            x2=x2-speed1
            if x2<5:
                motionl1=False
                motionr1=True
                left2=False
                right2=True 
        if motionr1:
            x2=x2+speed1
            if x2>745:
                motionl1=True
                motionr1=False
                left2=True
                right2=False 
        if ((x>=(x2-19)) and (x<=(x2+19))and (y>315)):
            run=False
        if right2:
            win.blit(manright2,(x2,y2))
        if left2:
            win.blit(manleft2,(x2,y2))
    pygame.display.set_caption("The hop game BY :- Malay Agrawal \n Points :- "+str(point))
    pygame.display.update()
pygame.quit()