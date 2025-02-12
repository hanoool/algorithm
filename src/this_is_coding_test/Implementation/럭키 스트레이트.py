if __name__ == "__main__":
    input = list(map(int, input()))
    mid = len(input)//2
    right = input[mid:]
    left = input[:mid]
    
    if sum(right) == sum(left):
        print("LUCKY")
    else:
        print("READY")