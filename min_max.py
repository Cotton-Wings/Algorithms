"""

Min-Max Algorithm

Author: Matthew Yeow
Date modified: 26/6/2018
Preconditions: Array of real numbers
Description: Finding the minimum and maximum value in the array
Complexity: O(n)
Space: O(n)
Space aux: In-place
"""

def find_min(array):
    minimum = array[0]
    for i in range(1, len(array)):
        if array[i] < minimum:
            minimum = array[i]
    return minimum

"""
If we consider the case of finding both the minimum and maximum element at the same time.
Clearly, our first algorithm for finding the minimum in N − 1 comparisons could easily be adapted
to find both the minimum and maximum in 2N − 2 comparisons, but can we do better?
"""

def find_min_max(array):
    """
    We can compute minimum and maximum in 3/2N comparisons
    """
    minimum = array[0]
    maximum = array[0]
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            if array[i] < minimum:
                minimum = array[i]
                
            if array[i+1] > maximum:
                maximum = array[i+1]

        else:   
            if array[i] > maximum:
                maximum = array[i]

            if array[i+1] < minimum:
                minimum = array[i+1]

    return minimum, maximum

alist = [26,93,44,20,77,31,36,28,55,17,11,123]
print(find_min_max(alist))


            
