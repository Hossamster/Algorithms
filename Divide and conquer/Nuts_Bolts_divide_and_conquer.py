# from random import sample,choice
# def random_list():
#     """generates a random list"""
#     lst = [choice(['%','$','#',"@","&"]) for i in range(0,5)]
#     return (sample(lst, len(lst)))
# print(random_list())


# Nuts and Bolts in a quick sort way
def quicksort(lst):
    """Sorting the list by quicksort technique """

    if len(lst) <= 1:
        return lst
    else:
        # pop the last element
        pivot = lst.pop()               
        lst_left = []
        lst_right = []  
        for i in lst:                   
            if i > pivot:               
                lst_right.append(i)
            elif i <= pivot:            
                lst_left.append(i)
        return quicksort(lst_left) + [pivot] + quicksort(lst_right)  

def nuts_bolts(nuts_lst, bolts_lst):
    """Mapping each nut to its bolt"""
    nuts = quicksort(nuts_lst)          # sorting the nuts by quicksort technique
    bolts = quicksort(bolts_lst)        # sorting the bolts by quicksort technique
    # mapping each nut to its bolt
    for i in nuts:          
        for j in bolts:     
            if i == j:      
                print(f"{i} nut is mapping to {j} bolt")

nuts_bolts([1,2,3,4,5], [3,2,4,1,5])

# nuts_bolts(random_list(), random_list())

"""In case you don't know what the function does !"""
"""Just type this >> print(function_name.__doc__)"""
"""for ex. print(quicksort.__doc__)"""
