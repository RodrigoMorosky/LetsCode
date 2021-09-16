def desenho(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |       \033[31mO\033[0;0m   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |       \033[31mO\033[0;0m   ")
        print(" |       \033[31m|\033[0;0m     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |       \033[31mO\033[0;0m   ")
        print(" |      \033[31m\|\033[0;0m    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |       \033[31mO\033[0;0m   ")
        print(" |      \033[31m\|/\033[0;0m   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |       \033[31mO\033[0;0m   ")
        print(" |      \033[31m\|/\033[0;0m   ")
        print(" |       \033[31m|\033[0;0m    ")
        print(" |            ")

    if(erros == 6):
        print(" |       \033[31mO\033[0;0m   ")
        print(" |      \033[31m\|/\033[0;0m   ")
        print(" |       \033[31m|\033[0;0m    ")
        print(" |      \033[31m/\033[0;0m     ")

    if (erros == 7):
        print(" |       \033[34mO\033[0;0m   ")
        print(" |      \033[34m\|/\033[0;0m   ")
        print(" |       \033[34m|\033[0;0m    ")
        print(" |      \033[34m/ \ \033[0;0m   ")

    print(" |            ")
    print("_|___         ")
    print()