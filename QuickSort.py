"""
Quick sort Auxiliary

Author: Matthew Yeow
Date modified: 24/6/2018
Preconditions: Array of real numbers
Description: A pivot is selected and array is partitioned based on the pivot value. Pivot selection and partioning continues with the partitioned arrays.
Complexity: O(n log n), best case when pivot selected is always the median value of the array. O(n^2), worst case when pivot chosen is the smallest or biggest value of the array.
Stability: Unstable
Space aux: O(log n)
Space: O(n)
"""

def quick_sort(array):
    start = 0
    end = len(array) - 1
    quick_sort_aux(array, start, end)

def quick_sort_aux(array, start, end):
    if start < end:
        boundary = partition(array, start, end)
        quick_sort_aux(array, start, boundary-1)
        quick_sort_aux(array, boundary+1, end)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
def partition(array, start, end):
    mid = (start + end)//2
    pivot = array[mid]
    swap(array, start, mid)
    index = start
    for k in range(start+1, end+1):
        if array[k] < pivot:
            index += 1
            swap(array, k, index)
    swap(array, start, index)
    return index

array = [5,9,2,3,2,1,6,7,0]
quick_sort(array)
print(array)
