# TODO: Non preemptive 
def task_scheduling(tasks):
    # generate 2d list 
    st_fn_lst = [ [[] for i in range(2)]for j in range(tasks)]

    # let the user input his start time and finish time for each task
    for i in range(tasks):
        for j in range(2):
            st_fn_lst[i][j] = int(input(" Enter the start number first and then the finsh number"))
    
    print(f"Before sorting the list {st_fn_lst}")
    # Lets sort the list by the least finish time
    st_fn_lst.sort(key=lambda x:(x[1]))
    print(f"The list after sorting {st_fn_lst}")
    
    cnt = 0     # for how much tasks can be done 
    lst = []    # to append in it which tasks 
    s = -1      
    for i in st_fn_lst:
        if s <= i[0]:
            s = i[1]
            cnt += 1
            lst.append(i)
    return f"The max number of tasks can be done is {cnt}\nThey are {lst} "

    
print(task_scheduling(5))
