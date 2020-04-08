from typing import *


def some_documented_func(arg_name: int) -> Tuple[Any]:
    """
    Description about this function

    :param arg_name: Explanation about this argument
    :return: Explanation about your return value
    :example:
    .. jupyter-execute::

        import your_package_name
        print(your_package_name.some_documented_func(1))
    """
    return arg_name,