if __name__ == "__main__":
    arr = list(map(int, input()))
    result = arr[0]
    
    for i in arr:
        if i <= 1 or result <= 1:
            result += i
        else:
            result *= i
    
    print(result)
    
    
        