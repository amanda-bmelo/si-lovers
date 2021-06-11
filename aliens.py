from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from random import randint


# Cria matriz de aliens
def aliens():
    aliens = []

    for i in range(3):
        line = []
        for j in range(4):
            alien = Sprite("images/alien.png", 1)
            alien.set_position(alien.width*1.2*j, alien.height*1.2*i)
            line.append(alien)
        aliens.append(line)

    return aliens

# Cria lista de tiros aliens
def alien_heart(array, all_aliens_hearts, dif):
    nums = [0, 0, 0, 0, -2+dif,-1+dif,0+dif]

    for line in array:
        for alien in line:
            n = randint(0,6)
            if nums[n] > 0:
                h = Sprite("images/heart.png", 1)
                h.set_position(alien.x, alien.y+alien.height), all_aliens_hearts.append(h)
                break
    return all_aliens_hearts

# Colisão dos corações do player com os aliens
def sleep(heart, array):
    slept = False

    for i in range(len(array)-1, -1, -1):
        line = array[i]
        normal_heart = True
        if line:
            for alien in line:
                if heart.y <= alien.y+72:
                    if Collision.collided_perfect(alien, heart):
                    #(alien.x < heart.x < alien.x+63 or alien.x < heart.x+15 < alien.x+63) or (alien.x < heart.x+65 < alien.x+63 or alien.x < heart.x+80 < alien.x+63):
                        if heart.width > 50:
                            normal_heart = False
                        line.pop(line.index(alien))
                        slept = True

    return array, slept, normal_heart

# Colisão dos corações dos aliens com o player
def lose(array, heart, spaceship, lives):
    loser = False

    if heart.y + heart.height >= spaceship.y:
        if spaceship.x < heart.x < spaceship.x+spaceship.width or spaceship.x < heart.x+15 < spaceship.x+spaceship.width:
            array.pop(array.index(heart))
            lives -= 1
            loser = True
    return array, loser, lives

