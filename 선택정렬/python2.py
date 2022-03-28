def sel_sort(a):
    n = len(a)
    for i in range (n-1):
        # 최솟값 찾음
        #리스트 맨 앞 원소가 하나씩 줄어들음
        #리스트 맨 뒤 원소 고정 및 기준
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        # 최솟값과 맨 앞 원소의 위치 변경 (swap)
        print(i+1 , "번째")
        print("min_idx : " , min_idx, ", value : ", a[min_idx])
        a[i], a[min_idx] = a[min_idx], a[i]
        print("swap 후 list : " , a)
        print()

list = [2,4,5,1,3]
sel_sort(list)
print(list)
