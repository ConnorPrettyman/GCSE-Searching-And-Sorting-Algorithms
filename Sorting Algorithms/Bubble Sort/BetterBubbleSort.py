# Python 3 script which performs a Bubble Sort operation on an array.

# This is time complexity O(n^2)

# Import time module to demonstrate execution time.
import time

# Set up variables:
array = [18, 13, 28, 14, 17, 3, 7]
startTime = time.time()

# Set up the Bubble Sort Function
# Variables have been strongly typed to prevent errors, though this is not necessary.
def betterBubbleSort(array:list[int]):
    arrayLen = len(array)

    # Search through all array elements
    for i in range(arrayLen):
        swapped = False

        # Last i elements are already in place.
        for j in range(0, arrayLen - i - 1):

            # If right value greater than left value
            if array[j] > array[j+1]:

                # Swap them
                tempVal = array[j]
                array[j] = array[j+1]
                array[j+1] = tempVal
                swapped = True
        
        # If no swap was needed, stop the algorithm.
        if (swapped == False):
            break

# Print Array, Target to screen
print(f'Current array order: {array}\n')

# Call the Bubble Sort function
betterBubbleSort(array)

print(f'Array has now been sorted: {array}')

print(f'\n\nExecution took {(time.time() - startTime)*1000} milliseconds.')
