from math import inf
n = int(input("Enter a number: "))
lst = [inf for i in range(1, n+1) ]
lst.insert(0, 0)
print(lst)
for i in range(1,n+1):
    for j in range(1,n+1):
        if j * j > i:
            break
        lst[i] = min(lst[i],1+lst[i-(j*j)])

print(lst[n])