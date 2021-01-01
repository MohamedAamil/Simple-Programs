"""
Anagram.py:

Two words are anagrams if you can rearrange the letters from one to spell the
other. Write a function called is_anagram that takes two strings and returns
True if they are anagrams.
Example for anagrams:
rat ⇒ tar, car ⇒ arc, elbow ⇒ below
"""

def is_anagram(str1,str2):
    """
    Checks if the given strings are Anagram
    :param str1: String , Word
    :param str2: String , Word
    :return: Boolean
    """
    for i in range(len(str1)):
        Check = False
        Char = str1[i]
        for j in range(len(str2)):
            if Char == str2[j]:
                Check = True
        if not Check:
            return False
    return True


FirstString = input("Enter First String: ")
SecondString = input("Enter Second String: ")
Result = is_anagram(FirstString,SecondString)

if Result:
    print("Its an Anagram")
else:
    print("Its not an Anagram")