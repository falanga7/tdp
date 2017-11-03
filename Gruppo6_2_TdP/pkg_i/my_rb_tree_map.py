from ..TdP_collections.map.red_black_tree import RedBlackTreeMap


class MyRBTreeMap(RedBlackTreeMap):

    def _black_depth(self):
        """Return black depth of RB Tree."""
        walk = self.root()
        self._black_depth = 1
        while self.left(walk) is not None:  # keep walking left
            walk = self.left(walk)
            if not super()._is_red(walk):
                self._black_depth += 1
        return self._black_depth

    def _find_black_parent(self, bd1):
        """Return black position of specified depth."""
        bd = self._black_depth()
        if bd < bd1:
            raise ValueError("L'altezza specificata è più grande di quella dell'albero.")
        walk = self.root()
        d_bd = bd - bd1 -1
        while d_bd != 0:
            walk = self.right(walk)
            if not super()._is_red(walk):
                d_bd-= 1
        return walk

    def fusion(self, t1):
        maxt = self.last()                               # O(logn)
        mint1 = t1.first()                               # O(logm)
        if mint1 < maxt:
            raise ValueError("Le chiavi dell'albero passato non sono maggiori delle chiavi di quest'albero.")
        bd_t = self._black_depth()                        # O(logn)
        bd_t1 = t1._black_depth()                         # O(logm)
        new_mint1 = self._make_position(mint1)
        del t1[mint1]                                     # O(logm)

        if bd_t == bd_t1:
            t_size = self._size
            t1_size = t1._size
            self._attach(new_mint1, self, t1)
            self._add_root(new_mint1.element())
            self._set_black(self.root())
            self._size = t_size + t1_size + 1
        elif bd_t > bd_t1:
            p = self._find_black_parent(bd_t1)
            mint1_left = p.right()
            self._add_right(p, new_mint1.element())
            self._add_left(new_mint1, mint1_left.element())
            self._add_right(new_mint1, )






    def split(self, k):
        node = self._validate(self.find_position(k))
        T1 = node._left
        T2 = node._right
        node._parent._left = None
        node._left = None
        node._right = None
        if self.is_root(node):
            return T1, T2
        elif node == node._parent._left:
            T2._attach(T2.last(), None, node._parent)
        else:
            T1._attach(T1.last(), node._parent, None)
        node._parent = node
        return T1, T2


