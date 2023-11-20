def huge_fibonacci(num, modulo):
    if num < 2:
        return num
    
    fib_numbers = [0, 1]
    i = 2

    while True:
        prev = fib_numbers[i - 1]
        prev_prev = fib_numbers[i - 2]

        if (prev + prev_prev == modulo) and (prev == 1):
            break

        fib_numbers.append((prev + prev_prev) % modulo)
        i += 1

    return fib_numbers[num % len(fib_numbers)]

if __name__ == "__main__":
    num, modulo = input().split()
    print(huge_fibonacci(int(num), int(modulo)))