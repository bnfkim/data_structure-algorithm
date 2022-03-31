def partition(list, start, end):
    pivot = list[end]
    i = start
    for j in range(start, end):
        if list[j] <= pivot:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[end] = list[end], list[i]
    return i

def quick_sort_sub(list, start, end):
    if start < end:
        pos = partition(list, start, end)
        quick_sort_sub(list, start, pos-1)
        quick_sort_sub(list, pos+1, end)

def quick_sort(list):
    quick_sort_sub(list, 0, len(list)-1)

list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(list)
print(list)