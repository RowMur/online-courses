def fibonacci_number(num: int):

    fibonacci_numbers = [0,1]
    if num < 2:
        return num

    i = 2
    while i <= num:
        fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
        i += 1
    
    return fibonacci_numbers[num]

if __name__ == "__main__":
    num = int(input())
    print(fibonacci_number(num))