"""
Linear_search.py: Finds an element from a given List using Linear Search
"""

def linear_search(Arr,Elem):
    """
    Finding ElemEnt using Linear Search
    :param Arr: List , Numbers
    :param Elem: Integer , Number
    """

    for i in range(len(Arr)):
        if Arr[i] == Elem:
            print("Element found in position: ",i+1)
            break
    else:
        print("Not Found")

Length = eval(input("Enter Range: "))
Arr = []
for i in range(Length):
    Num = eval(input("Enter Number: "))
    Arr.append(Num)

Elem = eval(input("\n Enter Element to search: "))
linear_search(Arr,Elem)