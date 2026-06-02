from turtle import *

diametro_balao = 40   # diametro inicial do balão
diametro_balaoPOP = 100   # diametro para estourar o balão

def balao_desenhado(): # desenhando o balão
    color('blue')
    dot(diametro_balao)

balao_desenhado()

tela.mainloop()