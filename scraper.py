import requests, re
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup

from parsing import get_episode, get_title
from settings import *

# Returns soup of html of url
def get_soup(url):
    try:
        page = requests.get(url, headers=HEADERS).content
        return BeautifulSoup(page, 'html.parser')
    except:
        return None


# Returns a chrome browser
def create_chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")                                                   # Maximizes
    options.add_argument("--incognito")                                                         # Incognito
    options.add_experimental_option("prefs", {"intl.accept_languages": "en-UK"})                # Ensures language is set to english
    browser = webdriver.Chrome(chrome_options=options)
    return browser


# Returns a dictionary with episode and title
def get_titles_list(query):
    titles = {}
    query = query.lower().replace(" ", "+")
    url = "https://www.google.com/search?q=list+of+{}+episodes".format(query)                   # Goodle search query
    browser = create_chrome_browser()
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    for text in [item.find(text=True) for item in soup.findAll("div", {"class": "title"})]:     # Episode titles
        code = get_episode(text)
        title = get_title(text)
        titles[code] = title

    browser.close()
    return titles


# Returns a dictionary with episode and download links in different qualities
def get_download_links(content_url):
    seasons = []
    links = {}

    content_soup = get_soup(content_url)
    if content_soup is None:
        return links

    for text in [item.find(text=True) for item in content_soup.find_all("a")]:                  # Each link is a subdirectory (season)
        if re.search(r'^[sS]\d{2}', text):
            seasons.append(text)

    for season in seasons:
        season_soup = get_soup(content_url + season)                                            # Checks each season for links

        for link in [item.get('href') for item in season_soup.find_all("a")]:
            episode = get_episode(link)

            if episode is not None:
                if episode in links:
                    links[episode].append(season + link)
                else:
                    mirrors = []
                    mirrors.append(season + link)
                    links[episode] = mirrors

    return links
