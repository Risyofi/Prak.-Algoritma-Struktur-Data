import timeit
import matplotlib.pyplot as plt

def measure_insert_time(n, position):
    setup_code = f"my_list = list(range({n}))"
    test_code = f"my_list.insert({position}, 0)"
    execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1)
    return execution_time

sizes = [10**i for i in range(1, 7)]

n = 100
positions = [1, n//2, n]

execution_times = []
for size in sizes:
    for position in positions:
        execution_time = measure_insert_time(size, position)
        execution_times.append((size, position, execution_time))

# Plot grafik waktu eksekusi
for position in positions:
    size_values = [data[0] for data in execution_times if data[1] == position]
    time_values = [data[2] for data in execution_times if data[1] == position]
    plt.plot(size_values, time_values, label=f"Position {position}")
    
plt.xlabel('Size of List')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of insert() Method')
plt.legend()
plt.show()
