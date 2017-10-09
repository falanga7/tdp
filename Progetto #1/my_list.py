class MyList:


    class Node:
        def __init__(self,element,left,right):
            self._left = left
            self._element = element
            self._right = right


    def __init__(self):
        self._head = None           #puntatore al primo nodo
        self._tail = None
        self._size = 0              #dimensione della lista
        self._fromLeft = True       #ordine di lettura SX->DX

    def append(self,x):

        new = self.Node(x,None,None)       #creazione nodo

        if(len(self)==0):                     #lista vuota
            self._head = new
            self._tail = new
        else:
            if(self._fromLeft):
                self._tail._right = new
                new._left = self._tail                 #aggiorno il link sinistro dell'ultimo nodo
                self._tail = new
            else:
                self._tail._left = new
                new._right = self._tail  # aggiorno il link sinistro dell'ultimo nodo
                self._tail = new
        self._size += 1

    ##DA MODIFICARE
    def insert(self,i,x):           #aggiungere eccezione se i non è compreso tra 0 e la dimensione della lista?

        if(i==0):                   #inserimento in testa
            new = self.Node(x,None,self._head)          # creazione nodo
            self._head._left = new
            self._head = new
        elif(i==self._size):        #inserimento in coda (append)
            self.append(x)
        elif (i>0 and i<self._size):   #inserimento all'interno della lista
            new = self.Node(x,None,None)  # creazione nodo
            position = 0            # scorro gli elementi della lista
            node = self._head
            while (position<i):
                if(self._fromLeft):
                    node = node._right
                else:
                    node = node._left
                position += 1
            if(self._fromLeft):
                new._right = node
                new._left = node._left
                node._left = new
            else:
                new._left = node
                new._right = node._right
                node._right = new
        self._size +=1

    def __len__(self):
        return self._size


    def __getitem__(self, j):
        cnt = 0
        if j<0: j=self._size
        if j<0 or j>self._size:
            raise IndexError()
        current = self._head
        while(current!=None):
            if cnt==j:
                return current
            else:
                cnt += 1
                if self._fromLeft:
                    current = current._right
                else:
                    current = current._left

    def __str__(self):
        toReturn = '<'
        current = self._head
        while current != None:
            toReturn += str(current._element)
            if self._fromLeft:
                current = current._right
            else:
                current = current._left
            if current != None:
                toReturn += ',	'
        toReturn += '>'
        return toReturn


    def reverse(self):

        if (self._tail == self._head or bool(self)== False):
            return

        tmp = self._head
        self._head = self._tail
        self._tail = tmp
        self._fromLeft = False



a = MyList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
print(a)
a.reverse()
print(a.count(1))