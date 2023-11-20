def last_digit_of_fibonacci(num):
    if num < 2:
        return num
    
    fib_numbers = [0, 1]

    i = 2
    while i <= num:
        fib_numbers.append((fib_numbers[i-1] + fib_numbers[i-2]) % 10)
        i += 1

    return fib_numbers[num]

if __name__ == "__main__":
    num = int(input())
    print(last_digit_of_fibonacci(num))