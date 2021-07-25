import random

def LeMatriz():
    '''
    Lê separadamente cada linha da matriz com valores separados por vírgula.
    Encerra a leitura quando o usuário digita "fim"
    '''
    print('Digite cada linha da matriz com valores separados por vírgula.\nAo terminar, digite "fim":')
    linha=input()
    M=[]
    while 'fim' not in linha:    
      L=[float(x)for x in linha.split(',')]
      linha=input()
      M.append(L)
    return M

def ImprimeListaFloat(L):
   '''
   Recebe uma lista de valores reais
   Imprime os valores com uma casa decimal separados por vírgula
   '''
   s=''
   for x in L:
     s=s+'%.1f'%x+', '
   print(s[:-2])
   
# Escreva aqui todas as funções que faltam para que o programa funcione
    
