from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from game import game

def dificuldade():
    janela = Window(500,720)
    janela.set_title("Space Invaders")
    background = GameImage("images/background.png")

    difs = [GameImage("images/level1.png"), GameImage("images/level2.png"), GameImage("images/level3.png")]
    mouse = Window.get_mouse()

    click = 0

    for i in range(3):
        difs[i].set_position(180, 300+70*i)

    while True:
        background.draw()
        for button in difs:
            button.draw()

        teclado = Window.get_keyboard()
        click += janela.delta_time()

        if teclado.key_pressed("ESC"):
            return 0

        if mouse.is_button_pressed(1) and click > 2:
            click = 0
            if mouse.is_over_object(difs[0]):
                return game(1)
            if mouse.is_over_object(difs[1]):
                return game(2)
            if mouse.is_over_object(difs[2]):
                return game(3)

        janela.update()