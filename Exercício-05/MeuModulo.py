import random
import matplotlib.pyplot as plt
import numpy as np


def LeMatriz():
    '''
    Lê separadamente cada linha da matriz com valores separados por vírgula.
    Encerra a leitura quando o usuário digita "fim"
    '''
    print('Digite cada linha da matriz com valores separados por vírgula.\nAo terminar, digite "fim":')
    linha = input()
    M = []
    while 'fim' not in linha:
        L = [float(x) for x in linha.split(',')]
        linha = input()
        M.append(L)
    return M


def ImprimeListaFloat(L):
    '''
    Recebe uma lista de valores reais
    Imprime os valores com uma casa decimal separados por vírgula
    '''
    s = ''
    for x in L:
        s = s + '%.1f' % x + ', '
    print(s[:-2])


# Escreva aqui todas as funções que faltam para que o programa funcione
def LeListaFloat():  # utilize esta função para a leitura da lista
    '''
    Lê uma linha com números reais separados por vírgula
    Retorna uma lista de números reais
    '''
    l = input('Digite números reais separados por vírgula:\n')
    s = l.strip().split(',')
    L = [float(x) for x in s]
    return L


def uniformFloat(low, high):
    return random.uniform(low, high)


def discrete(a):
    r = uniformFloat(0.0, sum(a))
    subtotal = 0.0
    for i in range(len(a)):
        subtotal += a[i]
        if subtotal > r:
            return i
    return len(a) - 1


def IFS(n, probabilities, cx, cy):
    x_l = []
    y_l = []
    x = 0.0
    y = 0.0
    for i in range(n):
        r = discrete(probabilities)
        x0 = cx[r][0] * x + cx[r][1] * y + cx[r][2]
        y0 = cy[r][0] * x + cy[r][1] * y + cy[r][2]
        x = x0
        y = y0
        x_l.append(x)
        y_l.append(y)
    return (x_l, y_l)
