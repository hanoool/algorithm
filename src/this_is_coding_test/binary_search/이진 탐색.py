# 반복문
def binary_search(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
		if array[mid] == target:
			return mid
        # 중간점 보다 타겟이 작은 경우 탐색 범위를 왼쪽으로 이동(end 변경)
		elif array[mid] > target:
			end = mid - 1
        # 중간점 보다 타겟이 큰 경우 탐색 범위를 오른쪽으로 이동(start 변경)
		else:
			start = mid + 1
	return None

# 재귀
def binary_search(array, target, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	if array[mid] == target:
		return mid
    # 중간점 보다 타겟이 작은 경우 탐색 범위를 왼쪽으로 이동(end 변경)
	elif array[mid] > target:
		return binary_search(array, target, start, mid - 1)
    # 중간점 보다 타겟이 큰 경우 탐색 범위를 오른쪽으로 이동(start 변경)
	else:
		return binary_search(array, target, mid + 1, end)