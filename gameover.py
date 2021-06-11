from PPlay.window import *
from PPlay.gameimage import *
from save_name import name

def gameover(points=0):
    janela = Window(500,720)
    janela.set_title("Space Lovers")
    screen = GameImage("images/gameover.png")

    buttons = [GameImage("images/save.png"), GameImage("images/return.png"), GameImage("images/menu.png"), GameImage("images/b4.png")]

    for b in range(4):  
        buttons[b].set_position(180, 450+60*b)

    mouse = Window.get_mouse()

    while True:
        screen.draw()
        
        for b in buttons:
            b.draw()

        if mouse.is_button_pressed(1):
            if mouse.is_over_object(buttons[0]):
                name(points, janela)
            if mouse.is_over_object(buttons[1]):
                return 1
            if mouse.is_over_object(buttons[2]):
                return 0
            if mouse.is_over_object(buttons[3]):
                exit()

        janela.update()