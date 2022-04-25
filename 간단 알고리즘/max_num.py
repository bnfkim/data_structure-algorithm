def find_max(list):
    n = len(list)
    max_num = list[0]
    
    for i in range(1,n):
        if list[i] > max_num :
            max_num = list[i]
    
    return max_num

list = [17, 19, 33, 58, 7, 42]
print(find_max(list))
