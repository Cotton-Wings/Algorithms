"""
Stable Quick Sort

Author: Matthew Yeow
Date modified: 26/6/2018
Preconditions: Array of real numbers
"""
def quickSort(alist):
    left = []
    mid = []
    right = []

    if len(alist) > 1:
        pivot = alist[0]
        mid.append(pivot)
        for i in range(1,len(alist)):
            if alist[i] < pivot:
                left.append(alist[i])
            if alist[i] == pivot:
                mid.append(alist[i])
            if alist[i] > pivot:
                right.append(alist[i])

        return quickSort(left)+mid+quickSort(right)
    else:
        return alist
    
alist = [26,93,44,20,77,31,36,28,55,17]
print(quickSort(alist))
