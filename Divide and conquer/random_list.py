from random import sample,randint
def random_list():
    k = randint(1,10)
    l = randint(11,100)
    m = randint(5,7)
    print(k,l,m)
    lst = [num for num in range(k,l,m)]
    return (sample(lst,len(lst)))

print(random_list())