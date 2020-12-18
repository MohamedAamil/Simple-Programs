"""
NewtonsSquareRoot.py : Finds the Square Root of a Number using Newton's Method
"""

def get_squareroot(Num):
    """
    Gets the Square Root of a Number
    :param Num: integer , Number
    """

    precision = 10 ** -15
    n = Num
    while abs(Num - n * n) > precision :
        n = (n + Num / n) / 2

    print("The Square Root of the Number : ",n)


Number = eval(input("Enter a Number : "))
get_squareroot(Number)
