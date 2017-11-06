from pkg_i.my_tree_map import MyTreeMap
from drawtree import draw_level_order

test = MyTreeMap()
test[1] = 2
test[2] = 3
test[4] = 5
test[3] = "Anna Chiara"
if test.is_empty():
    raise ValueError("L'abero è vuoto.")
for p in test.breadthfirst():
    if p is None:
        to_print += ",#"
    elif test.is_root(p):
        to_print = '{' + str(p.key())
    else:
        to_print += "," + str(p.key())
to_print += "}"
print(to_print)
draw_level_order(to_print)
