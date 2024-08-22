# Python 3 script which performs an Insertion Sort operation on an array.

# This is time complexity O(n^2)

# Import time module to demonstrate execution time.
import time

# Set up variables:
array = [18, 13, 28, 14, 17, 3, 7]
startTime = time.time()

# Set up the Insertion Sort Function
# Variables have been strongly typed to prevent errors, though this is not necessary.
def insertionSort(array:list[int]):

    # Search through index 1 -> Array Length
    for i in range(1, len(array)):

        # Record key value
        keyVal = array[i]

        # j = item in previous array index
        j = i - 1

        # Move elements that are >keyVal to an array index
        # 1 greater than their current array index.
        while j >= 0 and keyVal < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = keyVal

# Print Array, Target to screen
print(f'Current array order: {array}\n')

# Call the Insertion Sort function
insertionSort(array)

print(f'Array has now been sorted: {array}')

print(f'\n\nExecution took {(time.time() - startTime)*1000} milliseconds.')
