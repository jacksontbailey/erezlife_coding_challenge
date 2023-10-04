class HTMLParser:
    def __init__(self):
        self.stack = []
        self.output = []
        self.current_indentation = 0

    def parse_html(self, raw_html):
        i = 0
        while i < len(raw_html):
            if raw_html[i] == '<':
                i = self._parse_tag(raw_html, i)
            i += 1

        if self.stack:
            return f"Error: Unclosed tag: {self.stack[-1]}"

        return '\n'.join(self.output)


    def _parse_tag(self, raw_html, start_index):
        if raw_html[start_index + 1] == '/':
            return self._parse_closing_tag(raw_html, start_index + 2)
        else:
            return self._parse_opening_tag(raw_html, start_index + 1)


    def _parse_opening_tag(self, raw_html, start_index):
        tag_name, end_index = self._extract_tag_name(raw_html, start_index)
        if not tag_name:
            return end_index
        self.stack.append(tag_name)
        self.output.append('\t' * self.current_indentation + f'<{tag_name}>')
        self.current_indentation += 1
        return end_index


    def _parse_closing_tag(self, raw_html, start_index):
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