"""
Docstring for the test module.
"""
from my_class import MyClass


class TestMyClass:
    """
    Docstring for the test class.
    """

    def test_is_ok(self):
        """
        Tests if it's ok.
        """
        assert MyClass(1, 'OK').is_ok() is True

    def test_is_not_ok(self):
        """
        Tests that it's not ok.
        """
        assert MyClass(0, 'ok').is_ok() is False
