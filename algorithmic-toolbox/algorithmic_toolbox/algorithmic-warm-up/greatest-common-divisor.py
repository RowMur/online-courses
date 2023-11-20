def greatest_common_divisor(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    
    return b

if __name__ == "__main__":
    a, b = input().split()
    print(greatest_common_divisor(int(a), int(b)))