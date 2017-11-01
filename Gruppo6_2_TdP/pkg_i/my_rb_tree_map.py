from ..TdP_collections.map.red_black_tree import RedBlackTreeMap


class MyRBTreeMap(RedBlackTreeMap):
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


