"""
Palindrome.py : Checks if the given String is Palindrome
"""

def is_palindrome(word):
    """
    Checks for Palindrome String
    :param word: string , Word
    :return: Boolean , Palindrome or not
    """

    length = len(word)

    for i in range (0,length):
        if word[i] == word[length - 1]:
            pass
        else:
            return False

        length -= 1

    return True


Word = input("Enter a Word: ")
val = is_palindrome(Word)
if val:
    print("Its a Palindrome")
if not val:
    print("Not a Palindrome")