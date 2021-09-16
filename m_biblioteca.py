def cumprimenta_horario(nome, horario):
    if horario <12:
        print("Bom dia {}".format(nome))
    elif horario <18:
        print("Boa tarde {}".format(nome))
    else:
        print("Boa noite {}".format(nome))

def soma(num1, num2): # função com argumento e com return
    total = num1 + num2
    return total

def calculadora (num1, num2, operador):
    if operador =='+':
        calculo = num1 + num2
    elif operador =='-':
        calculo = num1 - num2
    elif operador =='/':
        calculo = num1 / num2
    elif operador =='*':
        calculo = num1 * num2
    else:
        calculo = num1 ** num2
        raise ValueError('Essa operação não existe!')
    return calculo

def pot (base, expoente):
    if expoente >0:
        return base * pot(base, expoente -1)
    else:
        return 1

def fatorial (n):
    if n >0:
        return n * fatorial(n - 1)
    else:
        return 1