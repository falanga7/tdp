from pkg_i.my_rb_tree_map import MyRBTreeMap
from drawtree import draw_level_order
from util import randList

rb_tree = MyRBTreeMap()
rl = randList(1, 100, 30)
i = 0
for element in rl:
    rb_tree[element] = "test"
    i += 1
    if i == 20:
        elem20 = element
    if i == 15:
        elem15 = element
    if i == 25:
        elem25 = element
draw_level_order(str(rb_tree))
