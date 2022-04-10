from random import sample,randint
from math import floor

# def random_list():
#     lst = [num for num in range(9,101,10)]
#     return (sample(lst,len(lst)))

# def random_list():
#     k = randint(1,10)
#     l = randint(11,100)
#     m = randint(5,7)
#     # print(k,l,m)
#     lst = [num for num in range(k,l,m)]
#     return (sample(lst,len(lst)))


def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop() # The last element in the array
        left_lst = []
        right_lst = []
        for i in lst:
            if i < pivot:
                left_lst.append(i)
            else:
                right_lst.append(i)
        return quicksort(left_lst) + [pivot] + quicksort(right_lst)


# print(quicksort(random_list()))

def median_of_two_sorts(lst1,lst2):
    lsts = quicksort(quicksort(lst1) + quicksort(lst2))
    # lsts = quicksort(lsts)
    print(lsts)
    n = len(lsts)
    if n % 2 == 0:
        k = int(n/2)
        result = lsts[k] + lsts[k-1]
        print(result)
    else:
        k = int(n/2)
        result = floor(lsts[k])
        print(result)
        
median_of_two_sorts([60, 51, 15, 6, 42, 33, 69, 24,55],[22, 27, 37, 47, 62, 12, 7, 52, 17, 32, 42, 67, 57])

"""
[15, 75, 25, 35, 55, 65, 45, 5]     n= 8 >> k[3] , k[4]
[15, 75, 25, 35, 55, 65]            n =6 >> k[2] , k[3]
"""
