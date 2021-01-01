"""
Cumulative_Sum.py :

Write a function called cumsum that takes a list of numbers and returns the
cumulative sum; that is, a new list where the ith element is the sum of the
first i + 1 elements from the original list.
Eg: t = [1, 2, 3]
cumsum(t) ⇒ [1, 3, 6]

"""
def cumsum(Arr):
    """
    Finds the Cumulative Sum
    :param Arr: List , Numbers
    :return Sum: List , New List of Numbers
    """

    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
        Arr[i] = Sum

    return Arr

t = [1,2,3]
print(cumsum(t))