from ..TdP_collections.map.binary_search_tree import TreeMap


class MyTreeMap(TreeMap):

    def before(self, p):
        """Return the Position just before p in the natural order.

        Return None if p is the first position.
        """
        self._validate(p)  # inherited from LinkedBinaryTree
        return self.predecessor(p)

    def after(self, p):
        """Return the Position just after p in the natural order.

        Return None if p is the last position.
        """
        self._validate(p)  # inherited from LinkedBinaryTree
        return self.successor(p)

    def LCA(self, p, q):
        """Return the position of the common ancestor."""
        self._validate(p)
        self._validate(q)
        root = self.root()

        while not self.is_leaf(root):
            if root.key() > p.key() and root.key() > q.key():
                root = root.left()
            elif root.key() < p.key() and root.key() < q.key:
                root = root.right()
            else:
                return root


