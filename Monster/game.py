import pgzrun
import time

WIDTH = 400
HEIGHT = 800

TITLE = "Amelie pirate"

player = Actor("player")
player.x = 200
player.y = 720

pirate = Actor("pirate")
pirate.x = 80
pirate.y = 730

background = Actor("background")

gameover = 3

score = 2

def draw():
    screen.clear()
    background.draw()
    player.draw()
    pirate.draw()
    screen.draw.text('Schaden: ' + str(score), (15,10), color=(255,255,255), fontsize=40)
    screen.draw.text('GAMEOVER', (30,30), color=(255,220,180), fontsize=88)



def set_score_detection():
    global score
    global gameover

    score = score -1

    player.x = 200
    player.y = 720
    time.sleep(1)
    player.image = "player"

def steuerung():
    if keyboard[keys.RIGHT]:
        player.x = player.x + 2
    if keyboard[keys.LEFT]:
        player.x = player.x -2
    if player.x <= 30:
        player.x = 30
    if player.x >= 370:
        player.x = 370

def gameover():
    screen.clear()
    screen.draw.text('kjkjkjkj', (30,30), color=(255,220,180), fontsize=88)
    global score
    score = 3
    player.x = 200
    player.y = 720
    time.sleep(3)
    player.image = "player"
    

def collision_detection():
    if player.colliderect(pirate):
        if score > 1:
            player.image = "explosion"
            clock.schedule(set_score_detection, 0.01)
        else:
            player.image = "gameover"
            clock.schedule(gameover, 0.01)
        
def update():
       
    steuerung()
    collision_detection()
    
    
    



pgzrun.go()
