from random import shuffle
from collections import deque
from copy import deepcopy
from math import sqrt

A = []
for i in range(0, 10):
    A.append(i)
shuffle(A)


# ========[Helper Functions]========

def Swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


def InsertionSort(A):
    B = [A[0]]
    i = 1
    while i < len(A):
        k = len(B) - 1
        while True:
            if A[i] > B[k]:
                B.insert(k + 1, A[i])
                break
            elif A[i] == B[k]:
                B.insert(k + 1, A[i])
                break
            elif A[i] < B[k]:
                k = k - 1
                if k < 0:
                    B.insert(0, A[i])
                    break
        i += 1
    return B

print(A)
C=InsertionSort(A)
print(C)
