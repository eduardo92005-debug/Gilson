


class Graph:
    def __init__(self):
        self.__adj = dict()
        self.__e = 0

    def add_vertex(self, v):
        if v not in self.__adj:
            self.__adj[v] = set()

    @property
    def vertices(self):
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
    def adjacent(self,v):
        return list(self.__adj[v])


class Node:
    def __init__(self, item, _next):
        self.item = item
        self.next = _next


class Paciente:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
        self.__hospital = None
        self.__prioridade = None

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
        object_text = "Id: %d Nome: %s" % (self.__id, self.__nome)
        return object_text


class Queue:
    def __init__(self):
        self.__start = None
        self.__end = None
        self.__n = 0

    def is_empty(self):
        return self.__n == 0

    def __len__(self):
        return self.__n

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

G = Graph()
for v in ['v1','v2','v3']:
    G.add_vertex(v)
G.add_edge('v4','v5')
print(G.vertices)
print(G.adjacent('v4'))
