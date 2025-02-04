def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        arr_sum = sum([max(x-mid, 0)for x in arr])
        if arr_sum < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 적어도 m 만큼의 떡을 얻기 위해 설정할 수 있는 절단기 높이의 최대값
    print(binary_search(arr, m, 0, max(arr)))
    
    