import networkx as nx


class Graph:
    def __init__(self):
        self.__adj = dict()
        self.__e = 0

    def add_vertex(self, v):
        if v not in self.__adj:
            self.__adj[v] = set()

    @property
    def vertex(self):
        return list(self.__adj.keys())

    def add_edge(self, v, w):
        if v not in self.__adj:
            self.__adj[v] = set()
        if w not in self.__adj:
            self.__adj[w] = set()
        if w not in self.__adj[v]:
            self.__adj[v].add(w)
            self.__adj[w].add(v)
            self.__e += 1

    def adjacent(self, v):
        return list(self.__adj[v])

    def count_vertex(self):
        return len(self.__adj.keys())

    def count_e(self):
        return self.__e

    def degree(self, v):
        return len(self.__adj[v])

    def has_vertex(self, v):
        return v in self.__adj

    def has_edge(self, v, w):
        return w in self.__adj[v]

    def read_graph(self, filename, delimiter=' '):
        with open(filename) as f:
            for line in f:
                line = line.strip()
                items = line.split(delimiter)
                self.add_edge(items[0], items[1])


class Node:
    def __init__(self, item, _next):
        self.item = item
        self.next = _next

    def __repr__(self):
        return '%s %s' % (self.item, self.next)


class Paciente:
    def __init__(self, id, nome, hospital=None, prioridade=None):
        self.__id = id
        self.__nome = nome
        self.__hospital = hospital
        self.__prioridade = prioridade

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def hospital(self):
        return self.__hospital

    @property
    def prioridade(self):
        return self.__prioridade

    @hospital.setter
    def hospital(self, hospital):
        self.__hospital = hospital

    @prioridade.setter
    def prioridade(self, prioridade):
        self.__prioridade = prioridade

    def __repr__(self):
        object_text = "Id: %s Nome: %s" % (self.__id, self.__nome)
        return object_text


class FilaUnica:
    def __init__(self):
        self.__start = None
        self.__end = None
        self.__n = 0

    def is_empty(self):
        return self.__n == 0

    def __len__(self):
        return self.__n

    def insereinicio(self, item):
        aux = Node(item, None)
        aux.next = self.__start
        self.__start = aux
        self.__n += 1

    def inserefim(self, item):
        aux = Node(item, None)
        self.__end.next = aux
        self.__n += 1

    def insere(self, paciente: Paciente):
        prioridade = paciente.prioridade
        prioridade = str(prioridade).upper()
        nome = paciente.nome
        _id = paciente.id
        if(prioridade == 'ALTA'):
            self.insereinicio(f'{_id} {nome}')
        else:
            self.inserefim(f'{_id} {nome}')

    def enqueue(self, item):
        aux = Node(item, None)
        if self.is_empty():
            self.__start = aux
        else:
            self.__end.next = aux
        self.__end = aux
        self.__n += 1

    def dequeue(self):
        x = self.__start.item
        self.__start = self.__start.next
        self.__n -= 1
        if self.__n == 0:
            self.__end = None
        return x

    def mostrar_fila(self):
        if self.is_empty():
            print('Fila vazia!')
        else:
            to_print = f'Fila: inicio {self.__start} fim'.replace('None','')
            print(to_print)

    def localiza(self, id):
        current = self.__start
        found = False
        while current and found is False:
            if current.item == id:
                found = True
                print(f'Paciente {paciente.nome}')
            else:
                current = current.next
        if current is None:
            raise ValueError("Data not in list")
        return current

    def __repr__(self):
        return f'Fila: {self.__start.item[0]} {self.__start.item[1]}'


fila_hospital = FilaUnica()
fila = FilaUnica()
global paciente
while True:
    opcao = input('opção: ')
    opcao = int(opcao)
    if opcao == 1:
        id_pac = input("id:\t")
        nome_pac = input("nome:\t")
        paciente = Paciente(id_pac,nome_pac)
        fila.enqueue(f'{id_pac} {nome_pac}')
    elif opcao == 2:
        prioridade = input('prioridade:\t')
        paciente.prioridade = prioridade
    elif opcao == 3:
        hospital = input('hospital:\t')
        paciente.hospital = hospital
    elif opcao == 4:
        fila_hospital.insere(paciente)
        fila_hospital.mostrar_fila()
    elif opcao == 5:
        pass
    elif opcao == 6:
        pass
    elif opcao == 0:
        break
    else:
        print('A opção não é válida.')

    '''except:
        print('===== Opções: =====')
        print('0: sair')
        print('1: criar paciente')
        print('2: define prioridade do paciente')
        print('3: define hospital do paciente')
        print('4: insere paciente criado na Fila Unica')
        print('5: remove um paciente da fila')
        print('6: localiza paciente')
        print('7: mostra fila unica')'''


def testando():
    # 3
    qu = FilaUnica()
    ########################
    pac1 = Paciente(12, 'Carlos', 'PMM', 'Alta')
    pac2 = Paciente(14, 'Filipe', 'PMM', 'Alta')
    pac3 = Paciente(2, 'Cs', 'HUSE', 'Alta')
    pac4 = Paciente(3, 'Jub', 'HUSE', 'Alta')
    qu.insere(pac1.id)
    qu.insere(pac2.id)
    qu.insere(pac3.id)
    qu.mostrar_fila()
    qu.localiza(3)
    '''
    G = Graph()
    for v in ['v1','v2','v3']:
        G.add_vertex(v)
    G.add_edge('v4','v5')
    print(G.vertex)
    print(G.adjacent('v4'))
    print(G.count_vertex())
    print(G.count_e())
    print(G.degree('v2'))
    print(G.has_vertex('v2'))'''

