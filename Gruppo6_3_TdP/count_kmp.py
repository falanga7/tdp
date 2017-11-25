from TdP_collections.text.find_kmp import *


def count_kmp(t, p):
    m = len(p)
    j = find_kmp(t, p)
    count = 0
    while j != -1:
        count += 1
        t = t[j+m:]
        j = find_kmp(t[j:], p)
    return count

