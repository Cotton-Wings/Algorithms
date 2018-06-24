"""
Selecttion sort

Author: Matthew Yeow
Date modified: 24/6/2018
Preconditions: Array of real numbers
Description: At each iteration of loop, the minimum value would be found and swap into the right position to sort in ascending order. Sorted values on the left are not iterated again.
Complexity: O(n^2)
Space: O(n)
Space aux: In-place
"""

def selectionSort(array):
    """
    Index method
    """
    for i in range(len(array)):
        minimumPosition = i
        for j in range(i, len(array)):
            if array[j] < array[minimumPosition]:
                minimumPosition = j
        array[i], array[minimumPosition] = array[minimumPosition], array[i]

array = [5,4,3,2,1]
selectionSort(array)
print(array)

array2 = [9.9, 4.5, 3.45, 12.031, 19.4]
selectionSort(array2)
print(array2)
