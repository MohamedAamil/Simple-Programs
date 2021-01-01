"""
SortedList.py:

Write a function called is_sorted that takes a list as a parameter and returns
True if the list is sorted in ascending order and False otherwise. For example:
Eg: is_sorted([1, 2, 2]) ⇒ True
is_sorted(['b', 'a']) ⇒ False
"""

def is_sorted(Arr):
    """
    Checks if the List is Sorted
    :param Arr: List , Elements
    :return: Boolean
    """

    n = 0
    while n < len(Arr) - 1:
        if Arr[n] > Arr[n+1]:
            return False
        n += 1
    return True

Arr1 = ['A','C','B']
Arr2 = [1,2,2]

print(is_sorted(Arr1))
print(is_sorted(Arr2))