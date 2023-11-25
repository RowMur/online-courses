def max_value_of_loot(capacity, options: list):
    options.sort(key= lambda obj : obj["value"] / obj["weight"])
    options.reverse()
    
    stolen_value = 0
    remaining_capacity = capacity
    for option in options:
        if remaining_capacity == 0:
            break
        
        elif remaining_capacity >= option["weight"]:
            stolen_value += option["value"]
            remaining_capacity -= option["weight"]
        
        else:
            fraction_to_take = remaining_capacity / option["weight"]
            stolen_value += fraction_to_take * option["value"]
            remaining_capacity = 0
    
    return stolen_value


if __name__ == "__main__":
    [n_of_options, capacity] = input().split()
    
    options = []
    for option in range(int(n_of_options)):
        [value, weight] = input().split()
        options.append({
            "weight": int(weight),
            "value": int(value)
        })

    print(max_value_of_loot(int(capacity), options))    
