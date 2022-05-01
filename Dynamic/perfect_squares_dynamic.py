from math import inf
def per(n):
    lst = [inf for i in range(1, n+1) ] 
    lst.insert(0, 0) # insert 0 in index 0 in lst 
    # print(lst)
    # if n = 13 >> so it can be 9 + 4 so the output is 2
    # if n = 12 >> so it cab be 4 + 4 +4 so the output is 3
    #i 0 1 2 3 4 5 6 7 8 9 10 11 12 13
    #j 0 1 2 3 1 2 3 4 2 1 2  3  3  2    >> least number of perfects squares that sum to n 
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j * j > i:
                break
            lst[i] = min(lst[i],1+lst[i-(j*j)])
    print(lst)
    return (lst[n])

print(per(13))
