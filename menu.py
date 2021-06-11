from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *


def menu():
    janela = Window(500,720)
    janela.set_title("Space Lovers")
    background = GameImage("images/background.png")

    mouse = Window.get_mouse()
    buttons = [GameImage("images/b1.png"), GameImage("images/b2.png"),GameImage("images/b3.png"), GameImage("images/b4.png")]
    click = 0

    for i in range(4):
        buttons[i].set_position(180, 400+70*i)

    while True:
        background.draw()
        for button in buttons:
            button.draw()
        
        click += janela.delta_time()

        if mouse.is_button_pressed(1) and click > 2:
            click = 0
            if mouse.is_over_object(buttons[0]):
                return 1
            if mouse.is_over_object(buttons[1]):
                return 2
            if mouse.is_over_object(buttons[2]):
                return 3
            if mouse.is_over_object(buttons[3]):
                exit()


        janela.update()
