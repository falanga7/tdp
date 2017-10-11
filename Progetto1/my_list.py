from .double_linked_list import DoubleLinkedList


class MyList(DoubleLinkedList):
    """Implementazione di list di python, usando le DoubleLinkedList"""

    class _Node:

        __slots__ = 'element', 'left', 'right'

        def __init__(self, element, left, right):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self):
        self._head = None                                      # puntatore nodo testa della lista
        self._tail = None                                      # puntatore nodo coda della lista
        self._size = 0                                         # dimensione della lista
        self._reverse = False                                  # ordine di lettura default SX->DX

    def append(self, x):

        new = self._Node(x, None, None)                        # creazione nodo

        if not self._head:
            self._head = new
            self._tail = new

        elif not self._reverse:
            new.left=self._tail
            self._tail.right = new
            self._tail = new

        else:
            new.right = self._tail
            self._tail.left = new
            self._tail = new
        self._size += 1

    def __len__(self):
        return self._size

    def __getitem__(self, j):
        cnt = 0
        if j<0: j+=self._size
        if j<0 or j>=self._size:
            raise IndexError()
        current = self._head._right if (not self._reverse) else self._head._left
        while(current!=None):
            if cnt==j:
                return current
            else:
                cnt += 1
                if not self._reverse:
                    current = current._right
                else:
                    current = current._left
'''
    ##Eccezione se i
    def insert(self,i,x):           #aggiungere eccezione se i non è compreso tra 0 e la dimensione della lista?

        if(i==0):                   #inserimento in testa
            self.reverse()
            self.append(x)
            self.reverse()
        elif(i==self._size):        #inserimento in coda (append)
            self.append(x)
        elif (i>0 and i<self._size):   #inserimento all'interno della lista
            """new = self._Node(x,None,None)  # creazione nodo
            position = 0            # scorro gli elementi della lista
            current = self._head.right if (not self._reverse) else self._head.left
            while (position<i-1):
                if(not self._reverse):
                    current = current.right
                else:
                    current = current.left
                position += 1
            if(not self._reverse):
                new.right = current.right
                new.left = current
                current.right.left = new
                current.right = new
            else:
                new.left = current.left
                new.right = current
                current.left.right = new
                current.left = new"""
            new = self._Node(x, None, None)
            current = iter(self)
            position = 0
            while(position<i):
                next(current)
                position+=1

            if (not self._reverse):
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

    def count(self,x):
        count = 0
        list = iter(self)
        for element in list:
           if(element._element is x):
               count += 1
        return count  '''

