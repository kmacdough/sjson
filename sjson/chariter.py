

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
        self._current_line = ""
        self._cur_char_idx = 0
        self._cur_char = None

    def advance(self):
        """
        Advances this iterator a charectar
        :return: None
        """
        if self.eof():
            return
        self._cur_char_idx += 1
        if self._cur_char_idx >= len(self._current_line):
            self._current_line = self.file.readline()
            self._cur_char_idx = 0
            if self._current_line == "":
                self._cur_char = EOF
                return
        self._cur_char = self._current_line[self._cur_char_idx]

    def cur_char(self):
        """
        Returns the current character
        :return: next current as a string of length 1
        :rtype: str or EOF
        """
        return self._cur_char

    def next_char(self):
        """
        Returns the next character
        :return: next next as a string of length 1
        :rtype: str or EOF
        """
        self.advance()
        return self._cur_char

    def eof(self):
        """
        Determines if htis iterator is at the end of the file
        :return: True if at end, False otherwise
        :rtype: bool
        """
        return self._cur_char is EOF

    def __iter__(self):
        return self

    def __next__(self):
        next_char = self.next_char()
        if next_char is EOF:
            raise StopIteration
        return next_char


class EOF:
    """
    Represents the end of the file
    """
    pass
EOF = EOF()


def main():
    sys = __import__('sys')
    char_iter = FileCharIter(sys.stdin)
    for char in char_iter:
        print(repr(char))


if __name__ == "__main__":
    main()