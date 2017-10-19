from Progetto1.my_list import *

def stampaSuffissiIterativa(lista):
    j = 1

    to_return = MyList()
    my_list = MyList()
    my_list.append(MyList())

    i = 0
    current = lista._tail._left if (not lista._reverse) else lista._tail._right
    while j <= lista._size:
        while i != j:
            to_return.insert(0, current._element)
            if not lista._reverse:
                current = current._left
            else:
                current = current._right
            i += 1
        j += 1
        my_list.append(to_return.copy())
    return my_list


def stampaSuffissiRicorsiva(lista):
    output = MyList()

    if (lista._size == 0):
        output.append(MyList())
        return output

    else:
        output.append(lista[0:lista._size])
        return stampaSuffissiRicorsiva(lista[0 + output._size:lista._size]) + output
