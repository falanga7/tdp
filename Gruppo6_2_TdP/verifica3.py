from pkg_i.my_tree_map import MyTreeMap
from drawtree import draw_level_order

btree = MyTreeMap()
btree[6] = 244
btree[2] = 448
btree[1] = 11
btree[4] = 999
btree[5] = 448
btree[9] = 11
btree[8] = 999
print("Stampa del di un albero con diversi LCA:")
draw_level_order(str(btree))
print("LCA(6,9)", btree.LCA(btree.find_position(6), btree.find_position(9)).key())
print("LCA(1,4)", btree.LCA(btree.find_position(1), btree.find_position(4)).key())
print("LCA(5,8)", btree.LCA(btree.find_position(5), btree.find_position(8)).key())
print("LCA(5,2)", btree.LCA(btree.find_position(5), btree.find_position(2)).key())
print("LCA(5,6)", btree.LCA(btree.find_position(5), btree.find_position(6)).key())
