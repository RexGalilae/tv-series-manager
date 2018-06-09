import json, os

from settings import *
from scraper import get_download_links, get_titles_list
from search import get_source_url


# Reads JSON file and returns python list of episodes
def read_shows():
    if not os.path.exists(DATAFILE):
        dfile = open(DATAFILE, "w")
        dfile.close()

    dfile =  open(DATAFILE, "r+")
    try:
        shows = json.load(dfile)
        return shows
    except:
        return []


# Writes python list of episodes into JSON file
def write_shows(shows):
    with open(DATAFILE, "w+") as dfile:
        json.dump(shows, dfile, indent=4)


# Wrtes an entry of a new show
def create_show(name):
    source = get_source_url(name)
    if source is None:
        return

    print("Source acquired, retrieving links...")
    episodes = []
    links = get_download_links(source)                  # dictionary of download links
    titles = get_titles_list(name)                      # dictionary of titles

    for code in links:
        episode = {
            "code" : code,
            "title" : titles.get(code),
            "mirrors" : links.get(code),
            "local" : None
        }
        episodes.append(episode)

    show = {
        "name" : name,
        "source" : source,
        "episodes" : episodes
    }

    shows = read_shows()
    shows.append(show)
    write_shows(shows)
    print("Successfully added to playlist!")


def update_show(index):
    shows = read_shows()
    show = shows[index]
    links = get_download_links(show.get("source"))
    titles = get_titles_list(show.get("name"))
    episodes = show.get("episodes")

    for code in links:
        episode = next((e for e in episodes if e["code"] == code), None)
        if episode is not None:                                             # If episode is already in list
            i = episodes.index(episode)
            episode["mirrors"] = links.get(code)
            episode["title"] = titles.get(code)
            episodes[i] = episode
        else:                                                               # New episode
            episode = {
                "code" : code,
                "title" : titles.get(code),
                "mirrors" : links.get(code),
                "local" : None
            }
            episodes.append(episode)

    show["episodes"] = episodes
    shows[index] = show
    write_shows(shows)
    print("Successfully updated!")
