#catalan numbers 1 1 2 5 14 42 132
# C(n) = summation from i =0 to n-1 for (C(i)*C(n-i-1))

n = int(input("Enter a number: "))

catalan =[1 for i in range(2)] # list comprehension
print(catalan) #>> [1,1] for index 0 and 1
k= 0

for i in range(2,n+1): # loop from index 2 to n
    for j in range(i-1,-1,-1): # reverse the loop >> from index i-1 to 0
        k += (catalan[j] * catalan[i-j-1]) # The formula
        #print(k)
    catalan.append(k) # append the catalan list with k 
    k = 0
print(catalan)
print(f"The catalan {n}th term is {catalan[n]}")
