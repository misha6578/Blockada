from pygame import *
class Settings(sprite.Sprite):
    def __init__(self, x, y, w, h, speed, img):
        super().__init__()
        self.speed = speed
        self.width = w
        self.height = h
        self.image = transform.scale(image.load(img),(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(Settings):
    def __init__(self, x, y, w, h, speed, img, side):
        Settings.__init__(self, x, y, w, h, speed, img)


        self.side = side

    def update(self):
        global side

        if self.side == "right":
            self.rect.x -= self.speed
        if self.side == "left":
            self.rect.x += self.speed
            
            
class Player(Settings):

    def r_l(self):
        global mana, img, f
        f=1
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
            mana.side = "left"
            f = 1
        if keys[K_d]:
            self.rect.x += self.speed
            f = 0
            mana.side = "right"

        if f == 1:
            self.image = transform.scale(image.load(hero_r), (self.width, self.height))
        if f == 0:
            self.image = transform.scale(image.load(hero_l), (self.width, self.height))    

    def u_d(self):
        keys = key.get_pressed()       
        if keys [K_w]:
            self.rect -= self.speed
        if keys [K_s]:
            self.rect += self.speed     
win_width = 1280
win_height = 720
window = display.set_mode((win_width, win_height))
display.set_caption("Maze_defection")
background = transform.scale(image.load("Fone.jpg"), (win_width, win_height))
window.blit(background,(0,0))
clock = time.Clock()
game = True
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS) 
    
    
   

