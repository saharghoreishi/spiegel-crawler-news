import datetime

import requests
import re
from bs4 import BeautifulSoup
import msql


def Crawl():
    global title
    url = 'https://www.spiegel.de/international/'
    urlcrawled = 'https://www.spiegel.de'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    weblinks = soup.find_all('a', {'href': True})
    # retrieve news linke from main page of site
    urls = re.findall('/international+[/a-z/]+(?:[-\w.]|(?:%[\da-fA-F]{2}))+.html', str(weblinks))
    for u in urls:
        strurl = "{0}{1}".format(urlcrawled, u)
        # """Scrapes information from pages into items"""
        pagez = requests.get(strurl)
        soupz = BeautifulSoup(pagez.content, 'html.parser')
        # now lets loop through  posts

        for tag in soupz.find_all("meta"):
            if tag.get("property", None) == "og:title":
                title = tag.get("content", None)

            elif tag.get("property", None) == "og:description":
                description = tag.get("content", None)
            elif tag.get("name", None) == "news_keywords":
                subtitle = tag.get("content", None)

        msql.Db(title, subtitle, description, datetime.datetime.utcnow())
