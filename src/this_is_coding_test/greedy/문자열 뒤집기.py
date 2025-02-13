if __name__ == "__main__":
    s = input()
    group = 0
    count = [0,0]
    
    for i in range(len(s) - 1):
       if s[i] == s[i + 1]:
           if i + 1 == len(s):
            if s[i] == '0':
               count[0] += 1
            else:
               count[1] += 1     
           else:
            continue
       else:
           if s[i] == '0':
               count[0] += 1
           else:
               count[1] += 1
               
    print(min(count))
    
    