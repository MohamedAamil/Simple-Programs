"""
Has_Duplicates.py:

Write a function called has_duplicates that takes a list and returns True if
there is any element that appears more than once. It should not modify the
original list
"""

def has_duplicates(L):
    """
    Checks for Duplicate Values
    :param L: List , Elements
    :return: Boolean
    """
    
    S = set(L)
    if len(S) == len(L):
        return False
    else:
        return True

Arr = ['apple','orange','Ball',12,43,'apple']
print(has_duplicates(Arr))