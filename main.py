import re

my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

def OrganizeList(myList):
    for item in myList:
        assert type(item) == int, "Word list must be a list of strings"
    myList.sort()
    return myList


def main():
   print(RemoveValue(27))
   print(RemoveValue(27))


if __name__ == "__main__":
    main()
# main
