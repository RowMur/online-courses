def last_digit_of_sum(num):
    if num < 2:
        return num
    
    modulo = 10
    fib_numbers = [0, 1]
    i = 2

    while True:
        prev = fib_numbers[i - 1]
        prev_prev = fib_numbers[i - 2]

        if (prev + prev_prev == modulo) and (prev == 1):
            break

        fib_numbers.append((prev + prev_prev) % modulo)
        i += 1
    
    return (fib_numbers[(num + 2) % len(fib_numbers)] - 1) % 10


if __name__ == "__main__":
    num = int(input())
    print(last_digit_of_sum(num))