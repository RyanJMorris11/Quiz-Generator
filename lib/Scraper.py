import bs4 as bs
import urllib.request


class Scraper:


    def scan_and_scrape(self, kw):
        data = {}
        count = 1
        sauce = urllib.request.urlopen('https://quizlet.com/subject/'+ kw + '/').read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
 
        for div in soup.find_all("div", {"class": "UILinkBox-link"}):
            souce = urllib.request.urlopen(div.a.get('href')).read()
            stone_soup = bs.BeautifulSoup(souce, 'lxml')

            for span in stone_soup.find_all("span", {"class": "TermText notranslate lang-en"}):
                data[count] = span.text
                count += 1
    
        return data
