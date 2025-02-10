if __name__ == "__main__":
    input_data = input()
    column = int(ord(input_data[0]) - ord('a')) + 1
    row = int(input_data[1])
    steps = [(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)]
    count = 0
    
    for step in steps:
        next_column = column + step[0]
        next_row = column + step[1]
        if next_column <= 8 and next_row >= 1 and next_row <= 8 and next_column >= 1:
            count += 1
    
    print(count)
    
        
    