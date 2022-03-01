"""
This is the docstring for the module.
"""


class MyClass:
    """
    This is the docstring for the class.
    """

    def __init__(self, a: int, b: str = 'sample'):
        """
        Init of `MyClass`.

        :param a: A required parameter that's an int.
        :param b: Just another parameter.
        """
        self.a = a
        self.b = b

    def is_ok(self) -> bool:
        """
        Check if it's *ok*.

        :return: `True` if it's ok, `False` oherwise.
        """
        return self.a > 0 and self.b.lower() == 'ok'
