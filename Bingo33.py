import random
from time import sleep

def bingooooo():
    print('''
#######       ##     ####       ##       ########           ########
##     ##     ##     ## ##      ##      ##       ##       ##        ##
##     ##     ##     ##  ##     ##     ##                ##          ##
#######       ##     ##   ##    ##     ##      #####     ##          ##
##     ##     ##     ##     ##  ##     ##         ##     ##          ##
##     ##     ##     ##      ## ##      ##       ##       ##        ##
#######       ##     ##       ####        #######           ########
\n\n\n''')

def bingooooo2():
    sleep(1)
    print('\033[1;33m')
    bingooooo()
    sleep(1)
    print('\033[1;32m')
    bingooooo()
    sleep(1)
    print('\033[1;31m')
    bingooooo()
    print('\033[0m')
    return

print('-=' * 65)
print('''\033[1;33m''')
bingooooo()
print('''


                                                                                 ####           ########          ########
                                                                                ##  ##          ##      ##       ##  
                                                                               ##    ##         ##       ##      ##  
                                                                              ##      ##        ##        ##      ########
                                                                             ############       ##       ##              ##
                                                                            ##          ##      ##      ##               ##
                                                                           ##            ##     ########          ########
\033[0m''')

def chamaBola(x):
    if x == 1:
        print('\nAgora sim, começa o jogo: \n')
    elif x == 5:
        print('\nO Cachorro Brabo: \n')
    elif x == 7:
        print('\nO Número da mentira. \n')
    elif x == 9:
        print('\nO Pingo no pé: \n')
    elif x == 10:
        print('\nO Craque de bola: \n')
    elif x == 11:
        print('\nUm atrás do outro! \n')
    elif x == 13:
        print('\nDeu azar!!! \n')
    elif x == 16:
        print('\nO leão esta solto! \n')
    elif x == 17:
        print('\nO pulo do macaco. \n')
    elif x == 22:
        print('\nDois patinhos na lagoa: \n')
    elif x == 31:
        print('\nPreparem os fogos que é Reveillon!!! \n')
    elif x == 33:
        print('\nA Idade de Cristo: \n')
    elif x == 45:
        print('\nFim do primeiro tempo. \n')
    elif x == 51:
        print('\nUma boa idéia! \n')
    elif x == 55:
        print('\nOs dois cachoros do padre. \n')
    elif x == 69:
        print('\nPode isso Arnaldo?\n') 
    elif x == 75:
        print('\nTerminou o jogo!\n Só que nãooooo\n')
    else:
        chamadas = ['\nA bola chamada foi:\n', '\nA Bola da vez é:\n', '\nEsse ... Será que alguém tem?\n', '\nO número da sorte é:\n']
        print(random.choice(chamadas))
        return

