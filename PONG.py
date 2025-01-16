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
        if sprite.collide_rect(self,player1):
            self.speed_x *= -1
            self.speed_y *= 1
            self.speed_x += 0.5
            self.speed_y += 0.5
        if sprite.collide_rect(self,player2):
            self.speed_x *= -1
            self.speed_y *= 1
            self.speed_x += -0.5
            self.speed_y += 1
        if self.rect.y < 0:
            self.speed_y *= -1
            self.speed_x *= 1
        if self.rect.y > 475:
            self.speed_y *= -1
            self.speed_x *= 1

        global finish
        if self.rect.x > 700:
            
            finish = True
            print("",self.rect.x)
        if self.rect.x < 0:
            
            finish = True


        



clock = time.Clock()
FPS = 40
window_width = 700
window_height = 500
window = display.set_mode((window_width,window_height))
display.set_caption("Pong")
background = transform.scale(image.load("background-1634817_1280.png"),(window_width,window_height))

puntosP1 = 0
puntosP2 = 0

player1 = Player("Icon76@2x copy.png", 100,200,0,8,25,100)
player2 = Player2("Icon76@2x copy.png", 550,200,0,8,25,100)
bola = Ball("Ball.png",350,250,3,3,15,15)

font.init()
font1 = font.SysFont("Arial",50) 
font2 = font.SysFont("Arial",50) 
font3 = font.SysFont("Arial",40)
font4 = font.SysFont("Arial",40)

finish = False
run = True
while run:

    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish == False:
        window.blit(background,(0,0))
        
        player1.update()
        player1.reset()

        player2.update()
        player2.reset()

        bola.update()
        bola.reset()
    
        puntosp1 = font3.render("PuntosP1: "+str(puntosP1),1,(0,0,0))
        puntosp2 = font4.render("PuntosP2: "+str(puntosP2),1,(0,0,0))
        
        window.blit(puntosp1,(0,0))
        window.blit(puntosp2,(0,40))
        
    elif finish == True:
        
        if bola.rect.x > 700:
            winP1 = font1.render("Ganaste Player 1",1,(255,255,0))
            window.blit(winP1,(230,250))
            puntosP1 += 1
        if bola.rect.x < 0:
            winP2 = font2.render("Ganaste Player 2",1,(255,255,0))
            window.blit(winP2,(230,250))
            puntosP2 += 1
        display.update()
        
        print("Vamos a reiniciar")
        time.wait(2000)
            
        player1 = Player("Icon76@2x copy.png", 100,200,0,8,25,100)
        player2 = Player2("Icon76@2x copy.png", 550,200,0,8,25,100)
        bola = Ball("Ball.png",350,250,3,3,15,15)
            
        finish = False
        
        
    if puntosP1 >= 2:
        winP1 = font2.render("Ganaste la partida Player 1",1,(255,255,0))
        window.blit(winP1,(130,330))
        
        display.update()
        time.wait(2000)
        run = False
        
    elif puntosP2 >= 3:
        winP2 = font2.render("Ganaste la partida Player 2",1,(255,255,0))
        window.blit(winP2,(230,250))
        display.update()
        time.wait(2000)
        run = False    

        
        

    display.update()
print("Fin")