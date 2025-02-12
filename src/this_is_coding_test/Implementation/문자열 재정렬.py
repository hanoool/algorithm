if __name__ == "__main__":
    input = input()
    alphabet = []
    num = 0
    for i in input:
        try:
            num += int(i)
        except Exception:
            alphabet.append(i)
    sorted_str = "".join(sorted(alphabet))
    
    print(sorted_str + str(num))