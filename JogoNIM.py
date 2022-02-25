

tipoDeJogo = 0

while tipoDeJogo == 0

print ("Bem-vindo ao jogo do NIM! Escolha:")
print ("1 - para jogar uma partida isolada")
print ("2 - para jogar um campeonato")

tipoDeJogo = int(input("Sua opção: "))

if tipoDeJogo == 1:
    print ("Você escolheu uma partida isolada!")
    partida ()

elif tipoDeJogo == 2:
    print ("Você escolheu um campeonato!")
    campeonato()
else:
    print("Opção inválida!")
    tipoDeJogo = 0


def partida():
    n = int (input("Quantas peças?"))
    m = int (input("Limite de peças por jogada?"))

vezDoComputador = True

    
    if n % (m + 1) == 0:
        vezDoComputador = False

while n > 0:
    if vezDoComputador:
        return "Computador começa!"
        computador_escolhe_jogada(n,m)


        
        return "Você começa!"
        usuario_escolhe_jogada(n,m)
    else:
        


def computador_escolhe_jogada(n,m):
    r = 
    O computador tirou    peça.
    Agora restam x peças no tabuleiro





def usuario_escolhe_jogada(n,m):
    p = int (input("Quantas peças vocês vai tirar?"))
    if p > m:
        print("Oops! Jogada inválida! Tente de novo.")
        
    r = n - p
    
    "Você tirou",p,"peças."
    "Agora restam",r,"peças no tabuleiro."
