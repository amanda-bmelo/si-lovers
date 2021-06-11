from PPlay.window import *
from PPlay.gameimage import *

def ranking():
    janela = Window(500,720)
    janela.set_title("Space Lovers - Ranking")
    background = GameImage("images/game.png")
    btns = [GameImage("images/menu.png"), GameImage("images/b4.png")]

    for b in range(2):  
        btns[b].set_position(180, 550+70*b)
    
    mouse = Window.get_mouse()
    click = 0

    while True:
        background.draw()
        janela.draw_text(f"RANKING", 150, 100, size=90, color=(240,240,240), font_name="Computer_says_no")

        for b in btns:
            b.draw()

        click += janela.delta_time()

        if mouse.is_button_pressed(1) and click > 5:
            click = 0
            if mouse.is_over_object(btns[0]):
                return 0
            if mouse.is_over_object(btns[1]):
                exit()

        with open("ranking.txt", "r") as r:
            players = r.readlines()
            size = len(players)
            if size > 10: size = 10

            for p in range(size):
                players[p] = players[p].split(" - ")
                players[p][1] = int(players[p][1][:-1])
            
            players = sorted(players, key=lambda player: player[1], reverse=True)
            for p in range(size):
                janela.draw_text(f"{p+1}. {players[p][0]} - {players[p][1]}", 130, 200+60*p, size=40, color=(240,240,240), font_name="Computer_says_no")
            
        janela.update()