from pygame import *



class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, player_speed_x,player_speed_y,player_size_x,player_size_y):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)
        
        
        

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# clase del jugador principal
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed_y
            
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed_y

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y



clock = time.Clock()
FPS = 40
window_width = 700
window_height = 500
window = display.set_mode((window_width,window_height))
display.set_caption("Pong")
background = transform.scale(image.load("background-1634817_1280.png"),(window_width,window_height))


player1 = Player("Icon76@2x copy.png", 100,200,0,5,20,100)
player2 = Player2("Icon76@2x copy.png", 550,200,0,5,20,100)
bola = Ball("Ball.png",350,250,5,5,15,15)

run = True
while run:

    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background,(0,0))
    
    player1.update()
    player1.reset()

    player2.update()
    player2.reset()

    bola.update()
    bola.reset()


    display.update()