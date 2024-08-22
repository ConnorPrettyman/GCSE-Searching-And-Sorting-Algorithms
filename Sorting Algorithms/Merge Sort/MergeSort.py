# Python 3 script which performs a Merge Sort operation on an array.

# This is time complexity O(n Log(n))

# Import time module to demonstrate execution time.
import time

# Set up variables:
array = [18, 13, 28, 14, 17, 3, 7]
startTime = time.time()

# Set up the Insertion Sort Function
# Variables have been strongly typed to prevent errors, though this is not necessary.
def mergeSort(array:list[int]):

    # If the array has more than one item within it
    if len(array) > 1:

        # Find the middle value of the Array
        middle = len(array)//2

        # Left half is from start of array to the middle value.
        left = array[:middle]

        # Right half is from the middle value to the end of the array
        right = array[middle:]

        # Recursively sort both halves of the array
        mergeSort(left)
        mergeSort(right)

        # Initialise 3 pointer vars, one per array, each equal 0.
        leftPointer = rightPointer = arrayPointer = 0

        # Copy data to temporary arrays left[] and right[]
        while leftPointer < len(left) and rightPointer < len(right):
            if left[leftPointer] <= right[rightPointer]:
                array[arrayPointer] = left[leftPointer]
                leftPointer += 1
            else:
                array[arrayPointer] = right[rightPointer]
                rightPointer += 1
            arrayPointer += 1
        
        # Checking if any element was left
        while leftPointer < len(left):
            array[arrayPointer] = left[leftPointer]
            leftPointer += 1
            arrayPointer += 1
  
        while rightPointer < len(right):
            array[arrayPointer] = right[rightPointer]
            rightPointer += 1
            arrayPointer += 1

# Print Array, Target to screen
print(f'Current array order: {array}\n')

# Call the Merge Sort function
mergeSort(array)

print(f'Array has now been sorted: {array}')

print(f'\n\nExecution took {(time.time() - startTime)*1000} milliseconds.')
