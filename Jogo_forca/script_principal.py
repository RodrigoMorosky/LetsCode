import random
from funcoes import *
from grafico import *

lista_palavras = ['ONTEM', 'TESTE','BUGIGANGA', 'MEQUETREFE', 'ACENDER', 'AFILHADO', 'ARDILOSO', 'ASTERISCO', 'BASQUETE', 'VISCERAL', 'SINO', 'OFTALMOLOGISTA', 'OTORRINOLARINGOLOGISTA']
palavra_secreta = random.choice(lista_palavras)
erro = 0
letras_erradas = []
palavra_escondida = imprime_palavra(palavra_secreta)
palavra_secreta = list(palavra_secreta)

# print(palavra_secreta) - tire o comentário para usar como gabarito do programa
# print(palavra_escondida)
# print(type(palavra_escondida))


while erro <7:
    print('Palavra secreta: ',palavra_escondida)
    print('Letras erradas: ', letras_erradas)
    desenho(erro)
    chute = input('Digite uma letra: ').strip().upper()

    if len(chute) > 1:
        lista_chute = list(chute)
        lista_chute == palavra_secreta
        desenho(erro)
        print('Parabens!\n Você acertou. A palavra era {}'.format(palavra_secreta))
        break
    elif palavra_escondida == palavra_secreta:
        print('Parabéns!\n Você acetou. A palavra era {}'.format(palavra_secreta))
        break
    
    elif len(chute) ==1:
        if chute in palavra_secreta:
            idx = 0
            for n in range(len(palavra_secreta)):
                       
                if chute == palavra_secreta[idx]:
                    palavra_escondida[idx] = chute 
                    idx +=1

                    if palavra_escondida == palavra_secreta:
                        print('Parabéns!\n Você acertou. A palavra era {}'.format(palavra_secreta))
                        break
                    else:
                        pass
                
                else:
                    idx +=1
        else:
            letras_erradas += chute
            erro +=1
    
    else:
        erro = 7
        desenho(erro)
        print('Você perdeu!')

desenho(erro)
print('Você perdeu!')

        