"""
Insertion sort

Author: Matthew Yeow
Date modified: 24/6/2018
Preconditions: Array of real numbers
Description: Loop starts with the 2nd element of the array. At each iteration of loop, the number would be inserted into the right position to sort in ascending order.
Complexity: O(n), best case when list is already in ascending order. O(n^2), worst case when list is in descending order.
Stability: Stable
Space: O(n)
Space aux: In-place
"""

def insertionSort(alist):
    """
    Index method
    """
    for index in range(1,len(alist)):
        currentvalue = alist[index]     #current value is set to the value in the array that is to be inserted
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue


def insertionSort2(array):
    """
    Swapping method from right to left
    """
    for k in range(1,len(array)):
        j = k
        while array[j-1] > array[j] and j>0:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1


array = [5.5,4,3.5,3.4,2,1]
insertionSort(array)
print(array)

array2 = [9,8,7,6,5]
insertionSort2(array2)
print(array2)
