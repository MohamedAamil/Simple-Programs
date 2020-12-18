"""
GCD.py : Displays the Greatest Common Divisor of two given Numbers
"""

def get_gcd1(a, b):
    """
    Finding GCD using simple method
    :param a: integer , Number 1
    :param b: integer , Number 2
    """
    smallest = min(a,b)
    if a == 0 or b == 0:
        return max(a,b)
    for i in range(1,smallest+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    print("The GCD of the Number (Method1): ", gcd)


def get_gcd2(a, b):
    """
    Finding GCD using Euclid's Algorithm
    :param a: integer , Number 1
    :param b: integer , Number 2
    """
    rem = a % b
    while rem !=0:
        a = b
        b = rem
        rem = a % b
    print("The GCD of the Number (Method2): ", b)



Number1 = eval(input("Enter First Number: "))
Number2 = eval(input("Enter Second Number: "))
get_gcd1(Number1,Number2)
get_gcd2(Number1,Number2)
