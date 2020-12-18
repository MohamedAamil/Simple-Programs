"""
ReverseNumber.py : Reverses a given Number
"""

def get_reverse(Num):
    """
    Reverses a given Number and Displays it
    :param Num: integer, Number
    """
    Sum = 0
    while Num != 0:
        a = Num % 10
        Sum = Sum * 10 + a
        Num = Num // 10
    print("The Reverse of the Number : ",Sum)


Number = eval(input("Enter a Number: "))
get_reverse(Number)