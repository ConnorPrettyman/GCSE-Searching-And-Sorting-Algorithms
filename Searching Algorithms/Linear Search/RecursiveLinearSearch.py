# Python 3 script which performs a Recursive Linear Search on an array.
# Returns the index of the target number if it is present, otherwise -1.

# This is time complexity O(n)

# Import time module to demonstrate execution time.
import time


# Set up variables:
array = [1, 3, 4, 7, 15, 22, 36]
target = 22
arrayLength = len(array)

startTime = time.time()

# Set up the Linear Search Function
# Variables have been strongly typed to prevent errors, though this is not necessary.
def linearSearch(array:list[int], arrayLength:int, target:int):

    # If nothing is found, return -1
    if (arrayLength == 0):
        return -1
    
    # If the value of the element is equal to the target, return it.
    # arrayLength - 1 as arrays are zero-indexed.
    elif (array[arrayLength - 1] == target):
        return arrayLength - 1
    
    # If the entire array has not been searched, and target not found
    # recurse the linearSearch function.
    else:
        return linearSearch(array, arrayLength - 1, target)

# Print Array, Target to screen
print(f'Searching the array: {array}\nfor target number: {target}\n')

# Call the Linear Search function
result = linearSearch(array, arrayLength, target)

if result != -1:
    print(f'Target number {target} has been found at array index {result}.')
else:
    print(f'Target number {target} has not been found in the array.')

print(f'\n\nExecution took {(time.time() - startTime)*1000} milliseconds.')
