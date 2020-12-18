"""
SumOfDigits.py : Displays the Sum of Digits of the given Number
"""
def get_sumofDigits(Num):
    """
    Calculates the Sum of Digits
    :param Num: integer , Number
    :return:
    """

    Sum = 0
    while Num != 0:
        a = Num % 10
        Sum = Sum  + a
        Num = Num // 10

    print("Sum of Digits : ",Sum)


Num = eval(input("Enter a Number: "))
get_sumofDigits(Num)