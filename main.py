import time

import requests
from bs4 import BeautifulSoup


def html_parser(url):
    r = requests.get(url)
    return r.url, BeautifulSoup(r.text, 'html.parser')


def html_first_href(soup):
    for a in soup.find(id='mw-content-text').p.find_all('a'):
        if a['href'][0] != '#':
            return 'https://en.wikipedia.org{}'.format(a['href'])


url, soup = html_parser('https://en.wikipedia.org/wiki/Robin_Stewart')

article_chain = []

while soup.title.string.find('Philosophy') < 0 and not url in article_chain:
    print(soup.title.string)
    article_chain.append(url)
    url, soup = html_parser(html_first_href(soup))
    time.sleep(1)

print(article_chain)
