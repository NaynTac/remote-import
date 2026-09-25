from url_finder import URLFinder

import re
import requests


def url_hook(some_str):
    
    if not some_str.startswith(("http", "https")):
        raise ImportError
        
    try:
        response = requests.get(some_str)
        data = response.text
    except Exception as exc:
        raise ImportError(f"Хост недоступен!: {exc}")
        
    filenames = re.findall("[a-zA-Z_][a-zA-Z0-9_]*.py", data)
    modnames = {name[:-3] for name in filenames}
    
    return URLFinder(some_str, modnames)