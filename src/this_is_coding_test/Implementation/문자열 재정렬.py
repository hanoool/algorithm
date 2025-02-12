if __name__ == "__main__":
    input = input()
    alphabet = []
    num = 0
    for i in input:
        if i.isalpha():
            alphabet.append(i)
        else:
            num += int(i)
    alphabet.sort()        
    ''.join(alphabet)
    
    if num != 0:
        alphabet.append(str(num))
    
    print(''.join(alphabet))