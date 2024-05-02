'''
Not a leetcode problem, but something that is useful for getting better sort algorithms for things like ValidAnagram and other things that can be solved using sorting.
'''

def QSort(array, leftP, rightP):
    '''
    the quicksort function takes 3 parameters: the array to sort, the left pointer, and the right pointer
    '''
    if leftP < rightP:
        '''
        if the left pointer is less than the right pointer, there are at 2 elements to sort. If not, the function returns because the array is either empty or contains one element.
        '''
        partition_position = partition(array, leftP, rightP)
        '''
        after partition is called, the pivot element is in its final position. Then QSort is called recursively on each side of the pivot element.
        '''
        QSort(array, leftP, partition_position - 1)
        QSort(array, partition_position + 1, rightP)

import random
# random is used to choose a random pivot point

def partition(array, leftP, rightP):
    pivot_index = random.randint(leftP, rightP)
    pivot = array[pivot_index]

    array[pivot_index], array[rightP] = array[rightP], array[pivot_index]

    '''
    A random pivot is chosen and swapped with the rightmost element in the subarray (rightP).
    '''

    # Initialize two pointers, i starts from the left end of the subarray

    i = leftP
    j = rightP - 1

    while i < j:
        # Move i to the right, skipping elements less than the pivot
        while i < rightP and array[i] < pivot:
            i += 1
        # Move j to the left, skipping elements greater than or equal to the pivot
        while j > leftP and array[j] >= pivot:
            j -= 1

        # If i and j haven't crossed each other, swap the elements at i and j
        if i < j:
            array[i], array[j] = array[j], array[i]

    # After i and j have crossed, if the element at i is greater than the pivot, swap these elements
    if array[i] > pivot:
        array[i], array[rightP] = array[rightP], array[i]

    return i


def Test_QSort():
    arr = list("nagaram")
    print("Unsorted:")
    print(arr)

    QSort(arr, 0, len(arr) - 1)
    print("Sorted:")
    print(arr)


Test_QSort()
