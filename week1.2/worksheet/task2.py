# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
 
numbers = read_numbers()
 
if len(numbers) == 0:
    sys.exit("Error: no numbers provided")
 
numbers.sort()
count = len(numbers)
middle = count // 2
 
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / count
 
if count % 2 == 1:
    median = numbers[middle]
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2
 
print("Minimum =", minimum)
print("Maximum =", maximum)
print("Mean =", mean)
print("Median =", median)
