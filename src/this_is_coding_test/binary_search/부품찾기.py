def binary_search(array, target, start, end):
    if start > end:
        print("no", end= " ")
        return None
    mid = (start + end) // 2
    
    if target == array[mid]:
        print("yes", end=" ")
        return None
    elif target > array[mid]:
        binary_search(array, target, mid + 1, end)
    else:
        binary_search(array, target, start, mid - 1)
    

if __name__ == "__main__":
    # 입력 받기
    n = int(input())
    supply = list(map(int, input().split()))
    
    m = int(input())
    requirements = list(map(int, input().split()))
    
    for requirement in requirements:
        binary_search(sorted(supply), requirement, 0, n - 1)