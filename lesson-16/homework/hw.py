
#1
import numpy as np

# Original list
original_list = [12.23, 13.32, 100, 36.32]
print("Original List:", original_list)

# Convert to 1D NumPy array
array_1d = np.array(original_list)
print("One-dimensional NumPy array:", array_1d)

#2
import numpy as np

# Create an array with values from 2 to 10 (inclusive)
arr = np.arange(2, 11)

# Reshape to 3x3 matrix
matrix = arr.reshape(3, 3)

print(matrix)

#3
import numpy as np

# Create null vector (all zeros) of size 10
vec = np.zeros(10)
print("Original vector:")
print(vec)

# Update sixth value (index 5) to 11
vec[5] = 11
print("\nUpdated vector:")
print(vec)

#4
import numpy as np

arr = np.arange(12, 38)
print(arr)

#5
import numpy as np

# Original integer array
arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

# Convert to float type
arr_float = arr.astype(float)
print("Array converted to float type:", arr_float)

#6
import numpy as np

# Sample array of Celsius temperatures
celsius = np.array([0, 12, 45.21, 34, 99.91])

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

print("Values in Celsius degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

#7
import numpy as np

# Original array
original_array = np.array([10, 20, 30])
print("Original array:", original_array)

# Values to append
values_to_append = [40, 50, 60, 70, 80, 90]

# Append values to the original array
new_array = np.append(original_array, values_to_append)
print("After append values to the end of the array:", new_array)

#8
import numpy as np

# Create random array of 10 elements (values between 0 and 100)
arr = np.random.randint(0, 101, size=10)
print("Random array:", arr)

# Calculate statistics
mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)

print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Standard Deviation: {std_dev}")

#9
import numpy as np

# Create a 10x10 array with random values between 0 and 1
arr = np.random.random((10, 10))
print("Array:\n", arr)

# Find minimum and maximum values
min_val = np.min(arr)
max_val = np.max(arr)

print(f"\nMinimum value: {min_val}")
print(f"Maximum value: {max_val}")

#10
import numpy as np

# Create 3x3x3 array with random floats between 0 and 1
arr = np.random.random((3, 3, 3))
print(arr)
