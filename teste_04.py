#antes:  [0,1,2,3,4,5]
#depois: [5,1,3,2,4,0]
#Encontros: 0 -> 5 ; 2 -> 3

dic_troca = {}
lista_teste = [1,3,5,2,4,6]
tam = len(lista_teste)
par_indices = []
impar_indices = []
def busca_par():
    for p in range(tam):
        if(lista_teste[p] % 2 == 0):
            par_indices.append(p)
def buscar_impar():
    for i in range(tam-1, 0, -1):
        if(lista_teste[i] % 2 != 0):
            impar_indices.append(i)

busca_par()
buscar_impar()
relaciona = zip(par_indices, impar_indices)
for relacao in relaciona:
    if(relacao[0] < relacao[1]):
        trocar_1 = lista_teste[relacao[0]]
        trocar_2 = lista_teste[relacao[1]]
        lista_teste[relacao[0]] = trocar_2
        lista_teste[relacao[1]] = trocar_1

print(lista_teste)

