##### ExercIcio 08 #####
'''
Função que calcula recursivamente o número de infectados de um vírus num dia
Exemplo de execução do programa principal:

infectados inicial: 1
índice de reprodutibilidade: 2
dia: 6
resultado: 32.0

'''
##### função #####
def Infectados(x,I0,r):
    '''
    Recebe:
    x : o dia a ser calculado o número de infectados
    I0 : o número de pessoas infectadas no dia 1
    r : o índice de reprodutibilidade do vírus
    
    Retorna: o número de infectados no dia x
    '''
    #escreva a função aquiv
    
    if x == 1:
      return I0
    else:
      return r**(x-2) + Infectados(x-1,I0,r)
    
##### principal #####    
def main():
  I0=int(input('infectados inicial: '))
  r=float(input('índice de reprodutibilidade: '))
  x=int(input('dia: '))
  # complete o código
  Infect=Infectados(x,I0,r)
  print('resultado: %.1f'%Infect)
  

  
main()
