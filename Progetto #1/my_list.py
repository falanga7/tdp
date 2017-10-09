class MyList:


    class Node:
        def __init__(self):
            self._left = None
            self._element = None
            self._right = None


    def __init__(self):
        self._root = None           #puntatore al primo nodo
        self._size = 0              #dimensione della lista

    def append(self,x):

        new = self.Node() #creazione nodo
        new._element = x     #assegno valore x al nodo

        if(len(self)==0):                     #lista vuota
            self._root = new
        else:                                 #lista con almeno un elemento
            last = self._root                  #scorro gli elementi della lista fino alla coda
            while(last._right != None):
                last = last._right
            new._left = last                  #aggiorno il link sinistro dell'ultimo nodo
            last._right = new

        self._size += 1


    def insert(self,i,x):           #aggiungere eccezione se i non è compreso tra 0 e la dimensione della lista?

        if(i==0):                   #inserimento in testa
            new = self.Node()       # creazione nodo
            new._data = x           # assegno valore al nodo
            new._right = self
            self._root._left = new
            self._root = new
        elif(i==self._size):        #inserimento in coda (append)
            self.append(x)
        elif (i>0 and i<self._size):   #inserimento all'interno della lista
            new = self.Node()  # creazione nodo
            new._data = x
            position = 0            # scorro gli elementi della lista
            node = self._root
            while (position<i):
                node = node._right
            new._right = node._right
            node._right = new
            new._left = node._right


    def __len__(self):
        return self._size


    def __bool__(self):
        return self._size>0


    def __getitem__(self, j):
        cnt = 0
        if j<0: j=self._size
        if j<0 or j>self._size:
            raise IndexError()
        current = self._root
        while(current!=None):
            if cnt==j:
                return current
            else:
                cnt += 1
                current = current._rigth
