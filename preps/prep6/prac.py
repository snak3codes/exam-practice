from typing import Union, List


def sum_nested(obj: Union[int, List]) -> int:
    """Return the sum of the numbers in a nested list <obj>.
    """
    if isinstance(obj, int):
        return obj
    else:
        s = 0
        for sublist in obj:
            s += sum_nested(sublist)
    return s


print(sum_nested([[3], [[3, 2, 1]], [1, 2, 3], [[[[4, 5, 6]]]]]))

# Running the function should return 30 because
# 3 + 3 + 2 + 1 + 1 + 2 + 3 + 4 + 5 + 6 = 30
