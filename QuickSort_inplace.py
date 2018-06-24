"""
Quick sort with In-place Partitioning

Author: Matthew Yeow
Date modified: 24/6/2018
Preconditions: Array of real numbers
Description: A pivot is selected and array is partitioned based on the pivot value. Pivot selection and partioning continues with the partitioned arrays.
Complexity: O(n log n), best case when pivot selected is always the median value of the array. O(n^2), worst case when pivot chosen is the smallest or biggest value of the array.
Stability: Unstable
Space aux: O(log n)
Space: O(n)
"""
def partition(alist, first, last):
    """
    Partitioning looks for the right position for the pivot to be swapped.
    """
    pivot = alist[first]
    LBAD = first + 1
    RBAD = last - 1

    while LBAD <= RBAD:
        while LBAD <= RBAD and alist[LBAD] <= pivot:
            LBAD = LBAD + 1

        while LBAD <= RBAD and alist [RBAD] > pivot:
            RBAD = RBAD - 1

        if LBAD <= RBAD:
            alist[LBAD],alist[RBAD] = alist[RBAD], alist[LBAD]

    alist[first], alist[RBAD] = alist[RBAD], alist[first]
    return RBAD

def quick_sort(alist, first, last):
    if (last - first) > 1:
        print("partitioning", alist[first:last], "pivot",alist[first])
        pivot_pos = partition(alist,first,last)
        print("partitioned:", alist[first:last])

        print("Splitting into two", alist[first:pivot_pos],alist[pivot_pos+1:last])
        quick_sort(alist,first,pivot_pos)
        quick_sort(alist,pivot_pos+1,last)

alist = [26,93,44,20,77,31,36,28,55,17]
quick_sort(alist,0,len(alist))
print(alist)
