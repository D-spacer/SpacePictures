import urllib.parse
import os


def extract_expansion(url):
    resulting_url = urllib.parse.urlsplit(url, scheme='', allow_fragments=True)
    expansion = os.path.splitext(resulting_url.path)[1]
    return expansion
