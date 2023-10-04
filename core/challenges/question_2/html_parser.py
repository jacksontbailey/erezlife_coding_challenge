class HTMLParser:
    """
    Class for parsing raw HTML strings and generating properly formatted output.

    Attributes:
        stack (list): Stack to keep track of opening and closing tags.
        output (list): List to store formatted HTML lines.
        current_indentation (int): Current level of indentation for formatting output.

    Methods:
        __init__(): Initializes an HTMLParser object with an empty stack, output, and current_indentation.
        parse_html(raw_html): Parses the raw HTML string and generates formatted output.
        _parse_tag(raw_html, start_index): Private method to parse a tag (opening or closing) in the raw HTML string.
        _parse_opening_tag(raw_html, start_index): Private method to parse an opening tag and update stack and output.
        _parse_closing_tag(raw_html, start_index): Private method to parse a closing tag and update stack and output.
        _extract_tag_name(raw_html, start_index): Private method to extract tag name from the raw HTML string.
    """
    def __init__(self):
        """
        Initializes an HTMLParser object with an empty stack, output, and current_indentation.
        """
        self.stack = []
        self.output = []
        self.current_indentation = 0

    def parse_html(self, raw_html):
        """
        Parses the raw HTML string and generates properly formatted output.

        Args:
            raw_html (str): Raw HTML string to be parsed.

        Returns:
            str: Formatted HTML output.
        """

        i = 0
        while i < len(raw_html):
            if raw_html[i] == '<':
                i = self._parse_tag(raw_html, i)
            i += 1

        if self.stack:
            return f"Error: Unclosed tag: {self.stack[-1]}"

        return '\n'.join(self.output)


    def _parse_tag(self, raw_html, start_index):
        """
        Private method to parse a tag (opening or closing) in the raw HTML string.

        Args:
            raw_html (str): Raw HTML string.
            start_index (int): Starting index of the tag in the raw HTML string.

        Returns:
            int: Updated index after parsing the tag.
        """
        if raw_html[start_index + 1] == '/':
            return self._parse_closing_tag(raw_html, start_index + 2)
        else:
            return self._parse_opening_tag(raw_html, start_index + 1)


    def _parse_opening_tag(self, raw_html, start_index):
        """
        Private method to parse an opening tag and update stack and output.

        Args:
            raw_html (str): Raw HTML string.
            start_index (int): Starting index of the opening tag in the raw HTML string.

        Returns:
            int: Updated index after parsing the opening tag.
        """
        tag_name, end_index = self._extract_tag_name(raw_html, start_index)
        if not tag_name:
            return end_index
        self.stack.append(tag_name)
        self.output.append('\t' * self.current_indentation + f'<{tag_name}>')
        self.current_indentation += 1
        return end_index


    def _parse_closing_tag(self, raw_html, start_index):
        """
        Private method to parse a closing tag and update stack and output.

        Args:
            raw_html (str): Raw HTML string.
            start_index (int): Starting index of the closing tag in the raw HTML string.

        Returns:
            int: Updated index after parsing the closing tag.
        """
        tag_name, end_index = self._extract_tag_name(raw_html, start_index)
        if not tag_name:
            return end_index
        if not self.stack or self.stack[-1] != tag_name:
            print(f"Error: Mismatched or unexpected closing tag: {tag_name}")
            return len(raw_html)
        self.stack.pop()
        self.current_indentation -= 1
        self.output.append('\t' * self.current_indentation + f'</{tag_name}>')
        return end_index


    def _extract_tag_name(self, raw_html, start_index):
        """
        Private method to extract tag name from the raw HTML string.

        Args:
            raw_html (str): Raw HTML string.
            start_index (int): Starting index of the tag in the raw HTML string.

        Returns:
            str: Extracted tag name.
            int: Updated index after extracting the tag name.
        """
        tag_name = ''
        i = start_index
        while i < len(raw_html) and raw_html[i] not in ['>', ' ', '/']:
            tag_name += raw_html[i]
            i += 1
        return tag_name, i


if __name__ == "__main__":
    # Test cases
    html_parser = HTMLParser()

    html1 = "<html><body><div></a></body></html>"
    html2 = "<html><body><div><a></div></a>"
    html3 = "<html><body><div><a></a></div></body></html>"


    print(html_parser.parse_html(html1))  # Should print an error message
    print(html_parser.parse_html(html2))  # Should print an error message
    print(html_parser.parse_html(html3))  # Should be correct 