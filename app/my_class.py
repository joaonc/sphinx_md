"""
This is the docstring for the module.
"""
from typing import Any, Optional, Union


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

        :return: `True` if it's ok, `False` otherwise.
        """
        return self.a > 0 and self.b.lower() == 'ok'

    def with_typehints_1(self, name: str, x: Optional[str] = None, i: Union[float, int] = 0):
        """
        Method with type hints to see how they look in the documentation.

        The return type is type is not specified in the method signature or in the `:return:` portion of the
        docstring.

        :param name: The name of something.
        :param x: Mysterious argument.
        :param i: A Number for the sake of it. Uses the `Union` syntax.
        """
        pass

    def with_typehints_2(self, no_th, a: Any, i: float | int) -> list[tuple[int, str, Any]]:
        """
        Another method with type hints to see how it looks in documentation.

        Return type is complicated.

        :param no_th: Parameter with no type hint.
        :param a: Can be anything.
        :param i: A Number for the sake of it. Uses the `|` syntax.
        :return: A list of stuff.
        """
        return []
