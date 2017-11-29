from TdP_collections.text.find_kmp import compute_kmp_fail


def find_kmp(T, P, fail):
  """Return the lowest index of T at which substring P begins (or else -1)."""
  n, m = len(T), len(P)            # introduce convenient notations
  if m == 0: return 0              # trivial search for empty string
  j = 0                            # index into text
  k = 0                            # index into pattern
  while j < n:
    if T[j] == P[k]:               # P[0:1+k] matched thus far
      if k == m - 1:               # match is complete
        return j - m + 1
      j += 1                       # try to extend match
      k += 1
    elif k > 0:
      k = fail[k-1]                # reuse suffix of P[0:k]
    else:
      j += 1
  return -1                        # reached end without match


def count_kmp(t, p):
    if not isinstance(t, str):
        raise TypeError("Non è stata specificata una stringa in cui ricercare il pattern ma un altro tipo.")
    if not isinstance(p, str):
        raise TypeError("Il pattern deve essere una stringa.")
    fail = compute_kmp_fail(p)  # rely on utility to precompute
    m, n = len(p), len(t)
    if m == 0 and n == 0:
        return 1
    elif n == 0 and m != 0:
        return 0
    elif n != 0 and m == 0:
        return n+1
    j = find_kmp(t, p, fail)
    count = 0
    while j != -1:
        count += 1
        t = t[j + m:]
        j = find_kmp(t[j:], p, fail)
    return count
