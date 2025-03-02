from pygame import *
import random
from time import sleep
mixer.init()
font.init()
x = int(0)
killed = 0
finish = False
mixer.music.load('bg_music.mp3')
sound1 = mixer.Sound('shot_sound2.mp3')
mixer.music.play(-1)
window = display.set_mode((1360,768))

bg = transform.scale(image.load("bg.jpg"), (1360,768))
bg2 = transform.scale(image.load("bg.jpg"), (1360,768))
gg = transform.scale(image.load('gg.png'), (150,150))
vrag = transform.scale(image.load('vrag.png'), (100,100))
bullett = transform.scale(image.load('ataka.png'),(20,20))
bg_loss = transform.scale(image.load('chrome_9JGCfJgPkm (Средний).png'), (1360, 768))
game = True
b_number = 0
clock = time.Clock()    
my_font = font.Font("Comfortaa-Bold.ttf", 50)
lose2 = my_font.render("Вы пропустили 5 монстров,", False, (75, 150, 110))
lose3 = my_font.render(" то есть проиграли(", False, (75, 150, 110))
lose = my_font.render("you lose", False, (75, 150, 110))
win = my_font.render("you win", False, (75, 150, 110))

bullets = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self,kartinka,x ,y, speed, w, h):
        super().__init__()
        self.image = transform.scale( image.load(kartinka), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        #self.rect.width -= 20
        #self.rect.height -= 20
        self.rect.x = x
        self.rect.y = y
    def risovka(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Enemy(GameSprite):
    global x_text
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 768:
            global x
            x += 1
            self.rect.y = -25
            self.rect.x = random.randint(1, 1260)
            
class Player(GameSprite):
    def fire(self):
        bullet = Bullet('ataka.png',self.rect.x + 70, self.rect.y,5, 20, 20 )
        bullets.add(bullet)
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        elif keys[K_a]:
            self.rect.x -= self.speed
        elif keys[K_RIGHT]:
            self.rect.x += self.speed
        elif keys[K_d]:
            self.rect.x += self.speed
        elif keys[K_UP]:
            self.rect.y -= self.speed
        elif keys[K_w]:
            self.rect.y -= self.speed
        elif keys[K_DOWN]:
            self.rect.y += self.speed
        elif keys[K_s]:
            self.rect.y += self.speed
        else:
             self.risovka()

        
        
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= 5
        if self.rect.y == 0:
            self.kill()
mx = random.randint(0,1200)
mx2 = random.randint(0,1200)
mx3 = random.randint(0,1200)
mx4 = random.randint(0,1200)
mx5 = random.randint(0,1200)
monster = Enemy('vrag.png',mx,0,random.randint(2,4),100,100)
monster2 = Enemy('vrag.png',mx2,0,random.randint(2,4),100,100)
monster3 = Enemy('vrag.png', mx3,0,random.randint(2,4),100,100)
monster4 = Enemy('vrag.png',mx4,0,random.randint(2,4),100,100)
monster5 = Enemy('vrag.png',mx5,0,random.randint(2,4),100,100)
gg = Player('gg.png', 5, 500, 12, 160, 120)
monsters = sprite.Group()
monsters.add(monster)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)

finish = False

y_bg_move = 0
y_bg2_move = -768
while game:
    for ev in event.get():
        if ev.type == QUIT:
            game = False
        if ev.type == KEYUP:
            if ev.key == K_SPACE:
                gg.fire()
                sound1.play()
    if not finish:
        window.blit(bg,(0,y_bg_move))
        y_bg_move += 1
        if y_bg_move >= 768:
            y_bg_move = -768
        if y_bg2_move >= 768:
            y_bg2_move = -768
        window.blit(bg2,(0,y_bg2_move))
        y_bg2_move += 1
        x_text = my_font.render(str(x), False, (75, 150, 110))
        window.blit(x_text,(100, 100))
        bullets.update()
        bullets.draw(window)
        if sprite.groupcollide(monsters, bullets, True, True):
            killed += 1
            monsters.add(Enemy('vrag.png',random.randint(0,1200),0,random.randint(2,5),100,100))

        gg.risovka()
        gg.update()
        monsters.draw(window)
        monsters.update()
        if sprite.collide_rect(gg, monster) or sprite.collide_rect(gg, monster2) or sprite.collide_rect(gg, monster3) or sprite.collide_rect(gg, monster4) or sprite.collide_rect(gg, monster5):
            killed = str(killed)
            killed_text = my_font.render('Число монстров, которых вы убили:', False, (75, 150, 110))
            killed_number = my_font.render(killed, False, (75, 150, 110))
            window.blit(bg_loss,(0,0))
            window.blit(lose, (500, 150))
            window.blit(killed_text, (100,400))
            window.blit(killed_number, (500,500))
            finish = True
        if x >= 5:
            killed = str(killed)
            killed_text = my_font.render('Число монстров, которых вы убили:', False, (75, 150, 110))
            killed_number = my_font.render(killed, False, (75, 150, 110))
            window.blit(bg_loss,(0,0))
            window.blit(lose2, (100, 150))
            window.blit(lose3,(100,250))
            window.blit(killed_text, (100,400))
            window.blit(killed_number, (500,500))
            finish = True
        if killed == 10:
            killed = str(killed)
            killed_text = my_font.render('Число монстров, которых вы убили:', False, (75, 150, 110))
            killed_number = my_font.render(killed, False, (75, 150, 110))
            window.blit(bg_loss,(0,0))
            window.blit(win, (500, 150))
            window.blit(killed_text, (100,400))
            window.blit(killed_number, (500,500))
            finish = True               
        clock.tick(40)
        display.update()