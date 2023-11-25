from functools import cmp_to_key

def maximum_salary(numbers: list):
    def compare(a, b):
        if (int(a + b) < int(b + a)):
            return -1
        elif (int(a + b) < int(b + a)):
            return 1
        else:
            return 0

    sorted_numbers = sorted(numbers, key=cmp_to_key(compare), reverse=True)
    return sorted_numbers


if __name__ == "__main__":
    n_of_numbers = int(input())
    numbers = input().split()
    
    print("".join(maximum_salary(numbers)))