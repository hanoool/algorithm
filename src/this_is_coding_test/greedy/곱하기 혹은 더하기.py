if __name__ == "__main__":
    arr = list(map(int, input()))
    arr = list(filter(lambda x: x != 0, arr))
    result = 1
    
    for i in arr:
        result = result * i
    print(result)
    
    
        