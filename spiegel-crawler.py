#Done By sahar Ghoreishi 2019/14/10
import datetime
from _csv import writer
import requests
import re
from bs4 import BeautifulSoup
import threading


def parse_page(response):
    """Scrapes information from pages into items"""
    pagez = requests.get (response)
    soupz = BeautifulSoup (pagez.content, 'html.parser')
    with open ('news.csv', 'w') as csv_file:
        csv_writer = writer (csv_file)  # creating headers in the csv file
        headers = ['Title', 'SubTitle', 'Abstract', 'InsertedDate']
        # writing a row of headers in the csv
        csv_writer.writerow (headers)
        # now lets loop through  posts
        for tag in soupz.find_all ("meta"):
            if tag.get ("property", None) == "og:title":
                title = tag.get ("content", None)
            elif tag.get ("property", None) == "og:description":
                description = tag.get ("content", None)
            elif tag.get ("name", None) == "news_keywords":
                subtitle = tag.get ("content", None)
                csv_writer.writerow ([title, subtitle, description, datetime.datetime.utcnow ()])
    csv_file.close ()


def ReadUrl():
    url = 'https://www.spiegel.de/international/'
    urlcrawled = 'https://www.spiegel.de'
    page = requests.get (url)
    soup = BeautifulSoup (page.content, 'html.parser')
    weblinks = soup.find_all ('a', {'href': True})
    #retrieve news linke from main page of site
    urls = re.findall ('/international+[/a-z/]+(?:[-\w.]|(?:%[\da-fA-F]{2}))+.html', str (weblinks))
    for u in urls:
        strurl = "{0}{1}".format (urlcrawled, u)
        parse_page (strurl)


threading.Timer (600.0, ReadUrl ()).start ()  # call the method each 10 min
