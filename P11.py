import urllib.request
import wget
import os
import bs4 as bs

def html_converter(url):
    page = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(page,'html.parser')
    text = soup.get_text()
    print(text)
    soup.get_text().strip
    file = url.split("/")[-1]
    path = "C:\\Users\\Asus\\python_practices"
    if os.path.exists(os.path.join(path,file)):
        print(file," already downloaded!")
    else:
        wget.download(url=url, out=path)

html_converter("https://www.g7website.com/website-categories/html-websites.html")

















