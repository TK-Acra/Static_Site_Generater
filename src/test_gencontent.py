import unittest
from gencontent import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_h1(self):
        result = extract_title("# Hello\n\nSome content here")
        self.assertEqual(result, "Hello")

    def test_h1_not_first_line(self):
        result = extract_title("Some intro\n\n# The Real Title\n\nMore stuff")
        self.assertEqual(result, "The Real Title")

    def test_h1_white_space(self):
        result = extract_title("#        Lots of space...   ")
        self.assertEqual(result, "Lots of space...")


    def test_h1_exception(self):
        with self.assertRaises(Exception):
            extract_title("## Only an h2\n\nNo h1 here")


if __name__ == "__main__":
    unittest.main()