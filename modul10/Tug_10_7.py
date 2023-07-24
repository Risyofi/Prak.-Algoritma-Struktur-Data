import timeit
import matplotlib.pyplot as plt

def measure_append_time(n):
    setup_code = f"my_list = []"
    test_code = f"my_list.append(1)"
    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=n)
    return execution_time

sizes = [10**i for i in range(1, 7)]

execution_times = []
for size in sizes:
    execution_time = measure_append_time(size)
    execution_times.append(execution_time)

plt.plot(sizes, execution_times)
plt.xlabel('Size of List')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of append() Method')
plt.show()