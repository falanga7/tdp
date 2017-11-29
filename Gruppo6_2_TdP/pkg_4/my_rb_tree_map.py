from TdP_collections.map.red_black_tree import RedBlackTreeMap
from TdP_collections.queue.array_queue import ArrayQueue


class MyRBTreeMap(RedBlackTreeMap):
    # -------------------------- nested _Node class --------------------------
    class _Node(RedBlackTreeMap._Node):
        """Node class for red-black squadreT maintains bit that denotes color."""
        __slots__ = '_left_size', '_right_size'  # add additional data member to the Node class

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._left_size = 0
            self._right_size = 0

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            self._update_sizes(p, -1)
            if k == p.key():
                self.delete(p)  # rely on positional version
                return  # successful deletion complete
            self._rebalance_access(p)  # hook for balanced squadreT subclasses
        raise KeyError('Key Error: ' + repr(k))

    def _rotate(self, p):
        """Rotate Position p above its parent.

        Switches between these configurations, depending on whether p==a or p==b.

              b                  a
             / \                /  \
            a  t2             t0   b
           / \                     / \
          t0  t1                  t1  t2

        Caller should ensure that p is not the root.
        """
        """Rotate Position p above its parent."""
        x = p._node
        y = x._parent  # we assume this exists
        z = y._parent  # grandparent (possibly None)
        if z is None:
            self._root = x  # x becomes root
            x._parent = None
        else:
            self._relink(z, x, y == z._left)  # x becomes a direct child of z
        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True)  # x._right becomes left child of y
            self._relink(x, y, False)  # y becomes right child of x
            y._left_size = x._right_size
            x._right_size = y._left_size + y._right_size + 1
        else:
            self._relink(y, x._left, False)  # x._left becomes right child of y
            self._relink(x, y, True)  # y becomes left child of x
            y._right_size = x._left_size
            x._left_size = y._left_size + y._right_size + 1

    def _rebalance_insert(self, p):
        # walk = p
        # parent = self.parent(walk)
        # while parent is not None:  # keep walking parent
        #     if self.left(parent) == walk:
        #         parent._node._left_size += 1
        #     else:
        #         parent._node._right_size += 1
        #     walk = parent
        #     parent = self.parent(walk)
        self._update_sizes(p, 1)
        self._resolve_red(p)  # new node is always red

    def _black_depth(self):
        """Return black depth of RB Tree."""
        walk = self.root()
        if walk is None:
            return 0
        black_depth = 1
        while self.left(walk) is not None or self.right(walk) is not None:  # keep walking left
            left = self.left(walk)
            right = self.right(walk)
            walk = left if left is not None else right
            if not super()._is_red(walk):
                black_depth += 1
        return black_depth

    def _find_black_parent_right(self, bd1):
        """Return black position of specified depth on right of root."""
        bd = self._black_depth()
        if bd < bd1:
            raise ValueError("La profondità specificata è più grande di quella dell'albero.")
        if bd1 == 0:
            return self.root()
        walk = self.root()
        d_bd = bd - bd1 - 1
        while d_bd != 0:
            walk = self.right(walk)
            if not super()._is_red(walk):
                d_bd -= 1
        return walk

    def _find_black_parent_left(self, bd1):
        """Return black position of specified depth on left of root."""
        bd = self._black_depth()
        if bd < bd1:
            raise ValueError("La profondità specificata è più grande di quella dell'albero.")
        if bd1 == 0:
            return self.root()
        walk = self.root()
        d_bd = bd - bd1 - 1
        while d_bd != 0:
            walk = self.left(walk)
            if not super()._is_red(walk):
                d_bd -= 1
        return walk

    def fusion(self, t1):
        if t1.is_empty():
            return
        elif self.is_empty():
            self._root = t1._root
            self._size = t1._size
            t1._root = None
            t1._size = 0
            return
        maxt = self.last()                               # O(logn)
        mint1 = t1.first()                               # O(logm)
        if mint1.key() < maxt.key() or mint1 is None:
            raise ValueError("Le chiavi dell'albero passato non sono maggiori delle chiavi di quest'albero.")
        len1 = len(self)
        len2 = len(t1)
        node = t1._validate(mint1)
        del t1[mint1.key()]                                # O(logm)
        bd_t = self._black_depth()  # O(logn)
        bd_t1 = t1._black_depth()  # O(logm)
        len2 -= 1
        node._parent = None

        if bd_t == bd_t1:
            self._root._parent = node
            node._left = self._root
            node._left_size = len1
            self._root = node
            t1._root._parent = node
            node._right_size = len2
            node._right = t1._root
            self._size = len1 + len2 + 1
        elif t1._root is None:
            self[mint1.key()] = mint1.value()
           # self._set_black(self.find_position(mint1.key()))
        elif bd_t > bd_t1:
            bp = self._validate(self._find_black_parent_right(bd_t1))  # O(log(m))
            node._left = bp._right
            bp._right = node
            node._left_size = bp._right_size
            bp._right_size += len2 + 1
            node._parent = bp
            node._right = t1._root
            t1._root._parent = node
            node._right_size = len2 -1
            node._red = True
            self._size = len1 + len2 + 1
            self._update_sizes(self._make_position(bp), bp._right_size)
        elif bd_t < bd_t1:
            bp = t1._validate(t1._find_black_parent_left(bd_t))  # O(log(m))
            node._right = bp._left
            bp._left._parent = node
            bp._left = node
            node._right_size = bp._left_size
            bp._left_size += len1 + 1
            node._parent = bp
            node._left = self._root
            self._root._parent = node
            node._left_size = len1
            node._red = True
            self._size = len1 + len2 + 1
            t1._update_sizes(t1._make_position(bp), bp._left_size)
            self._root = t1._root

        t1._root = None
        t1._size = 0

    def _update_sizes(self, p, size):
        walk = p
        parent = self.parent(walk)
        while parent is not None:  # keep walking parent
            if self.left(parent) == walk:
                parent._node._left_size += size
            else:
                parent._node._right_size += size
            walk = parent
            parent = self.parent(walk)

    def split(self, k):
        p = self.find_position(k)                       # O(logn)
        if p is None or p.key() != k:
            raise ValueError("La chiave k non appartiene all'albero.")
        node = self._validate(p)
        t1 = MyRBTreeMap()
        t2 = MyRBTreeMap()
        if node._left is not None:
            t1._root = node._left
            t1._size = node._left_size
        if node._right is not None:
            t2._root = node._right
            t2._size = node._right_size
        walk = p
        parent = self.parent(walk)
        if t1._root is not None:
            t1._root._parent = None
        if t2.root() is not None:
            t2._root._parent = None
        while parent is not None:  # keep walking parent
            if self.left(parent) == walk:
                parentTree = MyRBTreeMap()
                parentTree._root = parent._node
                parentTree._size = parent._node._right_size + 1
                parentTree._root._parent = None
                parentTree._root._left_size = 0
                parentTree._root._left = None
                parent._node._left = None
                parentTree[t1.root().key()] = t1.root().value()
                del t1[t1.root().key()]
                if t2._root is not None:
                    t2.fusion(parentTree)
                else:
                    t2 = parentTree
            else:
                parentTree = MyRBTreeMap()
                ancestor = parent._node._parent
                parentTree._root = parent._node
                parentTree._size = parent._node._left_size + 1
                parentTree._root._parent = None
                parentTree._root._right_size = 0
                parentTree._root._right = None
                parent._node._right = None
                t1[parentTree.root().key()] = parentTree.root().value()
                del parentTree[parentTree.root().key()]
                if t1._root is not None:
                    parentTree.fusion(t1)
                    t1 = parentTree
                else:
                    t1 = parentTree._root
                    t1._size = parentTree._size
                parent._node._parent = ancestor

            self._root._parent = None
            walk = parent
            parent = self.parent(walk)
        if t1._root is not None:
            t1._root._parent = None
        if t2._root is not None:
            t2._root._parent = None
        self._root = None
        self._size = 0
        return t1, t2

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
            elif self._is_red(p):
                to_print += ",\033[1;31;0m" + str(p.key()) + "\033[0m"
            else:
                to_print += "," + str(p.key())
        to_print += "}"
        return to_print

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this alberi.
        Raise ValueError if Position p is invalid or not external.
        """

        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():         # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            node._left_size = len(t1)
            t1._root = None             # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():         # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            node._right_size = len(t2)
            t2._root = None             # set t2 instance to empty
            t2._size = 0
        self._update_sizes(p, len(t1) + len(t2))
