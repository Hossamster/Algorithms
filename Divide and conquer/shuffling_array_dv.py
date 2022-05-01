def shuffle(lst):
    #print(lst)
    k = int(len(lst))
    # print(k)
    if k <= 1: 			# if the length of the list is less than or equal to one
        return lst		# return the list
    else:
        left_lst = []	 #[1]
        right_lst = []   #[2]
        for i in range(0,len(lst)): # (0,9)
            if i % 2 == 0:
                left_lst.append(lst[i]) # append lst[i] in left_lst if the index is even 
            else:
                right_lst.append(lst[i])# append lst[i] in right_lst if the index is odd
        
        return shuffle(right_lst) + shuffle(left_lst)

print(shuffle([1,3,7,4,8]))

# print(shuffle([2,5,1,3,4,7,6]))