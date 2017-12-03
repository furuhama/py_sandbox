""" This is a test program"""


def binary_search(arg_list, value):
    """
    Binary Search

    if value in list -> print 'Found' & return True
    else -> print 'Not Found' & return False
    """
    low = 0
    high = len(arg_list) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arg_list[mid] == value:
            print("Found!!!")
            return True
        elif arg_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    print("Not Found...")
    return False


#
# main
#
if __name__ == '__main__':
    MY_LIST = range(20)
    binary_search(MY_LIST, -50)  # False
    binary_search(MY_LIST, 20)  # False
    binary_search(MY_LIST, 19)  # True
    binary_search(MY_LIST, 0)  # True
    binary_search([1, 3, 7, 9, 10, 26, 36, 58, 99], 26)  # True
