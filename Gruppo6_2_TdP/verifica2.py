from pkg_i.my_tree_map import MyTreeMap
test = MyTreeMap()
test[1] = 2
test[2] = 3
test[4] = 5
for p in test.breadthfirst():
    if test.is_root(p):
        to_print = '{' + str(p.key())
    to_print += "," + str(p.key())
to_print += "}"
draw_level_order(to_print)
