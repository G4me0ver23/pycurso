from random import randrange

def display_borda(borda):
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {borda[0][0]}   |   {borda[0][1]}   |   {borda[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {borda[1][0]}   |   {borda[1][1]}   |   {borda[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {borda[2][0]}   |   {borda[2][1]}   |   {borda[2][2]}   |
|       |       |       |
+-------+-------+-------+

""")

def enter_move(borda):
    ok = False  
    while not ok:
        move = input("Digite seu movimento: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok: 
            print("Movimento inválido - faça outro movimento!")
            continue
        move = int(move) - 1
        linha = move // 3  
        coluna = move % 3  
        sign = borda[linha][coluna]  
        ok = sign not in ['O', 'X']
        if not ok:  
            print("Campo já ocupado - faça outro movimento!")
            continue
        borda[linha][coluna] = 'O'  

def ListaCasasLivres(borda):
    livres = []  
    for linha in range(3):  
        for coluna in range(3):  
            if borda[linha][coluna] not in ['O', 'X']:  
                livres.append((linha, coluna))
    print(livres)
    return livres

def ConferirVencedor(borda, sinal):
    if sinal == "X":  
        player = 'eu'  
    elif sinal == "O":  
        player = 'voce'  
    else:
        player = None  
    diagn1 = diagn2 = True
    for rc in range(3):
        if borda[rc][0] == sinal and borda[rc][1] == sinal and borda[rc][2] == sinal:
            return player
        if borda[0][rc] == sinal and borda[1][rc] == sinal and borda[2][rc] == sinal:
            return player
        if borda[rc][rc] != sinal:  
                diagn1 = False
        if borda[2 - rc][2 - rc] != sinal:  
                diagn2 = False
    if diagn1 or diagn2:
        return player
    return None


def draw_move(borda, livres): 
    csLivre = len(livres)
    if csLivre > 0:  
        num = randrange(csLivre)
        linha, coluna = livres[num]
        borda[linha][coluna] = 'X'

borda = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  
borda[1][1] = 'X'  
livres = ListaCasasLivres(borda)
jogador = True  
while len(livres):
    display_borda(borda)
    if jogador:
        enter_move(borda)
        winner = ConferirVencedor(borda, 'O')
    else:
        draw_move(borda, livres)
        winner = ConferirVencedor(borda, 'X')
    if winner != None:
        break
    jogador = not jogador
    livres = ListaCasasLivres(borda)

display_borda(borda)
if winner == 'voce':
    print("Você ganhou!")
elif winner == 'eu':
    print("eu venci")
else:
    print("Empate!")

