from PPlay.window import *
from PPlay.gameimage import *
from save_name import name


def winner_screen(level, points):
    janela = Window(500,720)
    janela.set_title("Space Lovers")
    fundo = GameImage("images/winner.png")

    buttons = [GameImage("images/next.png"), GameImage("images/menu.png"), GameImage("images/b4.png")]

    if level == 3: 
        buttons.pop(0)
        name(points, janela)

    for b in range(len(buttons)):  
        buttons[b].set_position(180, 500+70*b)

    mouse = Window.get_mouse()
    click = 0

    while True:
        fundo.draw()
        janela.draw_text(f"{points}", 210, 300, size=90, color=(240,240,240), font_name="Computer_says_no", italic=True)

        click += janela.delta_time()

        for b in buttons:
            b.draw()

        if mouse.is_button_pressed(1) and click > 1:
            click = 0
            if level != 3:
                if mouse.is_over_object(buttons[0]):
                    return level+1
                if mouse.is_over_object(buttons[1]):
                    return 0
                if mouse.is_over_object(buttons[2]):
                    exit()
            else:
                if mouse.is_over_object(buttons[0]):
                    return 0
                if mouse.is_over_object(buttons[1]):
                    exit()

        janela.update()