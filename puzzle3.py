with open("puzzle3_ip.txt", "r") as f:
    ip = f.read()

lines = ip.strip().split('\n')

joltage = 0

for line in lines:
    x = max(line)
    x_pos = line.find(x) + 1
    if x_pos == len(line):
        x_max_2 = max(line.replace(x,''))
        x_pos_2 = line.find(x_max_2)
        x_pos = x_pos_2 + 1
    x = line[x_pos - 1]
    y = max(line[x_pos:])
    z = x + y
    final = int(z)
    joltage += final
print("Part1 joltage -> ", joltage)


sum_12 = 0

for line in lines:
    n = len(line)
    result = []
    start = 0
    
    for i in range(12):
        remaining_needed = 12 - i - 1        
        end = n - remaining_needed
        
        max_digit = max(line[start:end])
        pos = line.find(max_digit, start)
        
        result.append(max_digit)

        start = pos + 1
    #print(result)
    
    final_number = ''.join(result)
    sum_12 += int(final_number)

print("part2 joltage -> ", sum_12)