def showSorteio(x):
    unidade = x % 10
    dezena = int((x - unidade) / 10)
    if unidade == 1:
        unidade = [
'   ###     ',
'  ####     ',
' ## ##     ',
'##  ##     ',
'    ##     ',
'    ##     ', 
'#########  ',
'\n'
]
    elif unidade == 2:
        unidade = [
' ########   ',
'##      ##  ',    
'      ##    ',     
'    ##      ',      
'  ##        ',
'##      ##  ',
' #########  ',
'\n'
]
    elif unidade == 3:
        unidade = [
' ########   ',
'##      ##  ',
'        ##  ',
'    ####    ',
'        ##  ',
'##      ##  ',
' ########   ',
'\n'
]
    elif unidade == 4:
        unidade = [
'   ######    ',
'  ##   ##    ',
' ##    ##    ',
'##     ##    ',
'###########  ',
'       ##    ',
'       ##    ',
'\n'
]
    elif unidade == 5:
        unidade = [
'#########   ',
'##     ##   ',
'##          ',  
'#########   ',
'        ##  ',
'##      ##  ',
' ########   ',
'\n'
]
    elif unidade == 6:
        unidade = [
' ########   ',
'##          ',      
'##          ',  
'#########   ',
'##      ##  ',
'##      ##  ',
' ########   ',
'\n'
]
    elif unidade == 7:
        unidade = [
'###########  ',
'##       ##  ',    
'        ##   ',     
'       ##    ',     
'      ##     ',
'     ##      ',
'    ##       ',
'\n'
]
    elif unidade == 8:
        unidade = [
' ########   ',
'##      ##  ',
'##      ##  ',
' ########   ',
'##      ##  ',
'##      ##  ',
' ########   ',
'\n'
]
    elif unidade == 9:
        unidade = [
' ########   ',
'##      ##  ',
'##      ##  ',
' ########   ',
'        ##  ',
'        ##  ',
' ########   ',
'\n'
]
    if unidade == 0:
        unidade = [
' ########   ',
'##      ##  ',
'##      ##  ',
'##      ##  ',
'##      ##  ',
'##      ##  ',
' ########   ',
'\n'
]

    if dezena == 1:
        dezena = [
'   ###     ',
'  ####     ',
' ## ##     ',
'##  ##     ',
'    ##     ',
'    ##     ', 
'#########  ',
'\n'
]
    elif dezena == 2:
        dezena = [
' ########   ',
'##      ##  ',    
'      ##    ',     
'    ##      ',      
'  ##        ',
'##      ##  ',
' #########  ',
'\n'
]
    elif dezena == 3:
        dezena = [
' ########   ',
'##      ##  ',
'        ##  ',
'    ####    ',
'        ##  ',
'##      ##  ',
' ########   ',
'\n'
]
    elif dezena == 4:
        dezena = [
'   ######    ',
'  ##   ##    ',
' ##    ##    ',
'##     ##    ',
'###########  ',
'       ##    ',
'       ##    ',
'\n'
]
    elif dezena == 5:
        dezena = [
'#########   ',
'##     ##   ',
'##          ',  
'#########   ',
'        ##  ',
'##      ##  ',
' ########   ',
'\n'
]
    elif dezena == 6:
        dezena = [
' ########   ',
'##          ',      
'##          ',  
'#########   ',
'##      ##  ',
'##      ##  ',
' ########   ',
'\n'
]
    elif dezena == 7:
        dezena = [
'###########  ',
'##       ##  ',    
'        ##   ',     
'       ##    ',     
'      ##     ',
'     ##      ',
'    ##       ',
'\n'
]
    elif dezena == 8:
        dezena = [
' ########   ',
'##      ##  ',
'##      ##  ',
' ########   ',
'##      ##  ',
'##      ##  ',
' ########   ',
'\n'
]
    elif dezena == 9:
        dezena = [
' ########   ',
'##      ##  ',
'##      ##  ',
' ########   ',
'        ##  ',
'        ##  ',
' ########   ',
'\n'
]
    if dezena == 0:
        dezena = [
' ########   ',
'##      ##  ',
'##      ##  ',
'##      ##  ',
'##      ##  ',
'##      ##  ',
' ########   ',
'\n'
]
    if x < 10:
        for y in range(0,8):
            print(f'\033[1;32m{unidade[y]}\033[0m')
    else:
        for y in range(0,8):
            print(f'\033[1;32m{dezena[y]}{unidade[y]}\033[0m')
    return

