"""
Nested_Sum.py :

Write a function called nested_sum that takes a list of lists of integers and
adds up the elements from all of the nested lists
Eg: t = [ [1, 2], [3], [4, 5, 6] ]
nested_sum(t) ⇒ 21
"""

def nested_sum(Arr):
    """
    Finds the Nested Sum of the given list
    :param Arr: List , Numbers
    :return Sum: Integer , Sum Value
    """

    Sum = 0
    for i in Arr:
        Sum = Sum + sum(i)
    return Sum


t = [[1,2],[3],[4,5,6]]
print(nested_sum(t))
