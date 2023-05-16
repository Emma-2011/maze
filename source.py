import pygame
pygame.init()
sc = pygame.display.set_mode((500,500))
pygame.key.set_repeat(10)
b1=pygame.image.load("C:\\mxcmaterials\\迷宫-bg1-cdaf00ee-96ed-469c-bac7-546ed87f7e6b.png")
b2=pygame.image.load("C:\\mxcmaterials\\迷宫-bg2-f4c97173-b491-4d55-ade0-245acc1980ad.png")
b3=pygame.image.load("C:\\mxcmaterials\\迷宫-bg3-54045b64-ba59-4c67-91e4-6e71426876c6.png")
b4=pygame.image.load("C:\\mxcmaterials\\迷宫-win-7eafe69e-79ae-4217-a8de-a93a8fdd08e9.png")
bg_list=[b1,b2,b3]
sc.blit(b1,(0,0))
level=0
pygame.display.update()
class Ball:
    def __init__(self):
        self.x = 250 
        self.y = 20
    def draw_ball(self):
        pygame.draw.circle(sc,(218, 112, 214),(self.x,self.y),6)
    def move_up(self):
        self.y -=1
    def move_down(self):
        self.y +=1
    def move_left(self):
        self.x -=1
    def move_right(self):
        self.x +=1
    def reset(self):
        self.x = 250 
        self.y = 20
def detect(x,y):
    if sc.get_at((x-8,y))!=white:
        return sc.get_at((x-8,y))
    if sc.get_at((x+8,y))!=white:
        return sc.get_at((x+8,y))
    if sc.get_at((x,y-8))!=white:
        return sc.get_at((x,y-8))
    if sc.get_at((x,y+8))!=white:
        return sc.get_at((x,y+8))
ball=Ball()
green= (0,255,0)
black=(0,0,0)
white=(255,255,255)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                ball.move_up()
            if event.key==pygame.K_DOWN:
                ball.move_down() 
            if event.key==pygame.K_LEFT:
                ball.move_left()
            if event.key==pygame.K_RIGHT:
                ball.move_right()

    sc.blit(bg_list[level],(0,0))
    ball.draw_ball()
    color = detect(ball.x,ball.y)
    if color== black:
        ball.reset()
    if color ==green:
        ball.reset()
        if level<2:
            level+=1
        else:
            sc.blit(b4,(0,0))
        
            pygame.display.update()
    pygame.display.update()
input()
