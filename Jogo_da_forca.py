print('\33[33;40m#~#\33[m' * 12)
print('\33[34;40m          JOGO DE FORCA.\33[m')
print('\33[33;40m#~#\33[m' * 12)
from random import randint
computador = randint(1, 10)
print('''\33[36;40mOlá, sou seu COMPUTADOR ! Neste jogo penso em uma PALAVRA. Você tem que adivinhar as letras da PALAVRA que estou pensando.\33[m''')
palavra = [ ]
temp = [ ]
letraDig = [ ]
contapal = 0
letranum = 0
acertou = False  
palavras = ('youtube', 'livro', 'garrafa', 'escola', 'sorte')
computador = randint(0, 4)
sorteio = palavras[computador]
letra = sorteio.split(palavras[computador])
while not acertou:
    jogador = str(input('\33[35;40mDigite a primeira letra\33[m\33[32;40m: \33[m'))
    if jogador not in letraDig:
             letraDig.append(jogador)
    else:
            len(letraDig[1:])
            print('\33[31;40m[ ERRO ]\33[m\33[33;40m=>\33[mLetra {} já foi digitada\33[m\33[35;40m!!!\33[m'.format(jogador))
    temp.append(jogador)
    if jogador in sorteio:
        palavra.append(temp[0:])
        total = len(palavra)
        total2 = len(sorteio)
        if total == total2:
           acertou = True
    letra = sorteio.count(jogador)
    temp.clear()
    if jogador in sorteio:
        letranum += 1
        contapal += 1
        print('\33[34;40mA Letra \33[33;40m{}\33[m \33[34;40mé uma das LETRAS que falta para completar PALAVRA sorteada e temos \33[m\33[31;40m{} LETRA(s)\33[m\33[34;40m na PALAVRA sorteada.\33[m'.format(jogador, letra))
        print('\33[36;40mLetra armazenada com SUCESSO\33[m\33[32;40m...\33[m'.format(jogador))
        print('\33[33;40mVocê está no \33[31;40m{}°\33[m\33[33;40m palpite\33[m'.format(contapal))
    elif jogador not in sorteio:
        contapal += 1
        print('\33[34;40mA Letra \33[m\33[31;40m{}\33[m\33[34;40m não tem na palavra sorteada\33[m\33[32;40m!!!\33[m'.format(jogador))
        print('\33[33;40mVocê está no \33[31;40m{}°\33[m\33[33;40m palpite\33[m'.format(contapal)) 
    print(palavra) 
print('\33[32;40mA palavra sorteada é \33[m\33[31;40m{}\33[m \33[32;40me as LETRAS são\33[m \33[31;40m{},\33[m\33[32;40mvocê concluiu em\33[m\33[31;40m {}\33[m \33[32;40mpalpites.\33[m \33[33;40mParabéns...\33[m'.format(sorteio, palavra, contapal))
 
