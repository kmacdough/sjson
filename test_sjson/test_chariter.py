import unittest
import io
from sjson.chariter import *


class FileCharIterTest (unittest.TestCase):
    """
    Tests the FileCharIterTest class
    """
    def test_iterator(self):
        test_str = "hello"
        char_iter = FileCharIter(io.StringIO(test_str))
        for expected, actual in zip(test_str, char_iter):
            self.assertEqual(expected, actual)

    def test_get_char_const(self):
        test_str = "hello"
        char_iter = FileCharIter(io.StringIO(test_str))
        char_iter.advance()
        self.assertEqual(test_str[0], char_iter.cur_char())
        self.assertEqual(test_str[0], char_iter.cur_char())
        self.assertEqual(test_str[0], char_iter.cur_char())

    def test_get_char_advance(self):
        test_str = "hello"
        char_iter = FileCharIter(io.StringIO(test_str))
        char_iter.advance()
        self.assertEqual(test_str[0], char_iter.cur_char())
        char_iter.advance()
        self.assertEqual(test_str[1], char_iter.cur_char())
        char_iter.advance()
        self.assertEqual(test_str[2], char_iter.cur_char())

    def test_get_char_multiple_advance(self):
        test_str = "hello"
        char_iter = FileCharIter(io.StringIO(test_str))
        char_iter.advance()
        self.assertEqual(test_str[0], char_iter.cur_char())
        char_iter.advance()
        char_iter.advance()
        char_iter.advance()
        self.assertEqual(test_str[3], char_iter.cur_char())

    def test_get_next_char_1(self):
        test_str = "hello"
        char_iter = FileCharIter(io.StringIO(test_str))
        self.assertEqual(test_str[0], char_iter.next_char())
        self.assertEqual(test_str[1], char_iter.next_char())
        self.assertEqual(test_str[2], char_iter.next_char())
        self.assertEqual(test_str[3], char_iter.next_char())

    def test_empty_iterator(self):
        char_iter = FileCharIter(io.StringIO(""))
        count = 0
        for char in char_iter:
            count += 1
        self.assertEqual(0, count)

    def test_advance_eof(self):
        test_str = "hello"
        char_iter = FileCharIter(io.StringIO(test_str))
        for i in test_str:
            char_iter.advance()
        self.assertEqual(False, char_iter.eof())
        char_iter.advance()
        self.assertEqual(True, char_iter.eof())

    def test_empy_eof(self):
        char_iter = FileCharIter(io.StringIO(""))
        self.assertEqual(False, char_iter.eof())
        char_iter.advance()
        self.assertEqual(True, char_iter.eof())

def suite():
    suite = unittest.TestSuite()
    suite.addTest(FileCharIterTest())
    return suite

if __name__ == '__main__':
    unittest.main()