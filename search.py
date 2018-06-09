import requests

from bs4 import BeautifulSoup
from requests.utils import requote_uri

from parsing import get_acronym, remove_specials
from settings import *

# Verify link
def verify_url(url):
	try:
	    request = requests.get(url, headers=HEADERS)
	    return request.status_code == 200
	except:
		return False


# Check query
def check_query(query, base_url=DEFAULT_BASE_URL):
    query_url = base_url + requote_uri(query) + "/"

    if verify_url(query_url):
        return query_url


# Returns list of possible queries
def generate_queries(content):
    q = []
    q.append(content)										# Plain text
    q.append(remove_specials(content))						# Without special characters
    q.append(get_acronym(content))							# Acronym

    for s in q:
        if s.upper() not in q:
            q.append(s.upper())
        if s.lower() not in q:
            q.append(s.lower())

    return q


# Checks each query for content , returns source url if found
def get_source_url(content):
    for q in generate_queries(content):
        result = check_query(q)
        if result is not None:
            return result
