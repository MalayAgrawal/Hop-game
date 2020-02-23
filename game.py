import pygame
global high
pygame.init()
win=pygame.display.set_mode((800,450))
bg=pygame.image.load('back2.png')
man=pygame.image.load('standing.png')
manleft=pygame.image.load('L2.png')
manleft1=pygame.image.load('L2E.png')
manright=pygame.image.load('R2.png')
manright1=pygame.image.load('R2E.png')
manright2=pygame.image.load('R2E.png')
def game():
    global high
    music=pygame.mixer.music.load("back.mp3")
    manleft2=pygame.image.load('L2E.png')
    pygame.mixer.music.play()
    x=50
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
    lost=False
    jump=9
    speed=5
    speed1=8
    point=0
    clock=0
    while run:
        scored=pygame.font.SysFont('comicsans',35,True)
        scored2=pygame.font.SysFont('comicsans',30,False,True)
        disp_s=scored.render(str(point),1,(0,0,0))
        high_s=scored2.render(str(high),1,(0,0,0))
        n=0
        pygame.time.delay(27)
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
        pygame.display.set_caption("The Hop game BY :- Malay Agrawal")
        if ((x>=(x1-19)) and (x<=(x1+19))and (y>315)):
            music=pygame.mixer.music.load("hit.mp3")
            run=False
            lost=True
        clock+=1
        if ((clock%60)==0):
            speed+=1
            speed1+=0.2
        if ((clock%10)==0):
            point+=1
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
        if(point>=30):
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
                music=pygame.mixer.music.load("hit.mp3")
                run=False
                lost=True
            if right2:
                win.blit(manright2,(x2,y2))
            if left2:
                win.blit(manleft2,(x2,y2))
        if run:
            disp_info=scored2.render("Use right left arrow key to move right and left",1,(0,0,0))
            disp_info1=scored2.render("Use up arrow key to jump",1,(0,0,0))
            win.blit(disp_info,(10,20))
            win.blit(disp_info1,(10,43))
        if not(run):
            pygame.mixer.music.play()
            disp_info=scored2.render("Press Space to start again ",1,(0,0,0))
            disp_info1=scored2.render("Press Esc to exit",1,(0,0,0))
            win.blit(high_s,(10,66))
            win.blit(disp_s,(745,30))
            win.blit(disp_info,(10,20))
            win.blit(disp_info1,(10,43))
            pygame.display.update()
        if high<point:
            high=point
        while lost: 
            button=pygame.key.get_pressed()
            for event in pygame.event.get():
                print()
            if button[pygame.K_SPACE]:
                lost=False
                run=True
                pygame.mixer.music.stop()
                game()
                break
            if button[pygame.K_ESCAPE]:
                run=False
                pygame.quit()
                break
        win.blit(disp_s,(745,30))
        pygame.display.update()
high=0
game()