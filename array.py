'''1. Basic Array Operations (Using Lists) 🐍
Python's list is the most common way to represent an array. It's a collection of items that are ordered and mutable (changeable).

Creating an Array:
'''
my_array = [10, 20, 30, 40, 50]
#Accessing Elements:
#You access elements by their index, which starts at 0.
  
# Access the first element
first_element = my_array[0]  # Output: 10

# Access the last element
last_element = my_array[-1]  # Output: 50
Modifying Elements:
You can change an element by assigning a new value to its index.

Python

my_array[2] = 99  # my_array is now [10, 20, 99, 40, 50]
Adding/Removing Elements:

Append: Adds an element to the end.

Python

my_array.append(60) # my_array is now [10, 20, 99, 40, 50, 60]
Insert: Adds an element at a specific index.

Python

my_array.insert(1, 15) # my_array is now [10, 15, 20, 99, 40, 50, 60]
Remove: Removes the first occurrence of a value.

Python

my_array.remove(99) # my_array is now [10, 15, 20, 40, 50, 60]
Pop: Removes and returns an element at a specific index (or the last one if no index is given).

Python

removed_item = my_array.pop(3) # removed_item is 40; my_array is [10, 15, 20, 50, 60]
2. Common Array Programs and Logic
Most array-related problems involve iterating through the elements and performing some action.

Finding the Largest/Smallest Element
To find the largest element, you can assume the first element is the largest, then iterate through the rest of the array and update your "largest" variable if you find a bigger number.

Python

numbers = [25, 12, 56, 8, 90, 33]
largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print("The largest number is:", largest_number) # Output: 90
Summing All Elements
This is a straightforward loop. You initialize a total variable to 0 and add each element to it.

Python

numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print("The sum is:", total) # Output: 15
Alternatively, you can use the built-in sum() function for a more concise solution: total = sum(numbers).

Reversing an Array
You can reverse an array in place or create a new reversed one.

Python

original_array = [10, 20, 30, 40]

# Method 1: Using slicing (creates a new array)
reversed_array_slice = original_array[::-1]
print(reversed_array_slice) # Output: [40, 30, 20, 10]

# Method 2: In-place reversal
original_array.reverse()
print(original_array) # Output: [40, 30, 20, 10]
Finding a Specific Element
To check if an element exists in an array, you can loop through it or use Python's in operator.

Python

my_array = ["apple", "banana", "cherry"]

# Using a loop
found = False
for item in my_array:
    if item == "banana":
        found = True
        break # Exit the loop once found

print("Is 'banana' in the array?", found)

# Using the 'in' operator (more Pythonic)
if "banana" in my_array:
    print("Yes, it's there!")
3. The array Module
For more memory-efficient storage of a large number of items of the same data type (like all integers or all floats), Python has a dedicated array module. This is useful for scientific or data-intensive applications.

Python

from array import array

# 'i' stands for signed integer
int_array = array('i', [1, 2, 3, 4])
print(int_array) # Output: array('i', [1, 2, 3, 4])
While this is a specialized tool, most beginners should stick with lists, which are more versatile and generally easier to use.
