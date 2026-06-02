from turtle import *

tela = Screen()

diametro_balao = 40   # diametro inicial do balão
diametro_balaoPOP = 100   # diametro para estourar o balão

def balao_desenhado(): # desenhando o balão
    color('blue')
    dot(diametro_balao)

def inflar_balao():
    global diametro_balao # definindo variável como global
    diametro_balao = diametro_balao + 10 
    balao_desenhado() # desenhando o balão com o novo tamanho

    if diametro_balao >= diametro_balaoPOP:
        clear()
        diametro_balao = 40
        write("POP! 😢")
    


balao_desenhado()
Screen().onkey(inflar_balao, "Up") # Ativando a função de inflar balão quando a tecla up for ativada
Screen().listen() #monitora as entradas do teclado

done()