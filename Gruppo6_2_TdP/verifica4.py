from pkg_i.my_rb_tree_map import MyRBTreeMap
from drawtree import draw_level_order
from util import randList
from TdP_collections.map.red_black_tree import RedBlackTreeMap

print("Albero RB casuale:")
rb_tree = MyRBTreeMap()
rb_treet = RedBlackTreeMap()

rl = randList(1, 100, 30)
i = 0
for element in rl:
    rb_tree[element] = "test"
    rb_treet[element] = "test"
    i += 1
    if i == 20:
        elem20 = element
    if i == 15:
        elem15 = element
    if i == 25:
        elem25 = element
draw_level_order(str(rb_tree))
print("Albero RB casuale non My:")
print(str(rb_treet))
print("Albero RB T:")
rb_tree1 = MyRBTreeMap()
rb_tree1[1] = "test"
draw_level_order(str(rb_tree1))
rb_tree2 = MyRBTreeMap()
rb_tree2[2] = "test"
print("Albero RB T1:")
draw_level_order(str(rb_tree2))
rb_tree1.fusion(rb_tree2)
print("Albero RB T.fusion(T1):")
draw_level_order(str(rb_tree1))
# Test se T > T1
# print("Albero RB T:")
# rb_tree3 = MyRBTreeMap()
# rb_tree3[2] = "test"
# draw_level_order(str(rb_tree3))
# rb_tree4 = MyRBTreeMap()
# rb_tree4[1] = "test"
# print("Albero RB T1:")
# draw_level_order(str(rb_tree4))
# rb_tree3.fusion(rb_tree4)
# print("Albero RB T.fusion(T1):")
# draw_level_order(str(rb_tree3))
print("Albero RB T:")
rb_tree5 = MyRBTreeMap()
rb_tree5[0] = 244
rb_tree5[1] = 448
rb_tree5[2] = 11
rb_tree5[3] = 999
draw_level_order(str(rb_tree5))
print("Albero RB T1:")
rb_tree6 = MyRBTreeMap()
rb_tree6[6] = 244
rb_tree6[7] = 448
rb_tree6[8] = 11
rb_tree6[9] = 999
draw_level_order(str(rb_tree6))
rb_tree5.fusion(rb_tree6)
print("Albero RB T.fusion(T1):")
draw_level_order(str(rb_tree5))
print("Albero RB T:")
rb_tree7 = MyRBTreeMap()
rb_tree7[0] = 244
rb_tree7[1] = 448
rb_tree7[2] = 11
rb_tree7[3] = 999
rb_tree7[4] = 999
rb_tree7[5] = 444
rb_tree7[6] = 888
rb_tree7[9] = 343
rb_tree7[10] = 999
rb_tree7[11] = 444
rb_tree7[12] = 888
rb_tree7[13] = 343
draw_level_order(str(rb_tree7))
print("Albero RB T1:")
rb_tree8 = MyRBTreeMap()
rb_tree8[15] = 244
rb_tree8[16] = 448
rb_tree8[17] = 11
rb_tree8[18] = 999
draw_level_order(str(rb_tree8))
rb_tree7.fusion(rb_tree8)
print("Albero RB T.fusion(T1):")
draw_level_order(str(rb_tree7))
print("Albero RB T:")
rb_tree9 = MyRBTreeMap()
rb_tree9[0] = 244
rb_tree9[1] = 448
rb_tree9[2] = 11
rb_tree9[3] = 999
draw_level_order(str(rb_tree9))
print("Albero RB T1:")
rb_tree10 = MyRBTreeMap()
rb_tree10[4] = 244
rb_tree10[5] = 448
rb_tree10[6] = 11
rb_tree10[7] = 999
rb_tree10[8] = 999
rb_tree10[9] = 444
rb_tree10[10] = 888
rb_tree10[11] = 343
rb_tree10[12] = 999
rb_tree10[13] = 444
rb_tree10[14] = 888
rb_tree10[15] = 343
draw_level_order(str(rb_tree10))
rb_tree9.fusion(rb_tree10)
print("Albero RB T.fusion(T1):")
draw_level_order(str(rb_tree9))
print("Albero RB T.split(9):")
rb_tree91, rb_tree92 = rb_tree9.split(9)
print("T1:")
draw_level_order(str(rb_tree91))
print("T2:")
draw_level_order(str(rb_tree92))
print("Albero RB T2.split(13):")
rb_tree921, rb_tree922 = rb_tree92.split(13)
print("T21:")
draw_level_order(str(rb_tree921))
print("T22:")
draw_level_order(str(rb_tree922))
print("T1:")
draw_level_order(str(rb_tree91))
print("Albero RB T1.split(4):")
rb_tree911, rb_tree912 = rb_tree91.split(4)
print("T21:")
draw_level_order(str(rb_tree911))
print("T22:")
draw_level_order(str(rb_tree912))