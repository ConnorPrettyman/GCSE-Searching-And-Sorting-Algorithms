# Python 3 script which performs a Recursive Binary Search on an array.
# Returns the index of the target number if it is present, otherwise -1.

# This is time complexity O(log n)

# Import time module to demonstrate execution time.
import time

# Set up variables:
array = [1, 3, 4, 7, 15, 22, 36]
target = 22

startTime = time.time()

# Set up the Binary Search Function
# Variables have been strongly typed to prevent errors, though this is not necessary.
def binarySearch(array:list[int], left:int, right:int, target:int):
    
    # Check base case
    if right >= left:

        middle = left + (right - left) // 2 # Floor Division (Math.Floor();)

        # If the target number IS the middle value:
        if array[middle] == target:
            return middle
        
        # If the target number is SMALLER than the middle value,
        # it must be within the left sub-array.
        elif array[middle] > target:
            return binarySearch(array, left, middle - 1, target) # RECURSION
        
        # Else, the target number must be in the right sub-array.
        else:
            return binarySearch(array, middle + 1, right, target)
    
    # If no prior conditions are met (number not found)
    else:
        return -1

# Print Array, Target to screen
print(f'Searching the array: {array}\nfor target number: {target}\n')

# Call the Binary Search function
result = binarySearch(array, 0, len(array)-1, target)

if result != -1:
    print(f'Target number {target} has been found at array index {result}.')
else:
    print(f'Target number {target} has not been found in the array.')

print(f'\n\nExecution took {(time.time() - startTime)*1000} milliseconds.')
