if __name__ == "__main__":
    s = input()
    group = 0
    count = [0,0]

    if s[0] == '0':
        count[0] += 1
    else:
        count[1] += 1    
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            continue
        else:
           if s[i + 1] == '0':
               count[0] += 1
           else:
               count[1] += 1
               
    print(min(count))
    
    