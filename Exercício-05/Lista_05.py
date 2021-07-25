##### Exercício 05 #####
'''
    Este exercício faz uma adaptação de ifs.py do livro Introduction to Programming in Python
    de Sedgewick tornando-o uma função contida em MeuModulo.py e portanto,
    as funções devem estar no outro arquivo e não neste.
    Neste arquivo está apenas o programa principal que:
    - inicializa random seed
    - realiza a leitura dos dados
    - chama a função ifs()
    - imprime as listas X e Y
    - plota os pontos com a biblioteca matplotlib (não funciona no moodle.
      Esta parte está comentada com hashtags, descomente para fazer funcionar em
      outra plataforma). Para formar figuras o número de iterações deve ser por volta de 1000
'''
##### Bibliotecas #####
import random
import matplotlib.pyplot as plt
import MeuModulo as MeMo # MeMo.funcãoBlabla é como você deve chamar as funções

random.seed(0) # não modifique esta linha para que o exercício dê as mesmas respostas nos testes

# Leitura dos valores de entrada:
n=int(input('iterações: '))
print('Probabilidades: ',end='')
p=MeMo.LeListaFloat()
print('cx: ',end='')
cx=MeMo.LeMatriz()
print('cy: ',end='')
cy=MeMo.LeMatriz()

# escreva aqui a chamada da função ifs():

# impressão das listas:
MeMo.ImprimeListaFloat(X)
MeMo.ImprimeListaFloat(Y)

# Plot do gráfico:
#plt.scatter(X,Y,marker='.',c='deeppink',alpha=0.5)
#plt.grid()
#plt.xlabel("Eixo X")
#plt.ylabel("Eixo Y")
#plt.show()
# Veja documentação em https://matplotlib.org/stable/api/pyplot_summary.html