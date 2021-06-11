from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from random import randint
from winner import winner
from aliens import aliens, alien_heart, sleep, lose
from gameover import gameover

def moveMatriz(array, position):

    for line in array:
        for alien in line:
            alien.move_x(position), alien.move_y(10)


def game(level, points=0, nome=''):
    janela = Window(500,720)
    janela.set_title("Space Lovers")
    background = GameImage("images/game.png")

    teclado = Window.get_keyboard()
    
    spaceship = GameImage("images/ship.png")
    spaceship.set_position(200, 580)

    all_hearts = []
    time, time_player = 2, 0
    lives = 5
    loser = False
    blink = False

    # DIFICULDADE
    if level == 1: a = 1
    elif level == 2: a = 1.5
    else: a = 2

    # ALIENS
    all_aliens = aliens()
    all_aliens_hearts = []
    alienSpeed = a
    time_alien = 0
    cd = 0

    while True:
        background.draw()
        if not loser and time > 2:
            spaceship.draw()
            blink = False
        elif randint(0,1) > 0:
            spaceship.draw()
            blink = True

        heartSpeed = -250*janela.delta_time()*a 
        time += janela.delta_time()
        time_player += janela.delta_time()
        time_alien += janela.delta_time()
        cd += janela.delta_time()


        # PLAYER

        if teclado.key_pressed("ESC"):
            return 0
        if teclado.key_pressed("LEFT") and spaceship.x > 0:
            spaceship.x -= 2
        if teclado.key_pressed("RIGHT") and spaceship.x < 400:
            spaceship.x += 2
        if teclado.key_pressed("SPACE") and time_player > 0.5:
            hearts = Sprite("images/shot.png", 1)

            while teclado.key_pressed("SPACE") and cd > 10:
                time_player += janela.delta_time()
                if time_player > 3:
                    hearts = Sprite("images/super_heart.png", 1)
                    cd = 0
                    break
            time_player = 0
            hearts.set_position(spaceship.x, spaceship.y-30)
            all_hearts.append(hearts)
        

        # COLISÕES
        # Tiros da nave
        for heart in all_hearts:
            if heart.y > 0:
                heart.move_y(heartSpeed)

                if not all_aliens[-1]:
                    all_aliens.pop(-1)
                if not all_aliens: 
                    return winner(level, points)

                slept = False
                normal_heart = True
                if all_aliens[-1][0].y + all_aliens[-1][0].height >= heart.y:
                    all_aliens, slept, normal_heart = sleep(heart, all_aliens)

                if not slept and normal_heart:
                    heart.draw()
                else:
                    points += 25*level
                    if normal_heart:
                        all_hearts.pop(all_hearts.index(heart))
            else:
                all_hearts.pop(all_hearts.index(heart))

        # Tiros dos aliens
        for heart in all_aliens_hearts:
            if heart.y < 720:
                heart.move_y(-heartSpeed)
                loser = False
                if heart.y + heart.height >= spaceship.y:
                    all_aliens_hearts, loser, lives = lose(all_aliens_hearts, heart, spaceship, lives)

                if not loser:
                    heart.draw()
                elif blink: 
                    lives += 1
                    loser = False
                else: 
                    time = 0
                    spaceship.set_position(200, 580)
            else:
                all_aliens_hearts.pop(all_aliens_hearts.index(heart))


        # ALIENS
        for line in all_aliens:
            if line:

                # Deslocando quando atinge laterais
                if line[0].x < 0 or line[-1].x >= 500-line[-1].width:
                    alienSpeed *= -1
                    moveMatriz(all_aliens, alienSpeed)

                # Setando tiros dos aliens
                if time_alien > randint(1, 3//level):
                    time_alien = 0
                    all_aliens_hearts = alien_heart(all_aliens, all_aliens_hearts, level)

                for alien in line:
                    if alien.y+alien.height >= 580: return 4

                    alien.move_x(alienSpeed)
                    alien.draw()
            else:
                all_aliens.pop(all_aliens.index(line))  
        

        # GAMEOVER // WINNER
        if lives == 0: 
            return gameover(points)
        elif not all_aliens: 
            return winner(level, points)


        janela.draw_text(f"Pontos: {points}", 30, 20, size=30, color=(240,240,240), font_name="Computer_says_no")
        janela.draw_text(f"Vidas: {lives}", 400, 20, size=30, color=(240,240,240), font_name="Computer_says_no")
        janela.update()
    