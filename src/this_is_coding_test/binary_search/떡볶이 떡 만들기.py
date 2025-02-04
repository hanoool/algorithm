def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        arr_sum = sum([(x-mid) if x-mid > 0 else 0 for x in arr])
        if arr_sum == target:
            print(mid)
            break
        elif arr_sum > target:
            start = mid + 1
        else:
            end = mid - 1

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 적어도 m 만큼의 떡을 얻기 위해 설정할 수 있는 절단기 높이의 최대값
    binary_search(arr, m, 0, max(arr))
    
    