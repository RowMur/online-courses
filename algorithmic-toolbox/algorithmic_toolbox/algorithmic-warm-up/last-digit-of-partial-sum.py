def last_digit_of_partial_sum(first_index, end_index):
    
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
    
    total_sum = (fib_numbers[(end_index + 2) % len(fib_numbers)] - 1) % 10
    start_sum = (fib_numbers[(first_index + 1) % len(fib_numbers)] - 1) % 10
    return (total_sum - start_sum) % 10


if __name__ == "__main__":
    start, end = input().split()
    print(last_digit_of_partial_sum(int(start), int(end)))