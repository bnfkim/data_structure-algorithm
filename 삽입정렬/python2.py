def inseration_sort(list):
    n = len(list)
    for i in range (1,n):
        key = list[i]
        j = i-1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

list = [2,5,3,7,4]
inseration_sort(list)
print(list)