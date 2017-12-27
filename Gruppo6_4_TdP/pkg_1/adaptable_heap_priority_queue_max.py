from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


class Empty(Exception):
    pass


class AdaptableHeapPriorityQueueMax(AdaptableHeapPriorityQueue):

    def _bubble(self, j):
        if j > 0 and self._data[j] > self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] > self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recur at position of parent

    def max(self):
        """Return but do not remove (k,v) tuple with max key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def min(self):
        raise NotImplementedError('Il metodo non è implementato in quanto siamo in una max heap priority queue.')

    def remove_min(self):
        raise NotImplementedError('Il metodo non è implementato in quanto siamo in una max heap priority queue.')

    def max(self):
        """Return but do not remove (k,v) tuple with maximum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_max(self):
        """Remove and return (k,v) tuple with maximum key.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)  # put maximum item at the end
        item = self._data.pop()  # and remove it from the list;
        self._downheap(0)  # then fix new root
        return (item._key, item._value)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            big_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    big_child = right
            if self._data[big_child] > self._data[j]:
                self._swap(j, big_child)
                self._downheap(big_child)  # recur at position of small child