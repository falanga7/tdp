class MyList:


    class Node:
        def __init__(self):
            self._element = None
            self._left = None
            self._right = None


    def __init__(self):
        self._size = 0


    def append(self,x):

        new = self.Node() #creazione nodo
        new._data = x     #assegno valore al nodo

        if(self == None):                     #lista vuota
            self = new
        else:                                 #lista con almeno un elemento
            last = self.Node                  #scorro gli elementi della lista fino alla coda
            while(last._right != None):
                head = last._right
            new._left = last                  #aggiorno il link sisistro dell'ultimo nodo


    def insert(self,i,x):           #aggiungere eccezione se i non è compreso tra 0 e la dimensione della lista?

        if(i==0):                   #inserimento in testa
            new = self.Node()       # creazione nodo
            new._data = x           # assegno valore al nodo
            new._right = self
        elif(i==self._size):        #inserimento in coda (append)
            self.append(x)
        elif (i>0 and i<self._size):   #inserimento all'interno della lista
            new = self.Node()  # creazione nodo
            new._data = x
            node = self.Node           # scorro gli elementi della lista
            position = 0
            while (position<i):
                node = node._right
            new._right = node._right
            node._right = new
            new._left = node._right