configNomes = True
configSorteio = True
jogadores = []
while True:
    print('-=' * 65)
    print('\n')
    print('\033[1;33mBEM VINDO AO BINGO!!! ESCOLHA UMA OPÇÃO: \033[0m\n')
    print('''
 ================================================================================================================================
|                                                                                                                                |
|               S = Jogar                           C = Configurar                            Outras Teclas = Sair               |
|                                                                                                                                |
 ================================================================================================================================
 \n\n''')
    print('-=' * 65)
    inicio = str(input('Digite sua opção: ')).upper()
    if inicio == 'S':
        jogo = int(input('Defina a quantidade de jogadores: '))
        if configNomes == True:
            for y in range(1,jogo+1):
                nomes = input(f'Digite o nome do {y}° Jogador: ').upper()
                jogadores.append(nomes)
        print('-=' * 65)
        b = [0] * jogo
        i = [0] * jogo
        n = [0] * jogo
        g = [0] * jogo
        o = [0] * jogo
        cartela = []
        cartela2 = []
        sorteio = 0
        listaSorteio = []
        temVencedor = False
        vencedores = []
        cartelaDosVencedores = []
        nomeVencedores = []
        pifados = []
        nomePifados = []
        break
    elif inicio == 'C':
        while True:
            print('\033[1;33mCONFIGURAÇÕES - ESCOLHA UMA DAS OPÇÔES ABAIXO: \033[0m\n')
            print('''
 ================================================================================================================================
|                                                 S = Desativar Sorteio Personalizado                                            |
|                                                 N = Desativar Nomes aos Jogadores                                              |
|                                                 A = Ambas as opções                                                            |
 ================================================================================================================================
 \n\n''')
            config = input('Digite sua opção: ').upper()
            if config == 'S':
                configSorteio = False
                break
            elif config == 'N':
                configNomes = False
                break
            elif config == 'A':
                configNomes, configSorteio = False, False
                break
            else:
                print('Retornando ao Menu Principal...')
                sleep(1)
                break
    else:
        print('\033[1;32mOK, até a próxima ...\033[0m\n')
        print('\n','-=-'*20,'\033[1;33m  FIM \033[0m','-=-'*20)
        exit()
print('-=' * 65)

                


for a in range(0, jogo):
    bingo = ['B', 'I', 'N', 'G', 'O']
    b[a] = sorted((random.sample(range(1,16),5)))
    i[a] = sorted((random.sample(range(16,31),5)))
    n[a] = sorted((random.sample(range(31,46),5)))
    n[a][2] = '$$'
    g[a] = sorted((random.sample(range(46,61),5)))
    o[a] = sorted((random.sample(range(61,76),5)))
    cartela.append(b[a] + i[a] + n[a] + g[a] + o[a])
    cartela2.append(b[a] + i[a] + n[a] + g[a] + o[a])
    print('\n')
    print('-'*22)
    if configNomes == True:
        print(f'\033[1;33m{jogadores[a]}\033[0m'.center(33))
    else:
        print(f'\033[1;33mJOGADOR {a+1}\033[0m'.center(33))
    print(f'{bingo[0]} - {bingo[1]} - {bingo[2]} - {bingo[3]} - {bingo[4]}'.center(23))
    print('-'*22)
    print(f'{b[a][0]:2} - {i[a][0]} - {n[a][0]} - {g[a][0]} - {o[a][0]}')
    print(f'{b[a][1]:2} - {i[a][1]} - {n[a][1]} - {g[a][1]} - {o[a][1]}')
    print(f'{b[a][2]:2} - {i[a][2]} - {n[a][2]} - {g[a][2]} - {o[a][2]}')
    print(f'{b[a][3]:2} - {i[a][3]} - {n[a][3]} - {g[a][3]} - {o[a][3]}')
    print(f'{b[a][4]:2} - {i[a][4]} - {n[a][4]} - {g[a][4]} - {o[a][4]}')
    print('\n')
    print('-=' * 65)

print('-=' * 65)
print('\033[1;32mSENHORAS E SENHORAS, VAMOS DAR ÍNICIO AO SORTEIO DO BINGO:\n')
inicio2 = str(input('''\033[1;33mPODEMOS COMEÇAR?\n 
Aperte [S] para SIM , [QUALQUER OUTRA TECLA] para CANCELAR: \033[0m\n''')).upper()

while True:        
    if inicio2 == 'S':
        print('\033[1;32mObrigado, vamos começar o sorteio!!! Boa Sorte!!!\033[0m\n')
        break
    else:
        print('\033[1;32mOK, até a próxima ...\033[0m\n')
        exit()
print('-=' * 65)

