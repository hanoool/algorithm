if __name__ == "__main__":
    n = int(input())
    
    hs = [str(i) for i in range(n+1)]
    ms = [str(i) for i in range(60)]
    ss = [str(i) for i in range(60)]

    count = 0
    time = ''
    for h in hs:
        for m in ms:
            for s in ss:
                if '3' in h + m + s:
                   count += 1
                
                
    print(count)