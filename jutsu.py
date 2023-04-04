import requests
from bs4 import BeautifulSoup
import re
import time
def jutsu(url,p):
    # URL of the page to parse

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Send a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    source_element = soup.findAll('source')

    # Get the src attribute value of the video source element
    for i in source_element:
        if i['res']==str(p):
            print(i['src'][:str(i['src']).index('?')])


def find_all_series(url,p):
    # URL of the page to parse

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Send a request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    name = url[15:-1]


    source_element = soup.findAll('a')
    for i in source_element:
        if name in i['href']:
            for j in i:
                if 'серия' in j:
                    j = re.sub('\ серия$', '', j)
                    jutsu(f'https://jut.su/{name}/episode-{j}.html',p)
                    time.sleep(1)


find_all_series('https://jut.su/katsute-kami/',1080)