"""
FermatsTheorem.py : Checks for validity of the Fermat's Last Theorem
"""

def check_fermat(a,b,c,n):
    """
    Checks validity of Fermat's Theorem
    :param a: integer , Number
    :param b: integer , Number
    :param c: integer , Number
    :param n: integer , Power
    """
    A = a**n
    B = b**n
    C = c**n

    if n > 2 and (A + B == C):
        print("Holy Smokes, Fermat was wrong")
    else:
        print("No, that doesnt work")


def get_values():
    """
    Get values from the user and calls function check_fermat()
    """
    a = eval(input("Enter the value of A: "))
    b = eval(input("Enter the value of B: "))
    c = eval(input("Enter the value of C: "))
    n = eval(input("Enter the value of n: "))

    check_fermat(a,b,c,n)

get_values()