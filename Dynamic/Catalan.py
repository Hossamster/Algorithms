n = int(input("Enter a number: "))

# list comprehension
catalan =[1 for i in range(2)]
#print(catalan)
k= 0

for i in range(2,n+1): # 2 to 5
    for j in range(i-1,-1,-1): #
        k += (catalan[j] * catalan[i-j-1])
        #print(k)
    catalan.append(k)
    k = 0
print(catalan)
print(f"The catalan {n}th term is {catalan[n]}")