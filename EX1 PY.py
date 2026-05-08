my_list = [7, 14, 21, 2, 8, 14, 35, 42, 8, 49, 10, 35]
set_from_list = set(my_list)
print(f"Set from list (duplicates removed): {set_from_list}")
set_divisible_by_7 = {i for i in range(1, 51) if i % 7 == 0}
print(f"Set of numbers divisible by 7 (1-50): {set_divisible_by_7}")
intersection_set = set_from_list.intersection(set_divisible_by_7)
print(f"Intersection of both sets: {intersection_set}")
sorted_result_list = sorted(intersection_set)
print(f"Result as a sorted list: {sorted_result_list}")
