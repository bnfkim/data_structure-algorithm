def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    # 리스트 원소가 존재하는 동안 loop 
    while a:
        # 최솟값의 index 찾음
        min_idx = find_min_idx(a)
        # 최솟값을 리스트에서 빼내어 변수에 저장
        value = a.pop(min_idx)
        # 최솟값을 리스트 원소로 새로 저장
        result.append(value)
    return result

list = [2, 4, 5, 1, 3]
print(sel_sort(list))