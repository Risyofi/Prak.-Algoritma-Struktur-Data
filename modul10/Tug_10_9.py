import timeit
import matplotlib.pyplot as plt

def measure_in_operation_time(n):
    setup_code = f"my_list = list(range({n}))"
    test_code = f"check = {n-1} in my_list"
    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1)
    return execution_time

sizes = [10**i for i in range(1, 7)]

execution_times = []
for size in sizes:
    execution_time = measure_in_operation_time(size)
    execution_times.append((size, execution_time))

size_values = [data[0] for data in execution_times]
time_values = [data[1] for data in execution_times]
plt.plot(size_values, time_values)

plt.xlabel('Size of List')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of "in" Operation')
plt.show()
