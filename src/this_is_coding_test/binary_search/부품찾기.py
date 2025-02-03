# def solve():
#     # 여기에 풀이 작성
#     pass

if __name__ == "__main__":
    # 입력 받기
    n = int(input())
    supply = list(map(int, input().split()))
    
    m = int(input())
    requirements = list(map(int, input().split()))
    
    for r in requirements:
        if r in supply:
            print("yes", end=" ")
        else:
            print("no", end=" ")