def ImprimeListaFloat(L):
   '''
   Recebe uma lista de valores reais
   Imprime os valores com três casas decimais separados por vírgula
   '''
   s=''
   for x in L:
     s=s+'%.1f'%x+', '
   print(s[:-2])
  
