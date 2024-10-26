import unittest

def addition(a, b):
    return a + b


def hello(name):
    return f"Hello, {name}!"


class TestSomeMethods(unittest.TestCase):
    
    def test_addition(self):
        result = addition(2, 5)
        self.assertEqual(result, 7)
    
    def test_addition_with_negative_numbers(self):
        result = addition(-5, -3)
        self.assertTrue(result == -8)
    
    
    def test_hello(self):
        result = hello("Alice")
        self.assertEqual(result, "Hello, Alice!")
    
    
    def xtest_hello_with_empty_string(self):
        result = hello("")
        self.assertFalse(result == "")

    def test_addition_with_one_param(self):
        with self.assertRaises(TypeError):
            addition(5)


if __name__ == '__main__':
    unittest.main()

