ip = "4077-5314,527473787-527596071,709-872,2487-3128,6522872-6618473,69137-81535,7276-8396,93812865-93928569,283900-352379,72-83,7373727756-7373754121,41389868-41438993,5757-6921,85-102,2-16,205918-243465,842786811-842935210,578553879-578609405,9881643-10095708,771165-985774,592441-692926,7427694-7538897,977-1245,44435414-44469747,74184149-74342346,433590-529427,19061209-19292668,531980-562808,34094-40289,4148369957-4148478173,67705780-67877150,20-42,8501-10229,1423280262-1423531012,1926-2452,85940-109708,293-351,53-71"

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

