def solve_safe_dial(rotations_input): 

    lines = rotations_input.strip().split('\n')

    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        
        if position == 0:
            zero_count += 1

    return zero_count

def solve_safe_dial_part2(rotations_input): 
    lines = rotations_input.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'R':
            first_zero = (100 - position) % 100
            if first_zero == 0:
                first_zero = 100
            
            if distance >= first_zero:
                zero_count += 1 + (distance - first_zero) // 100
            
            position = (position + distance) % 100
            
        else:
            first_zero = position
            if first_zero == 0:
                first_zero = 100
            
            if distance >= first_zero:
                zero_count += 1 + (distance - first_zero) // 100
            
            position = (position - distance) % 100

    return zero_count


if __name__ == "__main__":
    with open("puzzle1_input.txt", "r") as f:
        rotations_input = f.read()
    
    zero_count_part1 = solve_safe_dial(rotations_input)
    print(f"Part 1 - The password is: {zero_count_part1}")
    
    zero_count_part2 = solve_safe_dial_part2(rotations_input)
    print(f"Part 2 - The password is: {zero_count_part2}")
