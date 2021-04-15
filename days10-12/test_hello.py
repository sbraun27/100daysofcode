

# https://docs.python-guide.org/writing/tests/


from hello import hello_name

# Using the unittest method:
import unittest


class TestHello(unittest.TestCase):
    def test_hello_name(self):  # Needs to start with test to be recognized as a test case
        self.assertEqual(hello_name("Steven"), "Hello Steven")


# We don't need unittest either: (Still needs to start with test, though)
def test_hello_name():
    assert hello_name("Steven") == "Hello Steven"


if __name__ == "__main__":
    unittest.main()

    """
    can also use do with "pytest test_hello.py" in the command line. Don't need the 
    """
