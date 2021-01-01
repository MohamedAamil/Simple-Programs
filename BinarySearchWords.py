"""
BinarySearchWords.py

To check whether a word is in the word list, you could use the in operator, but
it would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with a
bisection search (also known as binary search), which is similar to what you
do when you look a word up in the dictionary (the book, not the data
structure). You start in the middle and check to see whether the word you are
looking for comes before the word in the middle of the list. If so, you search
the first half of the list the same way. Otherwise you search the second half.
Either way, you cut the remaining search space in half. If the word list has
113,809 words, it will take about 17 steps to find the word or conclude that it’s
not there.
Write a function called in_bisect that takes a sorted list and a target value and
returns True if the word is in the list and False if it’s not

"""


def in_bisect(Target, Strings):
    """
    Searches for the Element using Binary Search
    :param Target: String , Word
    :param Strings: List , Words
    :return: Boolean
    """
    First = 0
    Last = len(Strings) - 1

    while First <= Last:
        Mid = (First + Last) // 2
        if Target == Strings[Mid]:
            return Mid+1
        elif Target < Strings[Mid]:
            Last = Mid - 1
        else:
            First = Mid + 1
    else:
        return False


Length = eval(input("Enter Range: "))
Arr = []
for i in range(Length):
    Words = eval(input("Enter Sorted String : "))
    Arr.append(Words)

Elem = input("\n Enter Element to search: ")
Pos = in_bisect(Elem,Arr)
if not Pos:
    print("Element not Found!!")
else:
    print("\n Element found in Position : ", Pos)