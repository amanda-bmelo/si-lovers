from PPlay.window import *
from menu import menu
from game import game
from gameover import gameover
from dificuldade import dificuldade
from ranking import ranking
from winner import winner

janela = Window(500,720)
janela.set_title("Space Lovers")

global STATE
STATE = 0

while True:
    if STATE == 0:
        STATE = menu()
    if STATE == 1:
        STATE = game(1)
    if STATE == 2:
        STATE = dificuldade()
    if STATE == 3:
        STATE = ranking()
    if STATE == 4:
        STATE = gameover()
    