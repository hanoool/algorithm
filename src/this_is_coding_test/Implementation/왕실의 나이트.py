if __name__ == "__main__":
    input_data = input()
    w = input_data[0]
    h = int(input_data[1])
    change = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8}
    count = 0
    
    if change[w]+2 <= 8 and h + 1 <= 8:
        count += 1
    if change[w]+2 <= 8 and h - 1 >= 1:
        count += 1
    if change[w]-2 >= 1 and h + 1 <= 8:
        count += 1
    if change[w]-2 >= 1 and h - 1 <= 1:
        count += 1
    if change[w]+1 <= 8 and h + 2 <= 8:
        count += 1
    if change[w]+1 <= 8 and h - 2 >= 1:
        count += 1
    if change[w]-1 >= 1 and h + 2 <= 8:
        count += 1
    if change[w]-1 >= 1 and h - 2 <= 1:
        count += 1
    
    print(count)
    
        
    