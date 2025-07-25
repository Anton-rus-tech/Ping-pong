from pygame import *

font.init()

font1 = font.Font(None, 36)

class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
        
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    #метод "выстрел" (используем место игрока, чтобы создать там пулю)


back = (200, 255, 255) 
window = display.set_mode((600, 500))
window.fill(back)
clock = time.Clock()

#создание мяча и ракеток
Tenis_ball = GameSprite('tenis_ball.png', 250, 200, 100, 100, 1)
Pl_1 = Player('racket.png', 30, 200, 50, 150, 4)
Pl_2 = Player('racket.png', 520, 200, 50, 150, 4)

lose_1 = font1.render('Player 1 LOSE', True, (100, 0, 0))
lose_2 = font1.render('Player 2 LOSE', True, (100, 0, 0))

speed_x = 3
speed_y = 3

finish = False
game = True
while game == True:
    for ex in event.get():
        if ex.type == QUIT:
            game = False

    if finish == False:
        window.fill(back)###
        Pl_1.update_l()###
        Pl_2.update_r()###
        Tenis_ball.rect.x +=speed_x
        Tenis_ball.rect.y += speed_y

        if Tenis_ball.rect.y >= 450 or Tenis_ball.rect.y<=0:
            speed_y  *= -1
        if sprite.collide_rect(Pl_1,Tenis_ball) or sprite.collide_rect(Pl_2,Tenis_ball):
            speed_x *= -1
        if Tenis_ball.rect.x <0:
            finish = True
            window.blit(lose_1, (200, 200))
        if Tenis_ball.rect.x > 600:
            finish = True
            window.blit(lose_2, (200, 200))
            

    Pl_1.reset()###
    Pl_2.reset()###
    Tenis_ball.reset()###

    display.update()
    clock.tick(60)


