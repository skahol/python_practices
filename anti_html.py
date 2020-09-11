import urllib.request
from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
    


print('Beginning file download with urllib2...') 

urllib.request.urlretrieve("https://www.g7website.com/website-categories/html-websites.html", "data.html")

with open("./data.html","r+") as data:
    strip_tags(data).read()
