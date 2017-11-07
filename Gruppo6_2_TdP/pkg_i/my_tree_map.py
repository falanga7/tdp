from TdP_collections.map.binary_search_tree import TreeMap
from TdP_collections.queue.array_queue import ArrayQueue


class MyTreeMap(TreeMap):

    class _Node(TreeMap._Node):
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_successor', '_predecessor'  # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None, successor=None, predecessor=None):
            super().__init__(element, parent, left, right)
            self._successor = successor
            self._predecessor = predecessor

    def __init__(self):
        super().__init__()
        self._max = None
        self._min = None

    def before(self, p):
        """Return the Position just before p in the natural order.

        Return None if p is the first position.
        """
        node = self._validate(p)
        return self._make_position(node._predecessor)

    def after(self, p):
        """Return the Position just after p in the natural order.

        Return None if p is the last position.
        """
        node = self._validate(p)
        return self._make_position(node._successor)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        new = super()._add_left(p, e)
        node = p._node
        node._left._predecessor, node._left._successor = node._predecessor, node
        if not self.is_root(p):
            if node._predecessor is not None:
                node._predecessor._successor = node._left
        if node._predecessor is None:
            self._min = node._left
        node._predecessor = node._left
        return new

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        new = super()._add_right(p, e)
        node = p._node
        node._right._predecessor, node._right._successor = node, node._successor
        if not self.is_root(p):
            if node._successor is not None:
                node._successor._predecessor = node._right
        if node._successor is None:
            self._max = node._right
        node._successor = node._right
        return new

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        element = super()._delete(p)
        node = p._node
        if node._predecessor is not None:
            node._predecessor._successor = node._successor
        if node._successor is not None:
            node._successor._predecessor = node._predecessor
        return element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this alberi.
        Raise ValueError if Position p is invalid or not external.
        """
        node = self._validate(p)
        if not t1.is_empty():
            if t1._max is None:
                t1._max = t1.root()._node
            t1._max._successor = node
            node._predecessor = t1._max
        if not t2.is_empty():
            if t2._min is None:
                t2._min = t1.root()._node
            t2._min._predecessor = node
            node._successor = t2._min
        super()._attach(p, t1, t2)

    def LCA(self, p, q):
        """Return the position of the common ancestor."""
        self._validate(p)
        self._validate(q)
        root = self.root()

        while not self.is_leaf(root):
            if root.key() > p.key() and root.key() > q.key():
                root = self.left(root)
            elif root.key() < p.key() and root.key() < q.key():
                root = self.right(root)
            else:
                return root

    def breadthfirst(self):
        """Iterator breadth first of Tree Positions"""
        if not self.is_empty():
            fringe = ArrayQueue()
        fringe.enqueue(self.root())
        while not fringe.is_empty():
            p = fringe.dequeue()
            yield p
            if p is not None:
                fringe.enqueue(self.left(p))
                fringe.enqueue(self.right(p))

    def __str__(self):
        if self.is_empty():
            raise ValueError("L'abero è vuoto.")
        for p in self.breadthfirst():
            if p is None:
                to_print += ",#"
            elif self.is_root(p):
                to_print = '{' + str(p.key())
            else:
                to_print += "," + str(p.key())
        to_print += "}"
        return to_print