cont = 76
cartelaPreenchida = []
cartelaPreenchida = 0
while cont >= 0 and temVencedor == False:
    sorteio = random.randrange(1,76)
    if sorteio in listaSorteio:
        continue
    else:
        cont -= 1
        listaSorteio.append(sorteio)
        if configSorteio == True:
            chamaBola(sorteio)
            sleep(1)
            showSorteio(sorteio)
            print('-=' * 20)
            sleep(0)
        else:
            print(f'Bola sorteada de número \033[1;32m{sorteio}.\033[0m')
            print('-=' * 20)
            sleep(0)
        for j in range(0,jogo):
            for k in range(0,25):
                if cartela2[j][k] == sorteio:
                        cartela2[j][k] = '$$'
        for j in range(0,jogo):
            cartelaPreenchida = 0
            for k in range(0,25):
                if cartela2[j][k] == '$$':
                    cartelaPreenchida += 1 
            if cartelaPreenchida == 25:
                cartelaDosVencedores.append(cartela[j])
                vencedores.append(j+1)
                temVencedor = True
                bingooooo2()
                if configNomes == True:
                    nomeVencedores.append(jogadores[j])
            if cartelaPreenchida == 24:
                if configNomes == True:
                    if jogadores[j] in nomePifados:
                        continue
                    else:
                        nomePifados.append(jogadores[j])
                    print(f'\n\n\033[1;32mTemos {len(listaSorteio)} bolas chamadas e o(s) Jogador(es): {nomePifados} pifado(s)!!!\n\033[0m')
                else:
                    if j in pifados:
                        continue
                    else:
                        pifados.append(j)
                    print(f'\n\n\033[1;32mTemos {len(listaSorteio)} bolas chamadas e {len(pifados)} jogador(es) pifado(s)!!!\n\033[0m')

print('-=' * 65)
if len(vencedores) <= 1:
    print(f'\n\n\033[1;32mTivemos {len(vencedores)} ganhador!!!\nAbaixo segue sua cartela e bolas sorteadas:\033[0m\n')
else:
    print(f'\n\n\033[1;32mTivemos {len(vencedores)} ganhadores!!!\nAbaixo segue cartelas e bolas sorteadas:\033[0m\n')
for a in range(0, len(vencedores)):
    if configNomes == True:
        print('\n')
        print(f'\033[1;33m{nomeVencedores[a]}\033[0m'.center(33))
    else:
        print('\n')
        print(f'\033[1;33mJOGADOR {vencedores[a]}\033[0m'.center(33))
    print('-'*22)
    print(f'{bingo[0]} - {bingo[1]} - {bingo[2]} - {bingo[3]} - {bingo[4]}'.center(22))
    print('-'*22)
    print(f'{cartelaDosVencedores[a][0]:2} - {cartelaDosVencedores[a][5]:2} - {cartelaDosVencedores[a][10]:2} - {cartelaDosVencedores[a][15]:2} - {cartelaDosVencedores[a][20]:2}')
    print(f'{cartelaDosVencedores[a][1]:2} - {cartelaDosVencedores[a][6]:2} - {cartelaDosVencedores[a][11]:2} - {cartelaDosVencedores[a][16]:2} - {cartelaDosVencedores[a][21]:2}')
    print(f'{cartelaDosVencedores[a][2]:2} - {cartelaDosVencedores[a][7]:2} - {cartelaDosVencedores[a][12]:2} - {cartelaDosVencedores[a][17]:2} - {cartelaDosVencedores[a][22]:2}')
    print(f'{cartelaDosVencedores[a][3]:2} - {cartelaDosVencedores[a][8]:2} - {cartelaDosVencedores[a][13]:2} - {cartelaDosVencedores[a][18]:2} - {cartelaDosVencedores[a][23]:2}')
    print(f'{cartelaDosVencedores[a][4]:2} - {cartelaDosVencedores[a][9]:2} - {cartelaDosVencedores[a][14]:2} - {cartelaDosVencedores[a][19]:2} - {cartelaDosVencedores[a][24]:2}')
    print(f'\n\033[1;32mBolas sortedas: \033[0m\n{sorted(listaSorteio)}')
print('\n','-=-'*20,'\033[1;33m  FIM \033[0m','-=-'*20)

