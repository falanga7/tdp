from .double_linked_list import DoubleLinkedList


class MyList(DoubleLinkedList):

    class _Node:

        __slots__ = '_left', '_element', '_right'

        def __init__(self, element, left=None, right=None):
            self._left = left
            self._element = element
            self._right = right

    def __init__(self):
        self._head = self._Node(None)                                       # nodo testa della lista
        self._tail = self._Node(None)                                       # nodo coda della lista
        self._head._right = self._tail
        self._tail._left = self._head
        self._size = 0                                                      # dimensione della lista
        self._reverse = False                                               # ordine di lettura default SX->DX

    def append(self,x):

        new = self._Node(x)                                                 # creazione nodo

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

        if i < 0: i += self._size
        if i < 0 or i >= self._size:
            raise IndexError()
        if(i==0):                   #inserimento in testa
            self.reverse()
            self.append(x)
            self.reverse()
        elif(i==self._size):        #inserimento in coda (append)
            self.append(x)
        elif (0 < i < self._size):   #inserimento all'interno della lista
            new = self._Node(x)
            position = 0
            current = self._nodes()
            while (position < i ):
                current = next(current)
                position += 1
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

    def __len__(self):
        return self._size


    def index(self,x,start=0,end=None):

        if end is None:
            end = self._size-1

        position = 0
        nodes = self._nodes()
        for current in nodes:
            if(position>=start and position<=end):
                if (current._element is x):
                    return position
            position += 1
        return False

    def __getitem__(self, k):

        kabs = k if k >= 0 else -k
        if kabs > self._size:
            raise IndexError("L'indice scelto non risulta essere nel range della sequenza")

        if k >= 0:
            current = self._head._right if not self._reverse else self._head._left
            for kabs in range(kabs):
                current= current.right if not self._reverse else current._left
        else:
            current= self._tail._left if not self._reverse else self._tail._right
            for kabs in range(1, kabs):
                current = current._left if not self._reverse else current._right

        return current._element


        # cnt = 0
        # if j<0: j+=self._size
        # if j<0 or j>=self._size:
        #     raise IndexError()
        # current = self._head._right if (not self._reverse) else self._head._left
        # while(current!=self._tail):
        #     if cnt==j:
        #         return current._element
        #     else:
        #         cnt += 1
        #         if not self._reverse:
        #             current = current._right
        #         else:
        #             current = current._left

    def __setitem__(self, k, v):

        kabs = k if k >= 0 else -k
        if kabs > self._size:
            raise IndexError("L'indice scelto non risulta essere nel range della sequenza")

        if k >= 0:
            current = self._head._right if not self._reverse else self._head._left
            for kabs in range(kabs):
                current= current.right if not self._reverse else current._left
        else:
            current= self._tail._left if not self._reverse else self._tail._right
            for kabs in range(1, kabs):
                current = current._left if not self._reverse else current._right

        current._element = v

        # cnt = 0
        # if key<0: key+=self._size
        # if key==self._size:
        #     self.append(value)
        # if key<0 or key>=self._size:
        #     raise IndexError()
        # current = self._head._right if (not self._reverse) else self._head._left
        # while(current!=self._tail):
        #     if cnt==key:
        #         current._element = value
        #         return
        #     else:
        #         cnt += 1
        #         if not self._reverse:
        #             current = current._right
        #         else:
        #             current = current._left



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
           if(element is x):
               count += 1
        return count

    def extend(self,iterable):

        for i in iterable:
            self.append(i)




    """def __contains__(self, item):
        list = iter(self)
        for element in list:
           if(element is item):
               return True
        return False"""


    """def remove(self,x):
        list = iter(self)
        for element in list:
            if (element is item):
                return True
        return False"""

    def __delitem__(self, key):
        self._remove_item(key)

    def __del__(self):

        i = 0
        while(i < self._size):
            self.__delitem__()
        self._head._right = self._tail
        self._tail._left = self._head
        self._reverse = False

    def remove(self,x):

        i = self.index(x)
        self.__delitem__(i)

    def clear(self):
        del self

    def pop(self,i=None):
        if i == None:
            i = self._size-1
        return self._remove_item(i,printable=True)

    def _remove_item(self,key,printable=False):
        position = 0
        nodes = self._nodes()
        current = next(nodes)
        while current != self._tail:
            if (position is key):
                if (not self._reverse):
                    current._left._right = current._right
                    current._right._left = current._left
                else:
                    current._right._left = current._left
                    current._left._right = current._right
                value = current._element
                current._element = None
                current._left = None
                current._right = None
                self._size -= 1
                if printable:
                    return value
                else:
                    return
            position += 1
            current = next(nodes)

    def copy(self):
        copia = MyList()
        list = self._nodes()
        for current in list:
            copia.append(current._element)
        return copia


    def _nodes(self):
        current = self._head._right if (not self._reverse) else self._head._left
        while(current!=self._tail):
            yield current
            if not self._reverse:
                current = current._right
            else:
                current = current._left


