def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            #앞 원소 값이 크면 
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

list = [2, 4, 5, 1, 3]
bubble_sort(list)
print(list)