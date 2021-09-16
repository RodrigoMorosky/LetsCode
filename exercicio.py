def separa_num_txt(texto):
    letras = ''
    numero = ''
    for i in texto:
        if i.isdigit():
            numero = numero + i
        elif i.isalpha():
            letras = letras + i
        else:
            pass
    return print(letras,'\n', numero)

txt = input('Digite o texto:')
separa_num_txt(txt)