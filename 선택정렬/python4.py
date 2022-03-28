def sel_sort(a):
    n = len(a)
    for i in range (n-1):
        #최댓값 찾음
        #리스트 맨 뒤 원소가 하나씩 줄어들음
        #리스트 맨 앞 원소 고정 및 기준
        max_idx = 0
        for j in range(0, n-i): 
            if a[j] > a[max_idx]:
                max_idx = j
        print(i+1 , "번째")
        print("max_idx : " , max_idx, ", value : ", a[max_idx])
        # 최댓값과 맨 뒤 원소의 위치 변경 (swap)
        a[n-i-1], a[max_idx] = a[max_idx], a[n-i-1]
        print("swap 후 list : " , a)
        print()

list = [2,4,5,1,3]
sel_sort(list)
print(list)
