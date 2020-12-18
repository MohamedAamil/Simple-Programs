"""
Palindrome.py : Checks if the given Number is Palindrome
"""

def check_palindrome(Num):
    """
    Checks for Palindrome
    :param Num: integer, Number
    :return:
    """
    Sum = 0
    Number = Num
    while Num != 0:
        a = Num % 10
        Sum = Sum*10 + a
        Num = Num // 10

    if Sum == Number:
        print("Its a Palindrome Number")
    else:
        print("Not a Palindrome Number")



Number = eval(input("Enter a Number: "))
check_palindrome(Number)

