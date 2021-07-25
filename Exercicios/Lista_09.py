##### Exercício 09 #####
'''
    Neste exercício criaremos uma classe de nome Reta.
    A classe Ponto dada em aula também será utilizada, portanto copie no corpo do programa
    O programa principal possui opções e deve ser completado.
    
    ===== Opções: =====
    0: sair
    1: criar reta
    2: calcula f(x) dado x
    3: calcula área dado intervalo
    4: calcula perpendicular passando por ponto
    5: calcula interseção com outra reta
    6: calcula distância ao ponto
    
    Exemplo de execução:
    
    opção: 1
    a: -2
    b: -2
    Reta -2.0x-2.0
    opção: 2
    x: 4
    resultado: -10.0
    opção: 3
    início do intervalo: -5
    final do intervalo: -3
    resultado: 12.0
    opção: 4
    x: 5
    y: -2
    Reta 0.5x-4.5
    opção: 5
    a: 0.5
    b: -4.5
    Ponto em (1.0,-4.0)
    opção: 6
    x: 5
    y: -2
    resultado: 4.5
    opção: 0
'''
##### Classes ######
class Ponto:
    '''
    Atributos:
    x : coordenada no eixo x
    y : coordenada no eixo y
    
    Métodos:
    dist() : calcula a distância para outro ponto
    '''
    # copie o que foi dado em aula aqui
    
class Reta:
    ''' Coloque a descrição aqui
    '''
    # escreva aqui o construtor:
    
    # escreva aqui a representação para o print
    
    # escreva aqui os demais métodos

##### principal: #####
while True:
  opcao=input('opção: ')
  try:
    opcao=int(opcao)
    if opcao==1:
      # criar reta
      a=float(input('a: '))
      b=float(input('b: '))
      r=Reta(a,b)
      print(r)
    elif opcao==2:
      # calcula f(x) dado x
      
    elif opcao==3:
      # calcula área dado intervalo
      
    elif opcao==4:
      # calcula perpendicular passando por ponto
      
    elif opcao==5:
      # calcula interseção com outra reta
      
    elif opcao==6:
      # calcula distância ao ponto
      
    elif opcao==0:
      break
    else:
      print('A opção não é válida.')
      
  except:
    print('===== Opções: =====')
    print('0: sair')
    print('1: criar reta')
    print('2: calcula f(x) dado x')
    print('3: calcula área dado intervalo')
    print('4: calcula perpendicular passando por ponto')
    print('5: calcula interseção com outra reta')
    print('6: calcula distância ao ponto')