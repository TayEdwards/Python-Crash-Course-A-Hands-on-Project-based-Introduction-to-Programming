import time

oneMillion_list = [value for value in range(1, 100001)]

print(min(oneMillion_list))
print(max(oneMillion_list))
start_time = time.perf_counter()
print(sum(oneMillion_list))
end_time = time.perf_counter()

total_time = end_time-start_time
print(
    f'The amount of time it took to run sum on a million numbers. {total_time:.3f}')
