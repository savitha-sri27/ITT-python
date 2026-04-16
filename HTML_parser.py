from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
if __name__ == "__main__":
    import sys
    try:
        n = int(sys.stdin.readline())
        html_content = "".join([sys.stdin.readline() for _ in range(n)])
        
        parser = MyHTMLParser()
        parser.feed(html_content)
    except EOFError:
        pass
