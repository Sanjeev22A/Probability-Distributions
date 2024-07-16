import csv
import time
import random
import numpy as np
import matplotlib.pyplot as plt

# Example functions to represent algorithms
def algorithm_a(arr):
    # Implement Bubble Sort to sort the input array
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def algorithm_b(arr):
    for i in arr:
        continue

# Function to measure and store runtimes in CSV files
def measure_and_store_runtimes(filename_a, filename_b, num_samples):
    runtimes_a = []
    runtimes_b = []

    for _ in range(num_samples):
        # Generate a random array of size 100
        input_array = [random.randint(1, 1000) for _ in range(100)]

        start_time = time.time()
        algorithm_a(input_array)
        end_time = time.time()
        runtimes_a.append((end_time - start_time) * 10000000000000)

        start_time = time.time()
        algorithm_b(input_array)
        end_time = time.time()
        runtimes_b.append((end_time - start_time) * 10000000000000)

    with open(filename_a, 'w', newline='') as file_a:
        writer = csv.writer(file_a)
        writer.writerow(runtimes_a)

    with open(filename_b, 'w', newline='') as file_b:
        writer = csv.writer(file_b)
        writer.writerow(runtimes_b)

    return runtimes_a, runtimes_b

# Number of samples (e.g., iterations)
num_samples = 40

# File names for storing runtimes
file_a = 'algorithm_a_runtimes.csv'
file_b = 'algorithm_b_runtimes.csv'

# Measure and store runtimes
runtimes_a, runtimes_b = measure_and_store_runtimes(file_a, file_b, num_samples)

# Calculate the correlation between the two random variables using numpy
correlation = np.corrcoef(runtimes_a, runtimes_b)[0, 1]
correlation = 0 if np.isnan(correlation) else correlation  # Handle division by zero

# Check if both datasets have variance before calculating the correlation
if np.var(runtimes_a) > 0 and np.var(runtimes_b) > 0:
    print("Correlation between runtimes:", correlation)
else:
    print("Correlation cannot be calculated as one or both datasets have no variance.")

# Create a scatter plot to visualize the correlation
plt.scatter(runtimes_a, runtimes_b, c='blue', alpha=0.6, label=f'Correlation: {correlation:.2f}')
plt.xlabel('Algorithm A Runtimes')
plt.ylabel('Algorithm B Runtimes')
plt.title('Scatter Plot of Runtimes')

x = runtimes_a
y = runtimes_b


# Plot the regression lines
plt.plot(x, y, color='red', label=f'Regression Line Algorithm A')
#plt.plot(x, x, color='blue', linestyle='-', label=f'Regression Line Algorithm B')

# Add legends for clarity
plt.legend()

# Display the plot
plt.show()
