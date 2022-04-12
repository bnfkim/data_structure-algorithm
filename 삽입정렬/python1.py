def find_ins_idx(list, value):
	for i in range(len(r)):
		# 정렬된 리스트에서 자신보다 작은 값들을 모두 지나고 큰 값에서 멈춤
		if value < list[i]:
			return i
	return len(list)

def insertion_sort(list):
	result = []
	while list:
		value = list.pop(0)
		ins_idx = find_ins_idx(result, value)
		result.insert(ins_idx, value)
	return result

list = [2, 4, 5, 1, 3]
print(insertion_sort(list))