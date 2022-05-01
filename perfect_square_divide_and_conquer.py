from random import sample
def random_list():
    lst = [num for num in range(10,101,10)]
    lst = sample(lst,len(lst))
    print(lst)
random_list()
from math import sqrt

def perfect_square(n=1): # default parameter to avoid errors 
    check = False
    for i in range(1,n): # from 1 to n-1
        if sqrt(n) == i:
            check = True
    return check

print(perfect_square(4))



