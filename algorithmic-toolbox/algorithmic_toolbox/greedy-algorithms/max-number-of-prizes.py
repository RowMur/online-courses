def max_number_of_prizes(total_prizes):
    summands = []

    current_number = 1
    while total_prizes > 2 * current_number:
        summands.append(str(current_number))
        total_prizes -= current_number
        current_number += 1

    summands.append(str(total_prizes))
    return summands

if __name__ == "__main__":
    total_prizes = int(input())
    
    summands = max_number_of_prizes(total_prizes)
    print(len(summands))
    print(" ".join(summands))
