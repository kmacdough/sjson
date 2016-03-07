

class FileCharIter(object):
    """
    Class for iterating over individual characters of a file.
    """
    def __init__(self, file):
        """
        Creates a FileCharIter over the given file
        :param file: file-like object to be iterated over
        :type file: file-like
        :return: None
        """
        self.file = file
        self.current_line = ""
        self.cur_char_idx = 0

    def advance(self):
        """
        Advances this iterator a charectar
        :return: None
        """
        self.cur_char_idx += 1
        if self.cur_char_idx >= len(self.current_line):
            self.current_line = self.file.readline()
            self.cur_char_idx = 0

    def cur_char(self):
        """
        Returns the current character
        :return: next current as a string of length 1
        :rtype: str
        """
        print(repr(self.current_line), self.cur_char_idx)
        return self.current_line[self.cur_char_idx]

    def eof(self):
        """
        Determines if htis iterator is at the end of the file
        :return: True if at end, False otherwise
        :rtype: bool
        """
        return self.current_line == ""


def main():
    sys = __import__('sys')
    char_iter = FileCharIter(sys.stdin)
    char_iter.advance()
    while not char_iter.eof():
        print(repr(char_iter.cur_charance()()))
        char_iter.adv


if __name__ == "__main__":
    main()