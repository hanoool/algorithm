if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        data = input().split()
        name = data[0]
        score = int(data[1])
        arr.append((name, score))
        
    sorted = sorted(arr, key=lambda student: student[1])
    
    for name, score in sorted:
        print(name, end=" ")
        