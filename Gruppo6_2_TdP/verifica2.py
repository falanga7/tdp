from pkg_i.my_tree_map import MyTreeMap
from drawtree import draw_level_order
from util import randList


def printsp(tree):
    for p in tree.breadthfirst():
        if p is None:
            continue
        else:
            key = p.key()
            after = "#" if tree.after(p) is None else tree.after(p).key()
            before = "#" if tree.before(p) is None else tree.before(p).key()

        print("Il successore di", key, "è:", after)
        print("Il predecessore di", key, "è:", before)


btree1 = MyTreeMap()
btree1[0] = 233
print("Stampa del primo albero di test con successori e predecessori:")
draw_level_order(str(btree1))
printsp(btree1)

btree2 = MyTreeMap()
btree2[0] = 244
btree2[1] = 448
btree2[2] = 11
btree2[3] = 999
print("Stampa del secondo albero di test con successori e predecessori:")
draw_level_order(str(btree2))
printsp(btree2)

btree3 = MyTreeMap()
btree3[3] = 244
btree3[2] = 448
btree3[1] = 11
btree3[0] = 999
print("Stampa del terzo albero di test con successori e predecessori:")
draw_level_order(str(btree3))
printsp(btree3)

btree4 = MyTreeMap()
rl = randList(1, 100, 30)
i = 0
for element in rl:
    btree4[element] = "test"
    i += 1
    if i == 20:
        elem20 = element
    if i == 15:
        elem15 = element
    if i == 25:
        elem25 = element

print("Stampa del quarto albero di test con successori e predecessori:")
draw_level_order(str(btree4))
printsp(btree4)

print("Stampa del quarto albero di test con successori e predecessori e alcuni elementi eliminati:")

del btree4[elem20]
del btree4[elem15]
del btree4[elem25]
draw_level_order(str(btree4))
printsp(btree4)

print("Stampa del quarto albero di test con successori e predecessori e attach ad un elemento casuale:")

p = btree2.right(btree2.root())
p = btree2.right(btree2.right(p))
btree2._attach(p, btree3, btree4)
draw_level_order(str(btree2))
printsp(btree2)
