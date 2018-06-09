import re

# Returns acronym of string
def get_acronym(string):
    return "".join(sub[0] for sub in string.split())


# Removes special characters
def remove_specials(string):
    return re.sub(r'[^\w\s]', '', string)


# Removes remove_whitespace
def remove_whitespace(string):
    return string.replace(" ", '')


# Returns the episode code in the string
def get_episode(string):
    try:
        match = re.search(r'[sS]\d{2}.{0,1}[eE]\d{2}', string).group()
        return remove_whitespace(remove_specials(match.upper()))
    except:
        return None


# Returns the episode title in the string
def get_title(string):
    try:
        match = re.search(r'^[sS]\d{2}\s{1}[eE]\d{2}\s{1}.{1}\s{1}', string).group()
        return string.replace(match, '')
    except:
        return None
