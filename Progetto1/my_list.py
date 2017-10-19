from .double_linked_list import DoubleLinkedList


class MyList(DoubleLinkedList):

    class _Node:

        __slots__ = '_left', '_element', '_right'

        def __init__(self, element, left=None, right=None):
            self._left = left
            self._element = element
            self._right = right

    def __init__(self, my_list=None):

        self._head = self._Node(None)                                           # nodo testa della lista
        self._tail = self._Node(None)                                           # nodo coda della lista
        self._head._right = self._tail
        self._tail._left = self._head
        self._reverse = False                                                   # ordine di lettura default SX->DX
        self._size = 0                                                          # dimensione della lista
        if my_list is None:
            return
        else:
            try:
                object_iterator = iter(my_list)
            except TypeError:
                print(my_list, 'La sequenza passata non è iterabile o valida.')
            for element in object_iterator:
                self.append(element)


    def append(self, x):

        new = self._Node(x)                                                 # creazione nodo

        if not self._reverse:
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


    def insert(self, i, x):

        i = i if i >= 0 else self._size + i
        #if i > self._size:
            #raise IndexError("L'indice scelto non risulta essere nel range della sequenza")

        if i >= self._size:                                             # inserimento in coda
            self.append(x)
        else:                                                             # inserimento all'interno della lista
            new = self._Node(x)
            position = 0
            node_iterator = self._nodes()
            current = self._head
            while position < i:
                current = next(node_iterator)
                position += 1
            if not self._reverse:
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


            # if i < 0: i += self._size

    # if i < 0 or i >= self._size:
    #     raise IndexError()
    # if(i==0):                   #inserimento in testa
    #     self.reverse()
    #     self.append(x)
    #     self.reverse()
    # elif(i==self._size):        #inserimento in coda (append)
    #     self.append(x)
    # elif (0 < i < self._size):   #inserimento all'interno della lista
    #     new = self._Node(x)
    #     position = 0
    #     current = self._nodes()
    #     while (position < i ):
    #         current = next(current)
    #         position += 1
    #     if (not self._reverse):
    #         new._right = current._right
    #         new._left = current
    #         current._right._left = new
    #         current._right = new
    #     else:
    #         new._left = current._left
    #         new._right = current
    #         current._left._right = new
    #         current._left = new
    #     self._size += 1

    def extend(self, iterable):

        for element in iterable:
            if element is not None:
                self.append(element)


    def remove(self, x):

        i = self.index(x)
        self.__delitem__(i)


    def pop(self, i=None):
        if i is None:
            i = self._size - 1
        elif i < 0:
            i = self._size + i
        if i >= self._size:
            raise IndexError("L'indice specificato non è valido.")
        return self._remove_item(i, printable=True)

    def clear(self):
        self.__del__()


    def index(self, x, start=0, end=None):

        if end is None:
            end = self._size - 1
        elif start < 0 and end < 0:
            start = self._size + start
            end = self._size + end
        elif not (start > 0 and end > 0):
            raise ValueError("Il range inserito non è accettato.")

        position = 0
        nodes = self._nodes()
        for current in nodes:
            if start <= position <= end:
                if current._element == x:
                    return position
            position += 1
        raise ValueError("L'elemento cercato non è stato trovato.")


    def count(self, x):
        count = 0
        list_iterator = iter(self)
        for element in list_iterator:
            if element is x:
                count += 1

        return count


    def sort(self, key=None, reverse=False):

        self._insertion_sort(key)

        if reverse:
            self.reverse()


    def reverse(self):
        self._head, self._tail = self._tail, self._head
        self._reverse = True if (not self._reverse) else False


    def copy(self):
        copia = MyList()
        list = self._nodes()
        for current in list:
            copia.append(current._element)
        return copia


    #Operatori


    def __add__(self, other):
        copia = self.copy()
        copia.extend(other)
        return copia


        i = 0
        for elementB in b:
            if self[i] != elementB:
                return False
            i += 1
        return True


    def __iadd__(self, other):
        self.extend(other)
        return self



    def __le__(self, b):

        i = 0
        min = self._size if self._size < b._size else b._size
        while i != min:
            if self[i] < b[i]:
                return True
            elif self[i] > b[i]:
                return False
            i += 1
        if self._size < b._size:
            return False

        return True

    def __lt__(self,  b):

        i = 0
        min = self._size if self._size < b._size else b._size
        while i != min:
            if self[i] < b[i]:
                return True
            elif self[i] > b[i]:
                return False
            i += 1
        if self._size <= b._size:
            return False

        return True

    def __eq__(self, b):

        if self._size != b._size:
            return False


    def __ne__(self, b):
        return not self.__eq__(b)


    def __ge__(self, b):

        i = 0
        min = self._size if self._size < b._size else b._size
        while i != min:
            if self[i] > b[i]:
                return True
            elif self[i] < b[i]:
                return False
            i += 1
        if self._size < b._size:
            return False

        return True

    def __gt__(self, b):
        i = 0
        min = self._size if self._size < b._size else b._size
        while i != min:
            if self[i] > b[i]:
                return True
            elif self[i] < b[i]:
                return False
            i += 1
        if self._size <= b._size:
            return False

        return True


    def __contains__(self, a, b):

        for node in a:
            if node._element == b:
                return True
        return False


    def __delitem__(self, k):
        self._remove_item(k)


    def __getitem__(self, k):

        if type(k) is slice:
            step = k.step if k.step is not None else 1
            if (step < 0):
                start = k.start if k.start is not None else len(self)
                stop = k.stop if k.stop is not None else -1
            else:
                start = k.start if k.start is not None else 0
                stop = k.stop if k.stop is not None else len(self)

            return MyList(self.__getitem__(i) for i in range(start, stop, step))

        kabs = k if k >= 0 else -k
        if kabs > self._size - 1:
            raise IndexError("L'indice scelto non risulta essere nel range della sequenza")

        if k >= 0:
            j = 0
            current = self._head._right if not self._reverse else self._head._left
            while j != kabs:
                current = current._right if not self._reverse else current._left
                j += 1
        else:
            j = 1
            current = self._tail._left if not self._reverse else self._tail._right
            while j != kabs:
                current = current._left if not self._reverse else current._right
                j += 1

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

        if type(k) is slice:
            if(k.start == self.__len__() and k.stop is None and k.step is None):
                self.extend(v)
                return

            step = k.step if k.step is not None else 1
            if (step < 0):
                start = k.start if k.start is not None else len(self)
                stop = k.stop if k.stop is not None else -1
            else:
                start = k.start if k.start is not None else 0
                stop = k.stop if k.stop is not None else len(self)

            for i in range(start, stop, step):
                self.__setitem__(i, v)
            return
        kabs = k if k >= 0 else -k

        if kabs >= self._size :
            raise IndexError("L'indice scelto non risulta essere nel range della sequenza")


        if k >= 0:
            j = 0
            current = self._head._right if not self._reverse else self._head._left
            while j != kabs:
                current = current._right if not self._reverse else current._left
                j += 1
        else:
            j = 1
            current = self._tail._left if not self._reverse else self._tail._right
            while j != kabs:
                current = current._left if not self._reverse else current._right
                j += 1

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


    def __del__(self):

        i = 0
        while i < self._size:
            self.__delitem__(i)
        self._head._left = None
        self._head._right = self._tail
        self._tail._left = self._head
        self._tail._right = None
        self._reverse = False



    def __len__(self):
        """Implementando l'oparatore "len" python ci offre gratis l'operatore bool."""
        return self._size



    def __str__(self):

        to_return = '['
        nodes_iterator = self._nodes()
        i = 0
        while i != self._size:
            current = next(nodes_iterator)
            if i == self._size-1:
                to_return += str(current._element)
            else:
                to_return += str(current._element) + ", "
            i += 1

        return to_return + "]"
        # to_return = '<'
        # current = self._head._right if (not self._reverse) else self._head._left
        # while current != self._tail:
        #     to_return += str(current._element)
        #     if not self._reverse:
        #         current = current._right
        #     else:
        #         current = current._left
        #     if current != self._tail:
        #         to_return += ',	'
        # to_return += '>'
        # return to_return


    def _remove_item(self, key, printable=False):
        position = 0
        nodes = self._nodes()
        current = next(nodes)
        while current != self._tail:
            if position is key:
                if not self._reverse:
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


    def _nodes(self):
        current = self._head._right if (not self._reverse) else self._head._left
        while current != self._tail:
            yield current
            if not self._reverse:
                current = current._right
            else:
                current = current._left


    def _insertion_sort(self,key = None):

        ordered = MyList()
        ordered.append(self[0])
        i = 1
        while i < len(self):
            k = len(ordered) - 1
            while True:
                if key != None:
                    c_list = key(self[i])
                    o_list = key(ordered[k])
                else:
                    c_list = self[i]
                    o_list = ordered[k]
                if c_list > o_list:
                    ordered.insert(k + 1, self[i])
                    break
                elif c_list == o_list:
                    ordered.insert(k + 1, self[i])
                    break
                elif c_list < o_list:
                    k = k - 1
                    if k < 0:
                        ordered.insert(0, self[i])
                        break
            i += 1
        self.__init__(ordered)

