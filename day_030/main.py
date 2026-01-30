# Simulate web scraping logic (using concepts from BeautifulSoup)
from html.parser import HTMLParser

class SimpleParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            print(f"Found link: {dict(attrs).get('href')}")

html_content = """
<html>
    <body>
        <h1>My Favorite Links</h1>
        <a href="https://python.org">Python Official</a>
        <a href="https://github.com">GitHub</a>
    </body>
</html>
"""

print("Scraping links...")
parser = SimpleParser()
parser.feed(html_content)
