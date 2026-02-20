import numpy as np
import time

def print_logs(task,status):
    print("="*20)
    print(f"Task {task} {status}")
    print("="*20)


# Task 1
print_logs(1,"Create an Array and Basic Math Started")
temp_celsius = np.array([22, 25, 28, 24, 26])
print(f"Celsius: {temp_celsius}")
fahrenheit = temp_celsius * 1.8 + 32
print(f"Fahrenheit: {fahrenheit}")
average = np.average(fahrenheit)
print(f"Average Fahrenheit: {average: .1f}")
print_logs(1,"Create an Array and Basic Math Completed")


# Task 2
print_logs(2,"Array Shape and Statistics Started")
test_scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print("Shape: ", np.shape(test_scores))
print(f"Total elements: {np.size(test_scores)}")
print(f"Highest score: {np.max(test_scores)}")
print(f"Lowest score: {np.min(test_scores)}")
print(f"Range: {np.max(test_scores) - np.min(test_scores)}")
print_logs(2,"Array Shape and Statistics Completed")

# Task 3
print_logs(3,"Performance Comparison Started")
tmp_array = np.arange(1,50001)
tmp_list = list(range(1,50001))

start_time = time.time()
sum_array = np.sum(tmp_array)
end_time = time.time()
array_execution_time = end_time - start_time

start_time = time.time()
sum_list = sum(tmp_list)
end_time = time.time()
list_execution_time = end_time - start_time

print(f"NumPy sum: {sum_array}")
print(f"Python sum: {sum_list}")
print(f"NumPy time: {array_execution_time: .4f}")
print(f"Python time: {list_execution_time: .4f}")
print(f"NumPy is: {list_execution_time/array_execution_time:.1f}x faster")
print_logs(3,"Performance Comparison Completed")