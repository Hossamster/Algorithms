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

# Median of two sorted arrays by divide and conquer algorithm
from math import floor

def quicksort(lst):
    """Make quicksort for the lst"""
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop()  # The last element in the array
        left_lst = []  	  # Less than the pivot
        right_lst = []	  # Bigger than the pivot
        for i in lst:
            if i < pivot:  # if the item is less than the pivot, put it in the left lst
                left_lst.append(i)
            else:		  # if the item is greater than the pivot, put it in the right lst
                right_lst.append(i)
        return quicksort(left_lst) + [pivot] + quicksort(right_lst)


# print(quicksort(random_list()))

def median_of_two_sorts(lst1, lst2):
    """getting the median after sorted them in one list"""
    merged_lsts = lst1 + lst2 # merge the two lists in one list called merged_lsts
    lsts = quicksort(merged_lsts) # sort the merged_lsts by the quicksort method
    # after making sorting for the lists, get the length of the sorted lst
    print(lsts)
    n = len(lsts)  # the length of the sorted lst
    # print(n)
    if n % 2 == 0:  # if the length of the sorted lst is even
        k = int(n/2)
        result = (lsts[k] + lsts[k-1]) / 2  # the result of the median
        print(result)
    else:		 # if the length of the sorted lst is odd
        k = int(floor(n/2))
        result = (lsts[k])
        print(result)


median_of_two_sorts([60, 51, 15, 6, 42, 33, 69, 24, 55,76], [22, 27, 37, 47, 62, 12, 7, 52, 17, 32])

"""
[15, 75, 25, 35, 55, 65, 45, 5]     n= 8 >> k[3] , k[4]
[15, 75, 25, 35, 55, 65]            n =6 >> k[2] , k[3]
"""