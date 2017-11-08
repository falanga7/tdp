from pkg_i.my_rb_tree_map import MyRBTreeMap
from drawtree import draw_level_order

rb_tree = MyRBTreeMap()
rb_tree[0] = 1
rb_tree[1] = 4
rb_tree[3] = 54
rb_tree[6] = 22
rb_tree[88] = 22
draw_level_order(str(rb_tree))