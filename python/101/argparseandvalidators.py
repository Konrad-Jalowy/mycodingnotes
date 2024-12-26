import argparse
import validators

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", action="store")

args = parser.parse_args()

url = args.url


def add_protocol(_url):
    if _url.startswith("https://") or _url.startswith("http://"):
        return url
    return "https://" + url


def is_url(_url):
    return True if validators.url(_url) else False


url = add_protocol(url)
print(url)
print(is_url(url))
