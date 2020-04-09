from typing import List


# TypeErrors are raised when running functions with:
# [[1, [2]], [[[3]]], 4, [[5, 6], [[[7]]]]]

# Design recipe for recursive functions:

# def f(obj: Union[int, List]) -> ...:
#     if isinstance(obj, int):
#         ...
#     else:
#         for sublist in obj:
#             ... f(sublist) ...

def sum_list(lst: List[int]) -> int:
    """Return the sum of the items in a list of numbers.
    """
    s = 0
    for num in lst:
        # num is an int
        s += num
    return s


def sum_list2(lst: List[List[int]]) -> int:
    """Return the sum of the items in a list of lists of numbers.
    """
    s = 0
    for list_of_nums in lst:
        # list_of_nums is a List[int]
        s += sum_list(list_of_nums)
    return s


def sum_list3(lst: List[List[List[int]]]) -> int:
    """Return the sum of the items in a list of lists of lists of numbers.
    """
    s = 0
    for list_of_lists_of_nums in lst:
        # list_of_lists_of_nums is a List[List[int]]
        s += sum_list2(list_of_lists_of_nums)
    return s
