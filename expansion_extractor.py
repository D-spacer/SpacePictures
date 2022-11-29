import urllib.parse
import os


def expansion_extractor(url):
    resulting_url = urllib.parse.urlsplit(url, scheme='', allow_fragments=True)
    expansion = os.path.splitext(resulting_url.path)[1]
    return expansion
