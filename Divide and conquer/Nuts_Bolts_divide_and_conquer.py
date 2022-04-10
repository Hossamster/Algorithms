# Nuts and Bolts in a quick sort way

from random import sample


def random_list():
    """generates a random list"""
    lst = [num for num in range(9, 101, 10)]
    return (sample(lst, len(lst)))


print(random_list())


def quicksort(lst):
    """Sorting list from smallest to largest"""

    if len(lst) <= 1:
        return lst
    else:
        # pop the last element
        pivot = lst.pop()               # o(1)
        lst_left = []
        lst_right = []  # o(2)
        for i in lst:                   # o(lst)
            if i > pivot:               # o(lst)
                lst_right.append(i)
            elif i <= pivot:            # o(lst)
                lst_left.append(i)
        return quicksort(lst_left) + [pivot] + quicksort(lst_right)  # o(1) !

    # big O for quicksort() is O(3+3*lst) app. = O(lst)


def nuts_bolts(nuts_lst, bolts_lst):
    nuts = quicksort(nuts_lst)
    bolts = quicksort(bolts_lst)
    for i in nuts:          # o(n)
        for j in bolts:     # o(n)
            if i == j:      # o(1)
                print(f"{i} nut is mapping to {j} bolt")

    # big O for nuts_bolts() is O(n^2+1) app. = O(n^2)


nuts_bolts(random_list(), random_list())

"""In case you don't know what the function does !"""
"""Just type this >> print(function_name.__doc__)"""
"""for ex. print(quicksort.__doc__)"""
