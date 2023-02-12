record_sec = float(input())
distance_miters = float(input())
swimmer_sec_for_1met = float(input())

total_sec = distance_miters * swimmer_sec_for_1met
resistance = distance_miters // 15 * 12.5

total_time = total_sec + resistance

if total_time < record_sec:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_sec:.2f} seconds slower.")
