from .my_list import MyList


def merge(my_list1, my_list2, my_list, key=None):
    while len(my_list1) != 0 and len(my_list2) != 0:

        if key is not None:
            elem_1 = key(my_list1[0])
            elem_2 = key(my_list2[0])
        else:
            elem_1 = my_list1[0]
            elem_2 = my_list2[0]

        if elem_1 < elem_2:
            my_list.append(my_list1.pop(0))
        else:
            my_list.append(my_list2.pop(0))

    while len(my_list1) != 0:
        my_list.append(my_list1.pop(0))
    while len(my_list2) != 0:
        my_list.append(my_list2.pop(0))


def merge_sort(my_list, key=None):
    n = len(my_list)

    if n < 2:
        return

    my_list1 = MyList()
    my_list2 = MyList()

    while len(my_list1) < n // 2:
        my_list1.append(my_list.pop(0))
    while len(my_list) != 0:
        my_list2.append(my_list.pop(0))

    merge_sort(my_list1, key)
    merge_sort(my_list2, key)

    merge(my_list1, my_list2, my_list, key)


def insertion_sort(my_list, key=None):

        ordered = MyList()
        ordered.append(my_list[0])
        i = 1
        while i < len(my_list):
            k = len(ordered) - 1
            while True:
                if key is not None:
                    u_list = key(my_list[i])
                    o_list = key(ordered[k])
                else:
                    u_list = my_list[i]
                    o_list = ordered[k]
                if u_list > o_list:
                    ordered.insert(k + 1, my_list[i])
                    break
                elif u_list == o_list:
                    ordered.insert(k + 1, my_list[i])
                    break
                elif u_list < o_list:
                    k = k - 1
                    if k < 0:
                        ordered.insert(0, my_list[i])
                        break
            i += 1
        return ordered


def compute_minrun(n):
    run = 0
    while n >= 64:
        run |= (n & 1)
        n >>= 1
    return n+run