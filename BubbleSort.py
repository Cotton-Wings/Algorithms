"""

Bubble sort

Author: Matthew Yeow
Date modified: 26/6/2018
Preconditions: Array of real numbers
Description: Lighter bubbles rise to the top, heavier ones sink to the bottom. 
Complexity: O(n), best case when list is already in ascending order. O(n^2), worst case when list is in descending order.
Stability: Stable
Space: O(n)
Space aux: In-place
"""

def bubbleSort(array):
    """
    Naive method
    Best case time complexity is O(n^2), since there is no way of escaping the nested loop
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def bubbleSort2(array):
    """
    Improved bubble sort
    """
    for i in range(len(array) - 1, 0, -1):
        flag = False
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if flag == False:
            break

alist = [26,93,44,20,77,31,36,28,55,17]
bubbleSort2(alist)
print(alist)
    
