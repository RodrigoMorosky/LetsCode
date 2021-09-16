import os
hangman_base = '''
Instruções: Tente adivinhar a palavra letra a letra antes de ir a forca.
==============  Forca  ================
 +---+
 |   |   		{wrong_letters}
{hangman}  
 |     			{word_letters} 
 |_______

=========================================
'''

hangman_pttr = '''
 |   {head}   
 |  {left_arm}{body}{right_arm}                  
 |  {left_leg} {right_leg}
'''.strip('\n')

def hangman_draw(mistakes):
    ''' Desenha o hangman (somente o hangman, não o desenho todo da tela).
    Entradas:
        mistakes: número de erros já cometidos pelo jogador
    Saida: 
        draw: desenho do hangman em uma string
    '''
    head = 'O' if mistakes > 0 else ' '
    body = '|' if mistakes > 1 else ' '
    left_arm = '/' if mistakes > 2 else ' '
    right_arm = '\\' if mistakes > 3 else ' '
    left_leg = '/' if mistakes > 4 else ' '
    right_leg = '\\' if mistakes > 5 else ' '
    draw = hangman_pttr.format(
        head=head, 
        body=body, 
        left_arm=left_arm, 
        right_arm=right_arm, 
        left_leg=left_leg,
        right_leg=right_leg)
    return draw  

def user_interface(word_letters, all_letters, mistakes, outcome):
    ''' Faz a interface com o usuario.
    Imprime e lê os valores do terminal.
    Entradas:
         word_letters: lista com os caracters a serem imprimidos na dica. 
            Ex: ['_', 'A', '_', 'A', '_', 'A'] para um jogo onde o jogador já acertou o `A` de 
            `Banana` 
        all_letters: lista com o historico das tentativas de letras pelo jogador
        mistakes: número de erros já cometidos pelo jogador 
        outcome: controla o estado da execução do jogo. Pode assumir valores de 'won', 'lost', 
            'continue' ou 'exit'
    Saida:
        user_input: input do usuario
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print(hangman_base.format(
        wrong_letters=' '.join(all_letters).upper(), 
        word_letters=' '.join(word_letters).upper(),
        hangman=hangman_draw(mistakes)
    ))
    if outcome == 'won':
        print('Parabens, você ganhou!!!')
        return prompt_next_game()
    elif outcome == 'lost':
        print('Ahhhh, não foi dessa vez :(')
        return prompt_next_game()
    else:
        return prompt_game_choice(all_letters)

    
def prompt_next_game():
    ''' Faz o prompt se o usuario gostaria de jogar um novo jogo.
    Ja inclui a validação da entrada
    Entrada: 
        (nenhuma)
    Saida:
        user_input: input do usuario
    '''
    user_input = ''
    while user_input not in list('sn'):
        user_input = input('Gostaria de jogar de novo? (s/n): ').lower().strip()
    return user_input


def prompt_game_choice(all_letters):
    ''' Faz o prompt da adivinhação do usuario durante o jogo.
    Ja inclui a validação da entrada
    Entrada: 
        (nenhuma)
    Saida:
        user_input: input do usuario
    '''
    user_input = ''
    while (
        len(user_input) == 0 or 
        user_input.isspace() or 
        user_input in all_letters):
        user_input = input('Digite uma letra: ').lower().strip()
        
    return user_input 


def update_state(word_letters, all_letters, mistakes, word, user_input):
    ''' Atualiza o estado do jogo. 
    Estado são as variaveis que contém as informações que controlam o que está acontecendo 
    no jogo. Essas variaveis são `word_letters`, `all_letters`, `mistakes` e `outcome`
    Entradas:
         word_letters: lista com os caracters a serem imprimidos na dica. 
            Ex: ['_', 'A', '_', 'A', '_', 'A'] para um jogo onde o jogador já acertou o `A` de 
            `banana` 
        all_letters: lista com o historico das tentativas de letras pelo jogador
        mistakes: número de erros já cometidos pelo jogador 
        word: palavra usada no jogo
        user_input: input fornecido pelo usuario durante o jogo
    Saidas:
        word_letters: lista com os caracters a serem imprimidos na dica. 
            Ex: ['_', 'A', '_', 'A', '_', 'A'] para um jogo onde o jogador já acertou o `A` de 
            `banana` 
        all_letters: lista com o historico das tentativas de letras pelo jogador
        mistakes: número de erros já cometidos pelo jogador 
        outcome: controla o estado da execução do jogo. Pode assumir valores de 'won', 'lost', 
            'continue' ou 'exit'
    '''
    outcome = 'continue'
    if len(user_input) > 1:
        if user_input == word:
            outcome = 'won'
        elif user_input == 'sair':
            outcome = 'exit'
        else:
            outcome = 'lost'
            mistakes = 6
    else:
        all_letters.append(user_input)
        if user_input in word:
            word_letters = [w if w in all_letters else '_' for w in word]
        else:
            mistakes += 1
    if mistakes > 5:
        outcome = 'lost'
    elif '_' not in word_letters:
        outcome = 'won' 
    return word_letters, all_letters, mistakes, outcome


def get_word():
    '''Obtem uma palavra para o jogo.
    Entradas:
        (nenhuma)
    Saidas:
        word: palavra para o jogo
    '''
    return 'banana'


def game():
    ''' Cuida da execução de um jogo.
    Faz a execução de uma partida do jogo da forca. Retorna as informações do estado final após o
    fim do jogo. 
    Entradas:
        (nenhuma)
    Saidas:
        word_letters: lista com os caracters a serem imprimidos na dica. 
            Ex: ['_', 'A', '_', 'A', '_', 'A'] para um jogo onde o jogador já acertou o `A` de 
            `Banana` 
        all_letters: lista com o historico das tentativas de letras pelo jogador
        mistakes: número de erros já cometidos pelo jogador 
        outcome: controla o estado da execução do jogo. Pode assumir valores de 'won', 'lost', 
            'continue' ou 'exit'
    '''
    word = get_word()
    word_letters = ['_' for w in word]
    all_letters = []
    mistakes = 0
    outcome = 'continue'
    
    while outcome == 'continue':
        user_input = user_interface(word_letters, all_letters, mistakes, outcome)
        word_letters, all_letters, mistakes, outcome = \
            update_state(word_letters, all_letters, mistakes, word, user_input)
    
    return word_letters, all_letters, mistakes, outcome


def main():
    ''' Controla a execução principal do programa. 
    Essa função é responsavel por cuidar da execução dos jogos, e decidir o que fazer quando 
    jogo encerra (continua jogando ou sai do jogo)
    Entradas:
        (nenhuma)
    Saidas:
        (nenhuma)
    '''
    while True:
        word_letters, all_letters, mistakes, outcome = game()
        if outcome == 'exit':
            print('Hasta la vista!')
            break
        next_game = user_interface(word_letters, all_letters, mistakes, outcome)
        if next_game == 'n':
            print('Hasta la vista!')
            break

if __name__ == '__main__':
    main()