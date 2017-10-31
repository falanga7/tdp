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

