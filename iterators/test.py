import time
gen_start_time = time.time()
print(sum(num for num in range(1, 1000000)))
gen_end_time = time.time() - gen_start_time

print(f"gen_time: {gen_end_time}")


list_start_time = time.time()
print(sum([num for num in range(1, 1000000)]))
list_end_time = time.time() - list_start_time

print(f"list_time: {list_end_time}")
