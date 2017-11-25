from TdP_collections.text.find_kmp import *


def count_kmp(t, p):
    if not isinstance(t, str):
        raise TypeError("Non è stata specificata una stringa in cui ricercare il pattern ma un altro tipo.")
    if not isinstance(p, str):
        raise TypeError("Il pattern deve essere una stringa.")

    m, n = len(p), len(t)
    if m == 0 and n == 0:
        return 1
    elif n == 0 and m != 0:
        return 0
    elif n != 0 and m == 0:
        return n+1
    j = find_kmp(t, p)
    count = 0
    while j != -1:
        count += 1
        t = t[j + m:]
        j = find_kmp(t[j:], p)
    return count
