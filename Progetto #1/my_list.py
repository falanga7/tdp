from .doublelinkedlist import  DoubleLinkedList

class MyList(DoubleLinkedList):


    class Node:
        def __init__(self,element,left,right):
            self._left = left
            self._element = element
            self._right = right


    def __init__(self):
        self._head = self.Node(None,None,None)           #nodo testa della lista
        self._tail = self.Node(None,None,None)           #nodo coda della lista
        self._head._right = self._tail
        self._tail._left = self._head
        self._size = 0                                   #dimensione della lista
        self._reverse = False                            #ordine di lettura default SX->DX

    def append(self,x):

        new = self.Node(x,None,None)       #creazione nodo

        if(not  self._reverse):
            new._right = self._tail
            prev = self._tail._left
            self._tail._left = new
            prev._right = new
            new._left = prev
        else:
            new._left = self._tail
            prev = self._tail._right
            self._tail._right = new
            prev._left = new
            new._right = prev
        self._size += 1

    ##Eccezione se i
    def insert(self,i,x):           #aggiungere eccezione se i non è compreso tra 0 e la dimensione della lista?

        if(i==0):                   #inserimento in testa
            self.reverse()
            self.append(x)
            self.reverse()
        elif(i==self._size):        #inserimento in coda (append)
            self.append(x)
        elif (i>0 and i<self._size):   #inserimento all'interno della lista
            new = self.Node(x,None,None)  # creazione nodo
            position = 0            # scorro gli elementi della lista
            current = self._head._right if (not self._reverse) else self._head._left
            while (position<i-1):
                if(not self._reverse):
                    current = current._right
                else:
                    current = current._left
                position += 1
            if(not self._reverse):
                new._right = current._right
                new._left = current
                current._right._left = new
                current._right = new
            else:
                new._left = current._left
                new._right = current
                current._left._right = new
                current._left = new
            self._size += 1

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
        current = self._head._right if (not self._reverse) else self._head._left
        while current != self._tail:
            toReturn += str(current._element)
            if not self._reverse:
                current = current._right
            else:
                current = current._left
            if current != self._tail:
                toReturn += ',	'
        toReturn += '>'
        return toReturn


    def reverse(self):
        self._head,self._tail = self._tail,self._head
        self._reverse = True if (not self._reverse) else False



a = MyList()
a.reverse()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
print(a)
a.append(7)
print(a)
print(a)
a.insert(1,'100')
a.insert(2,'200')
a.insert(len(a)-1,'300')
a.insert(len(a)-3,'400')
print(len(a))
print(a)