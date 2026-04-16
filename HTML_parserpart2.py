from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)
import sys
n = int(sys.stdin.readline())
html_content = "".join([sys.stdin.readline() for _ in range(n)])
parser = MyHTMLParser()
parser.feed(html_content)
parser.close()
