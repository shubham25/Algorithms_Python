# Merge Sort using Iteration and Queue
import random


def merge(a, b):
    """
    Merge 2 input list and returns merged output list
    """
    n1 = len(a)
    n2 = len(b)
    out = []
    i, j = 0, 0
    while (i < n1) and (j < n2):
        if a[0] < b[0]:
            out.append(a.pop(0))
            i += 1
        else:
            out.append(b.pop(0))
            j += 1
    if i == n1:
        out.extend(b)
    elif j == n2:
        out.extend(a)
    return out


def mergesort_iterative(arr):
    """
    Converts list to queue and pop 2 items
    and merge them until single item remains
    :param arr: list to be sorted
    :return: returns sorted list. Not in place sort
    """
    arr = [[x] for x in arr]
    while True:
        # print(arr)
        # input()
        if len(arr) == 1:
            return arr[0]
        else:
            arr.append(merge(arr.pop(0), arr.pop(0)))


if __name__ == '__main__':
    res = [random.randrange(1, 100, 1) for i in range(10)]
    print(res, "\n")
    print(mergesort_iterative(res))
