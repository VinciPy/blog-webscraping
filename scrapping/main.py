import fire
import requests
from bs4 import BeautifulSoup as bs
from googlesearch import search


def start(keyword):

    links = search(f"{keyword} inurl:blog", num_results=0)
    link = str(links).replace('[', '')
    link = link.replace(']', '')
    link = link.replace("'", '')
    link = link.replace("'", '')
    request = scrapping(link)
    soup = bs(request.content, 'html.parser')
    contents = soup.find_all('p')
    for content in contents:
        if (len(content.get_text()) > 25):
            print(content.get_text())
        print(len(content.get_text()))    
    return 'a'


def scrapping(link):
    r = requests.get(link)
    return r

fire.Fire()