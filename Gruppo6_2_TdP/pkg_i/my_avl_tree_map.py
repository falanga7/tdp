from .my_tree_map import MyTreeMap
from ..TdP_collections.map.avl_tree import AVLTreeMap


class MyAVLTreeMap(MyTreeMap, AVLTreeMap):
    # -------------------------- nested _Node class --------------------------
    class _Node(MyTreeMap._Node):
        """Node class for AVL maintains height value for balancing.

        We use convention that a "None" child has height 0, thus a leaf has height 1.
        """
        __slots__ = '_height'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None, successor=None, predecessor=None):
            super().__init__(element, parent, left, right, successor, predecessor)
            self._height = 0  # will be recomputed during balancing


