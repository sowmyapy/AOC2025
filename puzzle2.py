ip = ""

sum_ids = 0

for r in ip.split(','):
    parts = r.split('-')
    start = int(parts[0])
    end = int(parts[1])
    
    for i in range(start, end + 1):
        s = str(i)
        if len(s) % 2 == 0:
            l = len(s)
            half = l // 2
            if s[0:half] == s[half:l]:
                sum_ids += i

print(f"Sum of all repetition numbers part 1: {sum_ids}")



def is_invalid_id(num_str):

    length = len(num_str)
    
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:

            pattern = num_str[:pattern_len]
            
            repetitions = length // pattern_len
            if pattern * repetitions == num_str:
                return True
    
    return False

sum_ids = 0

for r in ip.split(','):
    parts = r.split('-')
    start = int(parts[0])
    end = int(parts[1])
    
    for i in range(start, end + 1):
        s = str(i)
        if is_invalid_id(s):
            sum_ids += i

print(f"Sum of all invalid IDs (new rules): {sum_ids}")

