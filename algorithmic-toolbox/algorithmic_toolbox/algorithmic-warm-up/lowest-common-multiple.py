def lowest_common_multiple(a, b):
    init_a = a
    init_b = b
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    
    gcd = b

    return int((init_a * init_b) / gcd)

if __name__ == "__main__":
    a, b = input().split()
    print(lowest_common_multiple(int(a), int(b)))