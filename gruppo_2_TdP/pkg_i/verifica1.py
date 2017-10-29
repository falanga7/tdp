from gruppo_2_TdP.TdP_collections.map.red_black_tree import RedBlackTreeMap
from gruppo_2_TdP.TdP_collections.map.avl_tree import AVLTreeMap

avltree = AVLTreeMap()
node = AVLTreeMap._Node()
node._element(3)
avltree._rebalance_insert(node)
print(avltree)

