# Merge Sort using Recursion in Merge and Mergesort
import random


def merge_recursive(a, b, out, reverse=False):
    """
    Merge first element of both list recursively
    Return the merged list
    """
    # print(f"called merge on {a} and {b} and out is : {out}")
    # print(b)
    if len(a) == 0:
        out.extend(b[:])
    elif len(b) == 0:
        out.extend(a[:])
    else:
        if reverse:
            if a[0] > b[0]:
                out.append(a[0])
                merge_recursive(a[1:], b, out, reverse)
            else:
                out.append(b[0])
                merge_recursive(a, b[1:], out, reverse)
        else:
            if a[0] < b[0]:
                out.append(a[0])
                merge_recursive(a[1:], b, out, reverse)
            else:
                out.append(b[0])
                merge_recursive(a, b[1:], out, reverse)


def mergesort_recursive(arr, reverse=False):
    """
    Sort list using merge sort item
    """
    if len(arr) <= 1:
        return arr
    else:
        n = len(arr)
        out = []
        merge_recursive(mergesort_recursive(arr[:(n // 2)], reverse), mergesort_recursive(arr[(n // 2):],reverse), out, reverse)
        return out


if __name__ == '__main__':
    res = [random.randrange(1, 500, 1) for i in range(10)]
    print(res, "\n")
    print(mergesort_recursive(res, True))
