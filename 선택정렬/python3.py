def sel_sort(a):
    n = len(a)
    for i in range (n-1):
        max_idx = i
        # 최댓값 찾음
        for j in range(i+1, n):
            if a[j] > a[max_idx]:
                max_idx = j

        # 최댓값과 맨 앞 원소의 위치 변경 (swap)
        a[i], a[max_idx] = a[max_idx], a[i]

list = [2,4,5,1,3]
sel_sort(list)
print(list)
