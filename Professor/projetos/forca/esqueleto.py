import os


def main():
    ''' Controla a execução principal do programa. 
    Essa função é responsavel por cuidar da execução dos jogos, e decidir o que fazer quando 
    jogo encerra (continua jogando ou sai do jogo)
    Entradas:
        (nenhuma)
    Saidas:
        (nenhuma)
    '''
    # game()
    # user_interface(...)
    
    return


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
    # get_word()
    # user_interface(...)
    # update_state(...)
    
    return word_letters, all_letters, mistakes, outcome


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
    # hangman_draw(...)
    # prompt_next_game()
    # prompt_game_choice(...)


def get_word():
    '''Obtem uma palavra para o jogo.
    Entradas:
        (nenhuma)
    Saidas:
        word: palavra para o jogo
    '''
    return word


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
    return word_letters, all_letters, mistakes, outcome


def hangman_draw(mistakes):
    ''' Desenha o hangman (somente o hangman, não o desenho todo da tela).
    Entradas:
        mistakes: número de erros já cometidos pelo jogador
    Saida: 
        draw: desenho do hangman em uma string
    '''
    
    return draw  


def prompt_next_game():
    ''' Faz o prompt se o usuario gostaria de jogar um novo jogo.
    Ja inclui a validação da entrada
    Entrada: 
        (nenhuma)
    Saida:
        user_input: input do usuario
    '''
    
    return user_input


def prompt_game_choice(all_letters):
    ''' Faz o prompt da adivinhação do usuario durante o jogo.
    Ja inclui a validação da entrada
    Entrada: 
        (nenhuma)
    Saida:
        user_input: input do usuario
    '''
        
    return user_input 


if __name__ == '__main__':
    main()