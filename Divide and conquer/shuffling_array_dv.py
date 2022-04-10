# Assume [2,5,1,3,4,7] , n=lst/2 = 6/2 = 3
# [2,3,5,4,1,7]
def shuffle(lst):
    n = (len(lst) / 2)
    print(n)
    if n % 2 == 0:
        left_lst = []
        for i in range(0, n):
            left_lst.append(lst[i])

        right_lst = []
        for i in range(n, len(lst)):
            right_lst.append(lst[i])

        print(left_lst, right_lst)

        final_lst = []
        for i in range(0, len(left_lst)):
            final_lst.extend([left_lst[i], right_lst[i]])

        return final_lst

    return f"Please enter an array that divisible by 2"


print(shuffle([2, 5, 1, 3, 4, 7]))
