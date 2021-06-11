from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *


def name(points, janela):
    background = GameImage('images/name_screen.png')

    key = Window.get_keyboard()
    string = ''
    k = 0

    while k != 13:
        background.draw()
        janela.draw_text("Press ENTER to save", 100, 600, size=50, color=(240,240,240), font_name="Computer_says_no")
        
        k = key.show_key_pressed()
        if k:
            if k == 8:
                string = string[:len(string)-1]
            elif k != 13:
                string += chr(k).upper()
        
        janela.draw_text(string, 200, 300, size=50, color=(240,240,240), font_name="Computer_says_no")
        janela.update()

 
    with open("ranking.txt", "a") as n:
        string += f"  -  {points}\n"
        n.write(string)
    