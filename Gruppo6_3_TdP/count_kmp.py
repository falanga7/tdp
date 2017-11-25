from TdP_collections.text.find_kmp import *


def count_kmp(t, p):
    if not isinstance(t, str):
        raise TypeError("Non è stata specificata una stringa in cui ricercare il pattern ma un altro tipo.")
    if not isinstance(p, str):
        raise TypeError("Il pattern deve essere una stringa.")

    m = len(p)
    if m == 0:
        return 0
    j = find_kmp(t, p)
    count = 0
    while j != -1:
        count += 1
        t = t[j + m:]
        j = find_kmp(t[j:], p)
    return count
