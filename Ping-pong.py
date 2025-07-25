from pygame import *


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
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
        
    def update_right(self):
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
Pl_1 = Player('racket.png', 30, 200, 50, 150, 1)
Pl_2 = Player('racket.png', 520, 200, 50, 150, 1)

game = True
while game == True:
    for ex in event.get():
        if ex.type == QUIT:
            game = False
    
    #Tenis_ball.update()
    Tenis_ball.reset()

    Pl_1.update_left()
    Pl_1.reset()

    Pl_2.update_right()
    Pl_2.reset()


    display.update()
    clock.tick()
Pl_1.hd()