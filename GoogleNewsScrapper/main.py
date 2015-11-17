from bs4 import BeautifulSoup
import urllib.request
import pprint

class GoogleNewsSpider:

    def __init__(self):
        url = "https://news.google.com/"
        htmltext = urllib.request.urlopen(url).read()
        self.soup = BeautifulSoup(htmltext, "html.parser")

    def scrap(self):
        soup = self.soup
        clanky = []

        for tag in soup.findAll('table', {'class' : 'esc-layout-table'}):
            clanek = {}
            zprava = tag.tr.find('td', {'class' : 'esc-layout-article-cell'})
            clanek['nazev'] = zprava.find('span', {'class' : 'titletext'}).getText()
            clanek['odkaz'] = zprava.find('a', {'class' : 'article'}).get('url')
            clanky.append(clanek)
        return clanky

spider = GoogleNewsSpider()
clanky = spider.scrap()

pp = pprint.PrettyPrinter()
pp.pprint(clanky)